from LAVisitor import LAVisitor
from LAParser import LAParser
from SymbolTable import SymbolTable

class CodeGeneratorVisitor(LAVisitor):
    def __init__(self, symtable):
        self.symtable = SymbolTable() # Use a fresh one and populate it to track scopes accurately
        self.output = []
        self.indent_level = 0
        
    def add_line(self, line):
        self.output.append("    " * self.indent_level + line)
        
    def map_type(self, la_type):
        if la_type == 'inteiro':
            return 'int'
        if la_type == 'real':
            return 'float'
        if la_type == 'literal':
            return 'char' # Used with [80] in declarations
        if la_type == 'logico':
            return 'int' # Using int for boolean
        if la_type.startswith('^'):
            return self.map_type(la_type[1:]) + '*'
        return la_type # Custom types like tVinho
        
    def is_literal(self, la_type):
        return la_type == 'literal'
        
    def resolve_type(self, ident_ctx):
        nome_base = ident_ctx.IDENT(0).getText()
        sym = self.symtable.get(nome_base)
        if not sym:
            return "inteiro"
            
        current_type = sym['type']
        for i in range(1, len(ident_ctx.IDENT())):
            campo = ident_ctx.IDENT(i).getText()
            fields = None
            if i == 1:
                fields = sym.get('fields')
            if not fields:
                type_sym = self.symtable.get(current_type)
                if type_sym and type_sym.get('fields'):
                    fields = type_sym['fields']
            if fields and campo in fields:
                current_type = fields[campo]
        return current_type

    def visitPrograma(self, ctx:LAParser.ProgramaContext):
        self.add_line("#include <stdio.h>")
        self.add_line("#include <stdlib.h>")
        self.add_line("#include <string.h>")
        self.add_line("")
        
        for decl in ctx.declaracoes().decl_local_global():
            self.visit(decl)
            
        self.add_line("int main() {")
        self.indent_level += 1
        self.symtable.enter_scope()
        
        for decl in ctx.corpo().declaracao_local():
            self.visit(decl)
            
        for cmd in ctx.corpo().cmd():
            self.visit(cmd)
            
        self.add_line("return 0;")
        self.symtable.exit_scope()
        self.indent_level -= 1
        self.add_line("}")
        return "\n".join(self.output)

    def visitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        is_funcao = ctx.getText().startswith('funcao')
        nome = ctx.IDENT().getText()
        
        if is_funcao:
            tipo_retorno = self.map_type(ctx.tipo_estendido().getText())
            if ctx.tipo_estendido().getText() == 'literal':
                tipo_retorno = 'char*'
        else:
            tipo_retorno = 'void'
            
        params = []
        if ctx.parametros():
            for param_ctx in ctx.parametros().parametro():
                param_tipo = param_ctx.tipo_estendido().getText()
                c_tipo = self.map_type(param_tipo)
                if param_tipo == 'literal':
                    c_tipo = 'char*'
                is_ptr = param_ctx.getText().startswith('var')
                
                for ident_ctx in param_ctx.identificador():
                    nome_param = ident_ctx.getText()
                    if is_ptr:
                        params.append(f"{c_tipo}* {nome_param}")
                    else:
                        params.append(f"{c_tipo} {nome_param}")
                        
        params_str = ", ".join(params)
        self.add_line(f"{tipo_retorno} {nome}({params_str}) {{")
        self.indent_level += 1
        self.symtable.enter_scope()
        
        if ctx.parametros():
            for param_ctx in ctx.parametros().parametro():
                param_tipo = param_ctx.tipo_estendido().getText()
                for ident_ctx in param_ctx.identificador():
                    self.symtable.add(ident_ctx.IDENT(0).getText(), 'variavel', var_type=param_tipo)
        
        for decl in ctx.declaracao_local():
            self.visit(decl)
        for cmd in ctx.cmd():
            self.visit(cmd)
            
        self.symtable.exit_scope()
        self.indent_level -= 1
        self.add_line("}")
        self.add_line("")
        return None

    def visitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        if ctx.getText().startswith('declare'):
            self.visit(ctx.variavel())
        elif ctx.getText().startswith('tipo'):
            nome_tipo = ctx.IDENT().getText()
            if ctx.tipo().registro():
                fields = {}
                self.add_line(f"typedef struct {{")
                self.indent_level += 1
                for var_ctx in ctx.tipo().registro().variavel():
                    tipo_la = var_ctx.tipo().getText()
                    for ident_ctx in var_ctx.identificador():
                        fields[ident_ctx.IDENT(0).getText()] = tipo_la
                    self.visit(var_ctx)
                self.indent_level -= 1
                self.add_line(f"}} {nome_tipo};")
                self.symtable.add(nome_tipo, 'tipo', var_type='registro', fields=fields)
            else:
                base_type = self.map_type(ctx.tipo().getText())
                self.add_line(f"typedef {base_type} {nome_tipo};")
                self.symtable.add(nome_tipo, 'tipo', var_type=ctx.tipo().getText())
        elif ctx.getText().startswith('constante'):
            nome = ctx.IDENT().getText()
            tipo = self.map_type(ctx.tipo_basico().getText())
            valor = ctx.valor_constante().getText()
            self.add_line(f"const {tipo} {nome} = {valor};")
            self.symtable.add(nome, 'constante', var_type=ctx.tipo_basico().getText())
        return None

    def visitVariavel(self, ctx:LAParser.VariavelContext):
        if ctx.tipo().registro():
            fields = {}
            self.add_line("struct {")
            self.indent_level += 1
            for var_ctx in ctx.tipo().registro().variavel():
                tipo_la = var_ctx.tipo().getText()
                for ident_ctx in var_ctx.identificador():
                    fields[ident_ctx.IDENT(0).getText()] = tipo_la
                self.visit(var_ctx)
            self.indent_level -= 1
            self.add_line("} " + ", ".join([ident.getText() for ident in ctx.identificador()]) + ";")
            
            for ident_ctx in ctx.identificador():
                self.symtable.add(ident_ctx.IDENT(0).getText(), 'variavel', var_type='registro', fields=fields)
        else:
            tipo_la = ctx.tipo().getText()
            tipo_c = self.map_type(tipo_la)
            for ident_ctx in ctx.identificador():
                nome = ident_ctx.getText()
                self.symtable.add(ident_ctx.IDENT(0).getText(), 'variavel', var_type=tipo_la)
                if self.is_literal(tipo_la):
                    if ident_ctx.dimensao().getText():
                        dim = ident_ctx.dimensao().getText()
                        self.add_line(f"{tipo_c} {ident_ctx.IDENT(0).getText()}{dim}[80];")
                    else:
                        self.add_line(f"{tipo_c} {nome}[80];")
                else:
                    self.add_line(f"{tipo_c} {nome};")
        return None

    def get_c_format(self, la_type):
        if la_type == 'inteiro': return '%d'
        if la_type == 'real': return '%f'
        if la_type == 'literal': return '%s'
        if la_type == 'logico': return '%d'
        return '%d'

    def visitCmdLeia(self, ctx:LAParser.CmdLeiaContext):
        for ident_ctx in ctx.identificador():
            nome = ident_ctx.getText()
            tipo_la = self.resolve_type(ident_ctx)
            if tipo_la == 'literal':
                self.add_line(f"gets({nome});")
            else:
                fmt = self.get_c_format(tipo_la)
                self.add_line(f"scanf(\"{fmt}\", &{nome});")
        return None

    def visitCmdEscreva(self, ctx:LAParser.CmdEscrevaContext):
        for expr in ctx.expressao():
            # For writes, we should determine the format string dynamically if possible
            # But the expression type is complex. 
            # In LA, writes usually just output values. Let's do a simple heuristic for printf or use a helper to get expr type.
            expr_str = self.visit(expr)
            tipo_la = self.get_expr_type(expr)
            fmt = self.get_c_format(tipo_la)
            
            # Remove quotes if literal
            if tipo_la == 'literal' and expr_str.startswith('"') and expr_str.endswith('"'):
                # direct literal string
                self.add_line(f"printf({expr_str});")
            else:
                self.add_line(f"printf(\"{fmt}\", {expr_str});")
        return None
        
    def get_expr_type(self, ctx):
        text = ctx.getText()
        if text.startswith('"'): return 'literal'
        if text.isdigit(): return 'inteiro'
        if '.' in text and text.replace('.','',1).isdigit(): return 'real'
        
        try:
            ident = ctx.termo_logico(0).fator_logico(0).parcela_logica().exp_relacional().exp_aritmetica(0).termo(0).fator(0).parcela(0)
            if ident and ident.parcela_unaria() and ident.parcela_unaria().identificador():
                tipo = self.resolve_type(ident.parcela_unaria().identificador())
                return tipo
        except Exception:
            pass
            
        return 'inteiro' # fallback

    def visitCmdAtribuicao(self, ctx:LAParser.CmdAtribuicaoContext):
        is_pointer = ctx.getText().startswith('^')
        ident_str = ctx.identificador().getText()
        if is_pointer:
            ident_str = "*" + ident_str
            
        tipo_la = self.resolve_type(ctx.identificador())
        expr_str = self.visit(ctx.expressao())
        
        if tipo_la == 'literal':
            self.add_line(f"strcpy({ident_str}, {expr_str});")
        else:
            self.add_line(f"{ident_str} = {expr_str};")
        return None

    def visitCmdSe(self, ctx:LAParser.CmdSeContext):
        cond = self.visit(ctx.expressao())
        self.add_line(f"if ({cond}) {{")
        self.indent_level += 1
        
        in_senao = False
        for child in ctx.children:
            if child.getText() == 'senao':
                self.indent_level -= 1
                self.add_line("} else {")
                self.indent_level += 1
                in_senao = True
            elif isinstance(child, LAParser.CmdContext):
                self.visit(child)
                
        self.indent_level -= 1
        self.add_line("}")
        return None

    def visitCmdCaso(self, ctx:LAParser.CmdCasoContext):
        exp = self.visit(ctx.exp_aritmetica())
        self.add_line(f"switch ({exp}) {{")
        self.indent_level += 1
        
        for child in ctx.children:
            if isinstance(child, LAParser.SelecaoContext):
                self.visit(child)
            elif child.getText() == 'senao':
                self.add_line("default:")
                self.indent_level += 1
            elif isinstance(child, LAParser.CmdContext):
                self.visit(child)
                
        # If there was a senao block, we need to decrease indent
        # We can just check if any child was 'senao'
        has_senao = any(c.getText() == 'senao' for c in ctx.children)
        if has_senao:
            self.indent_level -= 1
            
        self.indent_level -= 1
        self.add_line("}")
        return None
        
    def visitSelecao(self, ctx:LAParser.SelecaoContext):
        for item in ctx.item_selecao():
            self.visit(item)
        return None
        
    def visitItem_selecao(self, ctx:LAParser.Item_selecaoContext):
        for intervalo in ctx.constantes().numero_intervalo():
            if intervalo.getText().find('..') != -1:
                # Interval e.g. 1..5
                parts = intervalo.getText().split('..')
                start = int(parts[0])
                end = int(parts[1])
                for i in range(start, end + 1):
                    self.add_line(f"case {i}:")
            else:
                self.add_line(f"case {intervalo.getText()}:")
                
        self.indent_level += 1
        for cmd in ctx.cmd():
            self.visit(cmd)
        self.add_line("break;")
        self.indent_level -= 1
        return None

    def visitCmdPara(self, ctx:LAParser.CmdParaContext):
        nome_var = ctx.IDENT().getText()
        inicio = self.visit(ctx.exp_aritmetica(0))
        fim = self.visit(ctx.exp_aritmetica(1))
        
        self.add_line(f"for ({nome_var} = {inicio}; {nome_var} <= {fim}; {nome_var}++) {{")
        self.indent_level += 1
        for cmd in ctx.cmd():
            self.visit(cmd)
        self.indent_level -= 1
        self.add_line("}")
        return None

    def visitCmdEnquanto(self, ctx:LAParser.CmdEnquantoContext):
        cond = self.visit(ctx.expressao())
        self.add_line(f"while ({cond}) {{")
        self.indent_level += 1
        for cmd in ctx.cmd():
            self.visit(cmd)
        self.indent_level -= 1
        self.add_line("}")
        return None

    def visitCmdFaca(self, ctx:LAParser.CmdFacaContext):
        self.add_line("do {")
        self.indent_level += 1
        for cmd in ctx.cmd():
            self.visit(cmd)
        self.indent_level -= 1
        cond = self.visit(ctx.expressao())
        self.add_line(f"}} while ({cond});")
        return None

    def visitCmdChamada(self, ctx:LAParser.CmdChamadaContext):
        nome = ctx.IDENT().getText()
        args = [self.visit(expr) for expr in ctx.expressao()]
        self.add_line(f"{nome}({', '.join(args)});")
        return None

    def visitCmdRetorne(self, ctx:LAParser.CmdRetorneContext):
        expr = self.visit(ctx.expressao())
        self.add_line(f"return {expr};")
        return None

    # Expressions
    def visitExpressao(self, ctx:LAParser.ExpressaoContext):
        res = self.visit(ctx.termo_logico(0))
        for i, op in enumerate(ctx.op_logico_1()):
            res += f" || {self.visit(ctx.termo_logico(i+1))}"
        return res

    def visitTermo_logico(self, ctx:LAParser.Termo_logicoContext):
        res = self.visit(ctx.fator_logico(0))
        for i, op in enumerate(ctx.op_logico_2()):
            res += f" && {self.visit(ctx.fator_logico(i+1))}"
        return res

    def visitFator_logico(self, ctx:LAParser.Fator_logicoContext):
        res = self.visit(ctx.parcela_logica())
        if ctx.getText().startswith('nao'):
            return f"!({res})"
        return res

    def visitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            return self.visit(ctx.exp_relacional())
        if ctx.getText() == 'verdadeiro':
            return "true"
        return "false"

    def visitExp_relacional(self, ctx:LAParser.Exp_relacionalContext):
        res = self.visit(ctx.exp_aritmetica(0))
        if ctx.op_relacional():
            op = ctx.op_relacional().getText()
            if op == '=': op = '=='
            if op == '<>': op = '!='
            res += f" {op} {self.visit(ctx.exp_aritmetica(1))}"
        return res

    def visitExp_aritmetica(self, ctx:LAParser.Exp_aritmeticaContext):
        res = self.visit(ctx.termo(0))
        for i, op in enumerate(ctx.op1()):
            res += f" {op.getText()} {self.visit(ctx.termo(i+1))}"
        return res

    def visitTermo(self, ctx:LAParser.TermoContext):
        res = self.visit(ctx.fator(0))
        for i, op in enumerate(ctx.op2()):
            res += f" {op.getText()} {self.visit(ctx.fator(i+1))}"
        return res

    def visitFator(self, ctx:LAParser.FatorContext):
        res = self.visit(ctx.parcela(0))
        for i, op in enumerate(ctx.op3()):
            res += f" {op.getText()} {self.visit(ctx.parcela(i+1))}"
        return res

    def visitParcela(self, ctx:LAParser.ParcelaContext):
        if ctx.parcela_unaria():
            return self.visit(ctx.parcela_unaria())
        return self.visit(ctx.parcela_nao_unaria())

    def visitParcela_unaria(self, ctx:LAParser.Parcela_unariaContext):
        if ctx.NUM_INT() or ctx.NUM_REAL():
            sign = ctx.parentCtx.op_unario().getText() if ctx.parentCtx and hasattr(ctx.parentCtx, 'op_unario') and ctx.parentCtx.op_unario() else ""
            return sign + ctx.getText()
            
        if ctx.IDENT():
            args = [self.visit(expr) for expr in ctx.expressao()]
            return f"{ctx.IDENT().getText()}({', '.join(args)})"
            
        if ctx.identificador():
            res = ctx.identificador().getText()
            if ctx.getText().startswith('^'):
                res = "*" + res
            return res
            
        if ctx.expressao():
            return f"({self.visit(ctx.expressao(0))})"
            
        return ctx.getText()

    def visitParcela_nao_unaria(self, ctx:LAParser.Parcela_nao_unariaContext):
        if ctx.CADEIA():
            return ctx.CADEIA().getText()
        if ctx.identificador():
            return "&" + ctx.identificador().getText()
        return ctx.getText()

