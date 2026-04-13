import sys
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener

# Classe customizada para capturar e formatar erros sintáticos
class CustomErrorListener(ErrorListener):
    def __init__(self, outfile):
        super(CustomErrorListener, self).__init__()
        self.outfile = outfile
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Garante que apenas o primeiro erro sintático seja reportado
        if self.has_error:
            return
            
        # O ANTLR usa <EOF> internamente, mas o padrão da disciplina exige EOF
        lexema = offendingSymbol.text if offendingSymbol else "EOF"
        if lexema == "<EOF>":
            lexema = "EOF"
            
        # Formatação exigida pelo professor: Linha X: erro sintatico proximo a <lexema>
        self.outfile.write(f"Linha {line}: erro sintatico proximo a {lexema}\n")
        self.outfile.write("Fim da compilacao\n")
        self.has_error = True

def main():
    # Validação de argumentos de linha de comando
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo_entrada> <arquivo_saida>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Abre o stream de entrada com codificação UTF-8
        input_stream = FileStream(input_file, encoding='utf-8')
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return

    # Abre o arquivo de saída garantindo que as quebras de linha sejam apenas LF (\n)
    # Isso é crítico para a compatibilidade com o corretor automático em ambiente Windows/Linux
    with open(output_file, 'w', encoding='utf-8', newline='\n') as outfile:
        lexer = LALexer(input_stream)
        
        # --- PRIMEIRA PASSADA: Verificação de Erros Léxicos (T1) ---
        erro_lexico = False
        while True:
            t = lexer.nextToken()
            if t.type == Token.EOF:
                break
            
            # Verifica tokens especiais de erro definidos na gramática
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
            
        # --- SEGUNDA PASSADA: Análise Sintática (T2) ---
        # Reinicia o lexer para processar o fluxo desde o início
        lexer.reset()
        token_stream = CommonTokenStream(lexer)
        parser = LAParser(token_stream)
        
        # Remove o listener de erro padrão do ANTLR e adiciona o customizado
        parser.removeErrorListeners()
        error_listener = CustomErrorListener(outfile)
        parser.addErrorListener(error_listener)
        
        # Inicia o parse a partir da regra inicial 'programa'
        parser.programa()

if __name__ == '__main__':
    main()
