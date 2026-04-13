import sys
from antlr4 import *
from LALexer import LALexer

input_file = sys.argv[1]
input_stream = FileStream(input_file, encoding='utf-8')
lexer = LALexer(input_stream)
for t in lexer.getAllTokens():
    nome_token = lexer.symbolicNames[t.type] if t.type < len(lexer.symbolicNames) else str(t.type)
    print(f"Line {t.line}:{t.column} [{nome_token}] '{t.text}'")
