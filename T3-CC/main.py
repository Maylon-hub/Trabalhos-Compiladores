import sys
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener
from SemanticVisitor import SemanticVisitor

class CustomErrorListener(ErrorListener):
    def __init__(self, outfile):
        super(CustomErrorListener, self).__init__()
        self.outfile = outfile
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self.has_error:
            return
            
        lexema = offendingSymbol.text if offendingSymbol else "EOF"
        if lexema == "<EOF>":
            lexema = "EOF"
            
        self.outfile.write(f"Linha {line}: erro sintatico proximo a {lexema}\n")
        self.outfile.write("Fim da compilacao\n")
        self.has_error = True

def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo_entrada> <arquivo_saida>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return

    with open(output_file, 'w', encoding='utf-8', newline='\n') as outfile:
        lexer = LALexer(input_stream)
        erro_lexico = False
        
        while True:
            t = lexer.nextToken()
            if t.type == Token.EOF:
                break
            
            if t.type == LALexer.ERRO:
                outfile.write(f"Linha {t.line}: {t.text} - simbolo nao identificado\n")
                erro_lexico = True
                break
            elif t.type == LALexer.COMENTARIO_NAO_FECHADO:
                outfile.write(f"Linha {t.line}: comentario nao fechado\n")
                erro_lexico = True
                break
            elif t.type == LALexer.CADEIA_NAO_FECHADA:
                outfile.write(f"Linha {t.line}: cadeia literal nao fechada\n")
                erro_lexico = True
                break
            
        if erro_lexico:
            outfile.write("Fim da compilacao\n")
            return
            
        lexer.reset()
        token_stream = CommonTokenStream(lexer)
        parser = LAParser(token_stream)
        
        parser.removeErrorListeners()
        error_listener = CustomErrorListener(outfile)
        parser.addErrorListener(error_listener)
        
        tree = parser.programa()
        
        if not error_listener.has_error:
            visitor = SemanticVisitor(outfile)
            visitor.visit(tree)
            visitor.write_errors()

if __name__ == '__main__':
    main()
