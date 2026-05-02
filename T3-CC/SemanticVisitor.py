from LAVisitor import LAVisitor
from LAParser import LAParser
from SymbolTable import SymbolTable

class SemanticVisitor(LAVisitor):
    def __init__(self, outfile):
        self.outfile = outfile
        self.symtable = SymbolTable()
        self.errors = []

    def add_error(self, line, msg):
        self.errors.append(f"Linha {line}: {msg}")

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

    def is_compatible(self, target, source):
        if target == source:
            return True
        if target == 'real' and source == 'inteiro':
            return True
        if target == 'inteiro' and source == 'real':
            return True # In LA, real can be assigned to inteiro? The specs say (real | inteiro) <- (real | inteiro)
        # Pointers: ponteiro <- endereco (needs & operator? We'll see)
        return False

    def visitPrograma(self, ctx:LAParser.ProgramaContext):
        self.visitChildren(ctx)
        return None

    def visitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        if ctx.getText().startswith('declare'):
            self.visit(ctx.variavel())
        elif ctx.getText().startswith('constante'):
            pass # TODO
        elif ctx.getText().startswith('tipo'):
            pass # TODO
        return None

    def visitVariavel(self, ctx:LAParser.VariavelContext):
        tipo_ctx = ctx.tipo()
        tipo_str = tipo_ctx.getText()
        
        if not self.resolve_type(tipo_str):
            self.add_error(ctx.start.line, f"tipo {tipo_str} nao declarado")
            tipo_resolvido = "tipo_erro"
        else:
            tipo_resolvido = tipo_str

        for ident_ctx in ctx.identificador():
            nome_var = ident_ctx.getText()
            if not self.symtable.add(nome_var, 'variavel', tipo_resolvido):
                self.add_error(ident_ctx.start.line, f"identificador {nome_var} ja declarado anteriormente")
        return None

    def visitCmdAtribuicao(self, ctx:LAParser.CmdAtribuicaoContext):
        ident_ctx = ctx.identificador()
        nome_var = ident_ctx.getText()
        is_pointer = ctx.getText().startswith('^')
        
        sym = self.symtable.get(nome_var)
        if not sym:
            self.add_error(ident_ctx.start.line, f"identificador {nome_var} nao declarado")
            self.visit(ctx.expressao())
            return None
            
        target_type = sym['type']
        if is_pointer and target_type and target_type.startswith('^'):
            target_type = target_type[1:]
            
        expr_type = self.visit(ctx.expressao())
        
        if expr_type == "tipo_erro" or target_type == "tipo_erro":
            return None
            
        if expr_type == "tipo_indefinido" or not self.is_compatible(target_type, expr_type):
            full_var_name = "^" + nome_var if is_pointer else nome_var
            self.add_error(ident_ctx.start.line, f"atribuicao nao compativel para {full_var_name}")
            
        return None

    def visitCmdLeia(self, ctx:LAParser.CmdLeiaContext):
        for ident_ctx in ctx.identificador():
            nome_var = ident_ctx.getText()
            if not self.symtable.get(nome_var):
                self.add_error(ident_ctx.start.line, f"identificador {nome_var} nao declarado")
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
        nome_func = ctx.IDENT().getText()
        if not self.symtable.get(nome_func):
            self.add_error(ctx.IDENT().symbol.line, f"identificador {nome_func} nao declarado")
        for exp in ctx.expressao():
            self.visit(exp)
        return None

    def visitCmdRetorne(self, ctx:LAParser.CmdRetorneContext):
        self.visit(ctx.expressao())
        return None

    def visitExpressao(self, ctx:LAParser.ExpressaoContext):
        types = [self.visit(t) for t in ctx.termo_logico()]
        if "tipo_erro" in types:
            return "tipo_erro"
        if "tipo_indefinido" in types:
            return "tipo_indefinido"
        if len(types) == 1:
            return types[0]
        for t in types:
            if t != 'logico':
                return "tipo_indefinido"
        return "logico"

    def visitTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        types = [self.visit(f) for f in ctx.fator_logico()]
        if "tipo_erro" in types:
            return "tipo_erro"
        if "tipo_indefinido" in types:
            return "tipo_indefinido"
        if len(types) == 1:
            return types[0]
        for t in types:
            if t != 'logico':
                return "tipo_indefinido"
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
        if "tipo_erro" in types:
            return "tipo_erro"
        if "tipo_indefinido" in types:
            return "tipo_indefinido"
        if len(types) == 1:
            return types[0]
        if not self.is_compatible(types[0], types[1]):
            return "tipo_indefinido"
        return "logico"

    def visitExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        types = [self.visit(t) for t in ctx.termo()]
        if "tipo_erro" in types:
            return "tipo_erro"
        if "tipo_indefinido" in types:
            return "tipo_indefinido"
        if len(types) == 1:
            return types[0]
        
        res = types[0]
        for op_ctx, t in zip(ctx.op1(), types[1:]):
            op = op_ctx.getText()
            if op == '+':
                if res == 'literal' and t == 'literal':
                    res = 'literal'
                elif res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                    if res == 'real' or t == 'real':
                        res = 'real'
                    else:
                        res = 'inteiro'
                else:
                    return "tipo_indefinido"
            elif op == '-':
                if res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                    if res == 'real' or t == 'real':
                        res = 'real'
                    else:
                        res = 'inteiro'
                else:
                    return "tipo_indefinido"
        return res

    def visitTermo(self, ctx:LAParser.TermoContext):
        types = [self.visit(f) for f in ctx.fator()]
        if "tipo_erro" in types:
            return "tipo_erro"
        if "tipo_indefinido" in types:
            return "tipo_indefinido"
        if len(types) == 1:
            return types[0]
        res = types[0]
        for t in types[1:]:
            if res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                if res == 'real' or t == 'real':
                    res = 'real'
                else:
                    res = 'inteiro'
            else:
                return "tipo_indefinido"
        return res

    def visitFator(self, ctx:LAParser.FatorContext):
        types = [self.visit(p) for p in ctx.parcela()]
        if "tipo_erro" in types:
            return "tipo_erro"
        if "tipo_indefinido" in types:
            return "tipo_indefinido"
        if len(types) == 1:
            return types[0]
        res = types[0]
        for t in types[1:]:
            if res in ['inteiro', 'real'] and t in ['inteiro', 'real']:
                if res == 'real' or t == 'real':
                    res = 'real'
                else:
                    res = 'inteiro'
            else:
                return "tipo_indefinido"
        return res

    def visitParcela(self, ctx:LAParser.ParcelaContext):
        if ctx.parcela_unaria():
            return self.visit(ctx.parcela_unaria())
        else:
            return self.visit(ctx.parcela_nao_unaria())

    def visitParcela_unaria(self, ctx:LAParser.Parcela_unariaContext):
        if ctx.NUM_INT():
            return 'inteiro'
        if ctx.NUM_REAL():
            return 'real'
        if ctx.IDENT():
            nome_func = ctx.IDENT().getText()
            sym = self.symtable.get(nome_func)
            if not sym:
                self.add_error(ctx.IDENT().symbol.line, f"identificador {nome_func} nao declarado")
            for expr in ctx.expressao():
                self.visit(expr)
            return sym['type'] if sym else "tipo_erro"
            
        if ctx.identificador():
            nome_var = ctx.identificador().getText()
            sym = self.symtable.get(nome_var)
            if not sym:
                self.add_error(ctx.identificador().start.line, f"identificador {nome_var} nao declarado")
                return "tipo_erro"
            t = sym['type']
            if ctx.getText().startswith('^'):
                if t.startswith('^'):
                    return t[1:]
                else:
                    return "tipo_indefinido"
            return t
        
        if ctx.expressao():
            return self.visit(ctx.expressao(0))
            
        return "tipo_indefinido"

    def visitParcela_nao_unaria(self, ctx:LAParser.Parcela_nao_unariaContext):
        if ctx.CADEIA():
            return 'literal'
        if ctx.identificador():
            nome_var = ctx.identificador().getText()
            sym = self.symtable.get(nome_var)
            if not sym:
                self.add_error(ctx.identificador().start.line, f"identificador {nome_var} nao declarado")
                return "tipo_erro"
            return "^" + sym['type']
        return "tipo_indefinido"

