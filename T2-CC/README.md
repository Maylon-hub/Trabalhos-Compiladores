# T2 - Analisador Sintático (LA)

Este diretório contém a implementação do Analisador Sintático para a linguagem LA, desenvolvida como o Trabalho 2 da disciplina de Construção de Compiladores.

## Estrutura de Arquivos

- `LA.g4`: Definição da gramática (Regras Léxicas e Sintáticas) em formato ANTLR4.
- `main.py`: Ponto de entrada do compilador. Gerencia a leitura de arquivos, execução do Lexer/Parser e formatação de saídas.
- `LALexer.py`, `LAParser.py`, `LAListener.py`: Classes geradas automaticamente pelo ANTLR para Python.
- `requirements.txt`: Dependências do projeto (runtime do ANTLR).
- `run_t2.bat`: Script de conveniência para execução no Windows, compatível com o corretor automático Java.
- `T2-CC-Documentacao-Externa.md`: Relatório técnico sobre a implementação.

## Requisitos

- Python 3.x
- antlr4-python3-runtime==4.13.2

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o analisador:
   ```bash
   python main.py <arquivo_entrada> <arquivo_saida>
   ```

## Implementação Interna

### Tratamento de Erros
A classe `CustomErrorListener` em `main.py` intercepta falhas de reconhecimento do ANTLR e as converte no formato:
`Linha X: erro sintatico proximo a <lexema>`

### Ordem de Análise
1. **Passada Léxica:** Verifica se existem erros do T1 (símbolos inválidos, comentários ou cadeias não fechadas). Se houver, imprime o erro e encerra.
2. **Passada Sintática:** Caso a léxica passe, reinicia o fluxo e executa o Parser para validar a estrutura gramatical.
