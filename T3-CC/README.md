# Compilador LA - Analisador Semântico (T3)

Este projeto implementa o Analisador Semântico para a Linguagem Algorítmica (LA), desenvolvido como parte do Trabalho 3 da disciplina de Compiladores (DC/UFSCar).

## Dependências

- Python 3
- ANTLR4 Python3 Runtime (`antlr4-python3-runtime==4.13.2`)
- Java JRE (para executar a geração inicial do ANTLR4, caso necessário)

## Instalação

Instale as dependências usando pip:

```bash
pip install -r requirements.txt
```

## Como executar

O script principal de execução é `main.py`, que pode ser chamado diretamente via Python ou usando o script em lote `run_t3.bat` para compatibilidade com o corretor automático em Java.

### Usando o `run_t3.bat` (Recomendado para o Corretor Automático)

```bash
run_t3.bat <arquivo_de_entrada.txt> <arquivo_de_saida.txt>
```

### Execução direta no Python

```bash
python main.py <arquivo_de_entrada.txt> <arquivo_de_saida.txt>
```

## Estrutura do Analisador

Diferentemente do T2 (Analisador Sintático), o T3 não interrompe a análise no primeiro erro. O analisador processa a árvore sintática gerada pelo ANTLR4 (AST) por completo e acumula todos os erros semânticos encontrados antes de finalizar a execução.

A implementação é baseada no padrão **Visitor**, estendendo a classe `LAVisitor` gerada automaticamente.

- **`main.py`**: Ponto de entrada. Gerencia as fases de compilação.
  - Verifica erros léxicos e sintáticos primeiro.
  - Se não houver erros na árvore, instancia o `SemanticVisitor` para avaliar a semântica do programa.
- **`SemanticVisitor.py`**: Contém as lógicas de travessia na AST. Ele checa as regras semânticas de:
  - Tipos não declarados.
  - Variáveis não declaradas (identificador não declarado).
  - Variáveis re-declaradas no mesmo escopo.
  - Atribuições não compatíveis (ex: atribuir um literal para uma variável inteira).
- **`SymbolTable.py`**: Estrutura de dados para a Tabela de Símbolos. Lida com:
  - Diferentes níveis de escopo (funções e global).
  - Armazenamento dos tipos semânticos (`inteiro`, `real`, `literal`, `logico`, bem como ponteiros).
- **`LA.g4`**: Arquivo de gramática atualizado.

## Tipos e Compatibilidade

A tabela de símbolos inicial é populada com os tipos básicos da linguagem LA. As regras de conversão suportadas implicitamente em expressões e atribuições são:
- Atribuição de inteiros para variáveis do tipo real.
- Ponteiros exigem verificação precisa do tipo base associado.

Durante a análise, se uma expressão contiver variáveis não declaradas, o tipo gerado é classificado internamente como `"tipo_erro"`, impedindo avisos repetitivos de "atribuição incompatível" para o mesmo erro. Já expressões com operandos nativamente incompatíveis retornam `"tipo_indefinido"`, resultando no erro padrão da linguagem.
