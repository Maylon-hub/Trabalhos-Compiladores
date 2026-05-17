import sys
from antlr4 import *
from PixelArtLexer import PixelArtLexer
from PixelArtParser import PixelArtParser
from SemanticVisitor import SemanticVisitor
from CodeGeneratorVisitor import CodeGeneratorVisitor
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Linha {line}: erro sintatico proximo a '{offendingSymbol.text if offendingSymbol else 'EOF'}'")

def main(argv):
    if len(argv) < 3:
        print("Uso: python main.py <arquivo_de_entrada> <arquivo_de_saida>")
        sys.exit(1)

    input_file = argv[1]
    output_file = argv[2]

    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        sys.exit(1)

    # Análise Léxica
    lexer = PixelArtLexer(input_stream)
    
    # Vamos fazer uma varredura léxica para erros
    # Diferente do LA, vamos usar o ErrorListener do ANTLR para capturar lexer errors tbm se precisarmos
    lexer.removeErrorListeners()
    error_listener = MyErrorListener()
    lexer.addErrorListener(error_listener)
    
    stream = CommonTokenStream(lexer)

    # Análise Sintática
    parser = PixelArtParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.programa()

    # Se houver erros léxicos/sintáticos, reporta e para
    if error_listener.errors:
        with open(output_file, 'w', encoding='utf-8') as f:
            for err in error_listener.errors:
                f.write(err + '\n')
            f.write("Fim da compilacao\n")
        return

    # Análise Semântica
    semantic_visitor = SemanticVisitor()
    semantic_visitor.visit(tree)

    # Se houver erros semânticos, reporta e para
    if semantic_visitor.errors:
        with open(output_file, 'w', encoding='utf-8') as f:
            for err in semantic_visitor.errors:
                f.write(err + '\n')
            f.write("Fim da compilacao\n")
        return

    # Geração de Código
    code_generator = CodeGeneratorVisitor()
    html_output = code_generator.visit(tree)

    # Gravar a saída
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

if __name__ == '__main__':
    main(sys.argv)
