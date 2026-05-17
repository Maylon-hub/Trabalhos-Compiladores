from LAVisitor import LAVisitor
from LAParser import LAParser
from SymbolTable import SymbolTable

class SemanticVisitor(LAVisitor):
    def __init__(self, outfile):
        self.outfile = outfile
        self.symtable = SymbolTable()
        self.errors = []
        self.reported_errors = set()

    def add_error(self, line, msg):
        err = f"Linha {line}: {msg}"
        if err not in self.reported_errors:
            self.errors.append(err)
            self.reported_errors.add(err)

    def write_errors(self):
        for e in self.errors:
            self.outfile.write(e + "\n")
        self.outfile.write("Fim da compilacao\n")

    def resolve_type(self, type_str):
        if type_str.startswith('^'):
            base = type_str[1:]
            if not self.symtable.exists(base):
                return None
            return type_str
        if not self.symtable.exists(type_str):
            return None
        return type_str

    def is_compatible(self, target, source, exact=False):
        if target == source:
            return True
        if not exact and target == 'real' and source == 'inteiro':
            return True
        return False

    def get_registro_fields(self, ctx_registro):
        fields = {}
        for var_ctx in ctx_registro.variavel():
            tipo_str = var_ctx.tipo().getText()
            tipo_resolvido = self.resolve_type(tipo_str) or "tipo_erro"
            if tipo_resolvido == "tipo_erro":
                self.add_error(var_ctx.start.line, f"tipo {tipo_str} nao declarado")
            for ident_ctx in var_ctx.identificador():
                fields[ident_ctx.getText()] = tipo_resolvido
        return fields

    def resolve_identificador(self, ident_ctx):
        nome_base = ident_ctx.IDENT(0).getText()
        sym = self.symtable.get(nome_base)
        if not sym:
            self.add_error(ident_ctx.start.line, f"identificador {ident_ctx.getText()} nao declarado")
            return "tipo_erro"
            
        current_type = sym['type']
        
        # Traverse nested properties like ponto1.x
        for i in range(1, len(ident_ctx.IDENT())):
            campo = ident_ctx.IDENT(i).getText()
            fields = None
            if i == 1:
                fields = sym.get('fields')
            
            if not fields:
                type_sym = self.symtable.get(current_type)
                if type_sym and type_sym.get('fields'):
                    fields = type_sym['fields']
                    
            if not fields or campo not in fields:
                self.add_error(ident_ctx.start.line, f"identificador {ident_ctx.getText()} nao declarado")
                return "tipo_erro"
            
            current_type = fields[campo]
            
        # Visit dimensions to catch undeclared vars in array index
        if ident_ctx.dimensao():
            for exp in ident_ctx.dimensao().exp_aritmetica():
                self.visit(exp)
                
        return current_type

    def check_function_call(self, line, nome_func, expressions_ctx):
        sym = self.symtable.get(nome_func)
        if not sym:
            self.add_error(line, f"identificador {nome_func} nao declarado")
            for expr in expressions_ctx:
                self.visit(expr)
            return "tipo_erro"
            
        params = sym.get('params') or []
        args_types = [self.visit(expr) for expr in expressions_ctx]
        
        if len(args_types) != len(params):
            self.add_error(line, f"incompatibilidade de parametros na chamada de {nome_func}")
        else:
            for arg_t, param in zip(args_types, params):
                if arg_t == "tipo_erro":
                    continue
                if not self.is_compatible(param['type'], arg_t, exact=True):
                    self.add_error(line, f"incompatibilidade de parametros na chamada de {nome_func}")
                    break
                    
        return sym['type'] or "tipo_erro"

    def visitPrograma(self, ctx:LAParser.ProgramaContext):
        self.visitChildren(ctx)
        return None

    def visitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        is_funcao = ctx.getText().startswith('funcao')
        nome = ctx.IDENT().getText()
        
        tipo_retorno = None
        if is_funcao:
            tipo_retorno = self.resolve_type(ctx.tipo_estendido().getText())
            if not tipo_retorno:
                tipo_retorno = "tipo_erro"
                
        params = []
        if ctx.parametros():
            for param_ctx in ctx.parametros().parametro():
                param_tipo_str = param_ctx.tipo_estendido().getText()
                param_tipo = self.resolve_type(param_tipo_str) or "tipo_erro"
                for ident_ctx in param_ctx.identificador():
                    params.append({'name': ident_ctx.IDENT(0).getText(), 'type': param_tipo})
                    
        if not self.symtable.add(nome, 'funcao' if is_funcao else 'procedimento', tipo_retorno, params):
            self.add_error(ctx.IDENT().symbol.line, f"identificador {nome} ja declarado anteriormente")
            
        self.symtable.enter_scope()
        for p in params:
            self.symtable.add(p['name'], 'variavel', p['type'])
            
        prev_context = getattr(self, 'current_global_context', None)
        self.current_global_context = 'funcao' if is_funcao else 'procedimento'
        
        for decl in ctx.declaracao_local():
            self.visit(decl)
        for cmd in ctx.cmd():
            self.visit(cmd)
            
        self.current_global_context = prev_context
        self.symtable.exit_scope()
        return None

    def visitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        if ctx.getText().startswith('declare'):
            self.visit(ctx.variavel())
        elif ctx.getText().startswith('tipo'):
            nome_tipo = ctx.IDENT().getText()
            tipo_ctx = ctx.tipo()
            if tipo_ctx.registro():
                fields = self.get_registro_fields(tipo_ctx.registro())
                self.symtable.add_type(nome_tipo, 'registro', fields)
            else:
                base_type = self.resolve_type(tipo_ctx.getText()) or "tipo_erro"
                self.symtable.add_type(nome_tipo, base_type)
        elif ctx.getText().startswith('constante'):
            nome = ctx.IDENT().getText()
            tipo = self.resolve_type(ctx.tipo_basico().getText()) or "tipo_erro"
            if not self.symtable.add(nome, 'constante', tipo):
                self.add_error(ctx.IDENT().symbol.line, f"identificador {nome} ja declarado anteriormente")
        return None

    def visitVariavel(self, ctx:LAParser.VariavelContext):
        tipo_ctx = ctx.tipo()
        fields = None
        if tipo_ctx.registro():
            tipo_resolvido = 'registro'
            fields = self.get_registro_fields(tipo_ctx.registro())
        else:
            tipo_str = tipo_ctx.getText()
            tipo_resolvido = self.resolve_type(tipo_str)
            if not tipo_resolvido:
                self.add_error(ctx.start.line, f"tipo {tipo_str} nao declarado")
                tipo_resolvido = "tipo_erro"
            else:
                sym_type = self.symtable.get(tipo_str)
                if sym_type and sym_type['category'] == 'tipo' and sym_type.get('fields'):
                    tipo_resolvido = tipo_str 
        
        for ident_ctx in ctx.identificador():
            nome_var = ident_ctx.IDENT(0).getText()
            
            if ident_ctx.dimensao():
                for exp in ident_ctx.dimensao().exp_aritmetica():
                    self.visit(exp)
                    
            if not self.symtable.add(nome_var, 'variavel', tipo_resolvido, fields=fields):
                self.add_error(ident_ctx.start.line, f"identificador {nome_var} ja declarado anteriormente")
        return None

    def visitCmdAtribuicao(self, ctx:LAParser.CmdAtribuicaoContext):
        ident_ctx = ctx.identificador()
        is_pointer = ctx.getText().startswith('^')
        
        target_type = self.resolve_identificador(ident_ctx)
        
        if target_type != "tipo_erro" and is_pointer:
            if target_type.startswith('^'):
                target_type = target_type[1:]
            else:
                target_type = "tipo_erro"
                
        expr_type = self.visit(ctx.expressao())
        
        if expr_type == "tipo_erro" or target_type == "tipo_erro":
            return None
            
        if expr_type == "tipo_indefinido" or not self.is_compatible(target_type, expr_type):
            full_var_name = ctx.getText().split('<-')[0]
            self.add_error(ident_ctx.start.line, f"atribuicao nao compativel para {full_var_name}")
            
        return None

    def visitCmdLeia(self, ctx:LAParser.CmdLeiaContext):
        for ident_ctx in ctx.identificador():
            self.resolve_identificador(ident_ctx)
        return None

    def visitCmdEscreva(self, ctx:LAParser.CmdEscrevaContext):
        for expr in ctx.expressao():
            self.visit(expr)
        return None

    def visitCmdSe(self, ctx:LAParser.CmdSeContext):
        self.visit(ctx.expressao())
        for cmd in ctx.cmd():
            self.visit(cmd)
        return None

    def visitCmdCaso(self, ctx:LAParser.CmdCasoContext):
        self.visit(ctx.exp_aritmetica())
        self.visit(ctx.selecao())
        for cmd in ctx.cmd():
            self.visit(cmd)
        return None

    def visitCmdPara(self, ctx:LAParser.CmdParaContext):
        nome_var = ctx.IDENT().getText()
        if not self.symtable.get(nome_var):
            self.add_error(ctx.IDENT().symbol.line, f"identificador {nome_var} nao declarado")
        for exp in ctx.exp_aritmetica():
            self.visit(exp)
        for cmd in ctx.cmd():
            self.visit(cmd)
        return None

    def visitCmdEnquanto(self, ctx:LAParser.CmdEnquantoContext):
        self.visit(ctx.expressao())
        for cmd in ctx.cmd():
            self.visit(cmd)
        return None

    def visitCmdFaca(self, ctx:LAParser.CmdFacaContext):
        self.visit(ctx.expressao())
        for cmd in ctx.cmd():
            self.visit(cmd)
        return None

    def visitCmdChamada(self, ctx:LAParser.CmdChamadaContext):
        self.check_function_call(ctx.IDENT().symbol.line, ctx.IDENT().getText(), ctx.expressao())
        return None

    def visitCmdRetorne(self, ctx:LAParser.CmdRetorneContext):
        if getattr(self, 'current_global_context', None) != 'funcao':
            self.add_error(ctx.start.line, "comando retorne nao permitido nesse escopo")
        self.visit(ctx.expressao())
        return None

    def visitExpressao(self, ctx:LAParser.ExpressaoContext):
        types = [self.visit(t) for t in ctx.termo_logico()]
        if "tipo_erro" in types: return "tipo_erro"
        if "tipo_indefinido" in types: return "tipo_indefinido"
        if len(types) == 1: return types[0]
        for t in types:
            if t != 'logico': return "tipo_indefinido"
        return "logico"

    def visitTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        types = [self.visit(f) for f in ctx.fator_logico()]
        if "tipo_erro" in types: return "tipo_erro"
        if "tipo_indefinido" in types: return "tipo_indefinido"
        if len(types) == 1: return types[0]
        for t in types:
            if t != 'logico': return "tipo_indefinido"
        return "logico"

    def visitFator_logico(self, ctx:LAParser.Fator_logicoContext):
        t = self.visit(ctx.parcela_logica())
        if ctx.getText().startswith('nao'):
            if t == "tipo_erro": return "tipo_erro"
            if t != 'logico': return "tipo_indefinido"
        return t

    def visitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            return self.visit(ctx.exp_relacional())
        return 'logico'

    def visitExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        types = [self.visit(e) for e in ctx.exp_aritmetica()]
        if "tipo_erro" in types: return "tipo_erro"
        if "tipo_indefinido" in types: return "tipo_indefinido"
        if len(types) == 1: return types[0]
        if not self.is_compatible(types[0], types[1]):
            return "tipo_indefinido"
        return "logico"

    def visitExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        types = [self.visit(t) for t in ctx.termo()]
        if "tipo_erro" in types: return "tipo_erro"
        if "tipo_indefinido" in types: return "tipo_indefinido"
        if len(types) == 1: return types[0]
        
        res = types[0]
        for op_ctx, t in zip(ctx.op1(), types[1:]):
            op = op_ctx.getText()
            if op == '+':
                if res == 'literal' and t == 'literal': res = 'literal'
                elif res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                    res = 'real' if res == 'real' or t == 'real' else 'inteiro'
                else: return "tipo_indefinido"
            elif op == '-':
                if res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                    res = 'real' if res == 'real' or t == 'real' else 'inteiro'
                else: return "tipo_indefinido"
        return res

    def visitTermo(self, ctx:LAParser.TermoContext):
        types = [self.visit(f) for f in ctx.fator()]
        if "tipo_erro" in types: return "tipo_erro"
        if "tipo_indefinido" in types: return "tipo_indefinido"
        if len(types) == 1: return types[0]
        res = types[0]
        for t in types[1:]:
            if res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                res = 'real' if res == 'real' or t == 'real' else 'inteiro'
            else: return "tipo_indefinido"
        return res

    def visitFator(self, ctx:LAParser.FatorContext):
        types = [self.visit(p) for p in ctx.parcela()]
        if "tipo_erro" in types: return "tipo_erro"
        if "tipo_indefinido" in types: return "tipo_indefinido"
        if len(types) == 1: return types[0]
        res = types[0]
        for t in types[1:]:
            if res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                res = 'real' if res == 'real' or t == 'real' else 'inteiro'
            else: return "tipo_indefinido"
        return res

    def visitParcela(self, ctx:LAParser.ParcelaContext):
        if ctx.parcela_unaria():
            return self.visit(ctx.parcela_unaria())
        else:
            return self.visit(ctx.parcela_nao_unaria())

    def visitParcela_unaria(self, ctx:LAParser.Parcela_unariaContext):
        if ctx.NUM_INT(): return 'inteiro'
        if ctx.NUM_REAL(): return 'real'
        if ctx.IDENT():
            return self.check_function_call(ctx.IDENT().symbol.line, ctx.IDENT().getText(), ctx.expressao())
            
        if ctx.identificador():
            target_type = self.resolve_identificador(ctx.identificador())
            if ctx.getText().startswith('^'):
                if target_type.startswith('^'):
                    return target_type[1:]
                else:
                    return "tipo_indefinido"
            return target_type
        
        if ctx.expressao():
            return self.visit(ctx.expressao(0))
            
        return "tipo_indefinido"

    def visitParcela_nao_unaria(self, ctx:LAParser.Parcela_nao_unariaContext):
        if ctx.CADEIA(): return 'literal'
        if ctx.identificador():
            target_type = self.resolve_identificador(ctx.identificador())
            if target_type == "tipo_erro": return "tipo_erro"
            return "^" + target_type
        return "tipo_indefinido"
