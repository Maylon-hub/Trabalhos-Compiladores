import sys
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from LAVisitor import LAVisitor
from SemanticVisitor import SemanticVisitor
from CodeGeneratorVisitor import CodeGeneratorVisitor

class CustomErrorListener:
    def __init__(self, outfile):
        self.outfile = outfile
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if not self.errors:
            text = offendingSymbol.text
            if text == '<EOF>': text = 'EOF'
            self.errors.append(f"Linha {line}: erro sintatico proximo a {text}")

def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo_entrada> <arquivo_saida>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(output_file, 'w', encoding='utf-8') as f:
        # FASE 1: Lexer (Verificação manual simplificada)
        try:
            with open(input_file, 'r', encoding='utf-8') as f_in:
                text = f_in.read()
                lexer = LALexer(InputStream(text))
                
                # Verificações léxicas retrocompatíveis
                for token in lexer.getAllTokens():
                    if token.type == LALexer.CADEIA_NAO_FECHADA:
                        f.write(f"Linha {token.line}: cadeia literal nao fechada\n")
                        f.write("Fim da compilacao\n")
                        return
                    elif token.type == LALexer.COMENTARIO_NAO_FECHADO:
                        f.write(f"Linha {token.line}: comentario nao fechado\n")
                        f.write("Fim da compilacao\n")
                        return
                    elif token.type == LALexer.ERRO:
                        f.write(f"Linha {token.line}: {token.text} - simbolo nao identificado\n")
                        f.write("Fim da compilacao\n")
                        return

        except Exception as e:
            pass

        # FASE 2: Parser (Sintático)
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = LALexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LAParser(stream)
        
        error_listener = CustomErrorListener(f)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        tree = parser.programa()
        
        if error_listener.errors:
            f.write(error_listener.errors[0] + "\n")
            f.write("Fim da compilacao\n")
            return

        # FASE 3: Semântico
        semantic_visitor = SemanticVisitor(f)
        semantic_visitor.visit(tree)
        
        if semantic_visitor.errors:
            semantic_visitor.write_errors()
            return
            
        # FASE 4: Geração de Código
        code_gen = CodeGeneratorVisitor(semantic_visitor.symtable)
        c_code = code_gen.visit(tree)
        f.write(c_code)

if __name__ == '__main__':
    main()
