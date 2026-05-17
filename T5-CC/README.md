# Compilador LA - Gerador de Código C (T5)

Este projeto implementa o Gerador de Código C completo para a Linguagem Algorítmica (LA), desenvolvido como parte do Trabalho 5 da disciplina de Compiladores (DC/UFSCar).

## Membros do Grupo

- Maylon Martins de Melo - RA 800199
- Eduardo Eudoro Lemos de Oliveira - RA 824757

## Dependências

- Python 3
- ANTLR4 Python3 Runtime (`antlr4-python3-runtime==4.13.2`)
- Java JRE (para executar a geração do ANTLR4 e o corretor automático)
- GCC Compiler (instalável via MinGW ou Chocolatey `choco install mingw -y` para Windows)

## Instalação

Instale as dependências usando pip:

```bash
pip install -r requirements.txt
```

## Como executar

O script principal de execução é `main.py`, que pode ser chamado diretamente via Python ou usando o script em lote `run_t5.bat`.

### Usando o `run_t5.bat`

```bash
run_t5.bat <arquivo_de_entrada.txt> <arquivo_de_saida.txt>
```

### Execução direta no Python

```bash
python main.py <arquivo_de_entrada.txt> <arquivo_de_saida.txt>
```

## Estrutura do Gerador de Código

O T5 adiciona a geração de código C de alto desempenho após todas as validações léxicas, sintáticas e semânticas das etapas anteriores:

- **`CodeGeneratorVisitor.py`**: O visitor que percorre a árvore sintática válida e traduz todos os comandos para C de forma equivalente.
- **Tabela de Símbolos Leve**: Usada para reter os tipos de variáveis e parâmetros locais durante a tradução de sub-rotinas e comandos de escrita/leitura.
- **Tradução Estruturada**:
  - Variáveis básicas, ponteiros, registros (`struct`) e tipos customizados (`typedef struct`).
  - Blocos condicionais (`if`, `switch` expandido).
  - Laços de repetição (`for`, `while`, `do-while`).
  - Funções (`return` e assinaturas tipadas) e Procedimentos (`void`).
  - Chamadas de I/O estruturadas (`printf` com especificadores inteligentes, `scanf`, `gets`, `strcpy`).
