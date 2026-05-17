# Relatório Técnico: Gerador de Código C (T5) - Linguagem LA

## Membros do Grupo

- Maylon Martins de Melo - RA 800199
- Eduardo Eudoro Lemos de Oliveira - RA 824757

## 1. Introdução

Este relatório documenta a arquitetura e a implementação da fase final (T5) do compilador da Linguagem Algorítmica (LA). Nesta etapa, desenvolvemos o **Gerador de Código C** (`CodeGeneratorVisitor.py`), responsável por traduzir os nós validados da Árvore de Sintaxe Abstrata (AST) para um código fonte C compilável e semanticamente idêntico. 

O compilador opera em fases integradas: primeiro valida a estrutura léxica, depois a sintática, em seguida a semântica (reportando erros de tipos, escopos e assinaturas) e, se não houver erros semânticos, prossegue para a geração de código.

## 2. Decisões Arquiteturais e Mapeamentos

O gerador foi implementado através do padrão de projeto Visitor (`CodeGeneratorVisitor.py`), que percorre a árvore gerada pelo ANTLR e mapeia as estruturas para sua sintaxe correspondente em C:

1. **Mapeamento de Tipos**:
   - `inteiro` -> `int`
   - `real` -> `float`
   - `literal` -> `char name[80]` (strings com limite padrão)
   - `logico` -> `int` (usado com macros booleanas implícitas)
   - Ponteiros (`^inteiro`) -> `int*`

2. **Estruturas complexas (Registros e Structs)**:
   - Registros declarados em variáveis são convertidos em blocos `struct { ... } nome;`.
   - Registros declarados como tipos customizados (`tipo tX : registro ...`) são traduzidos usando `typedef struct { ... } tX;`.

3. **Controle de Escopo de Geração**:
   - Re-implementamos uma tabela de símbolos leve (`SymbolTable.py`) no próprio Visitor para reter informações cruciais sobre os tipos de variáveis e parâmetros locais em escopos aninhados (durante visitas de funções/procedimentos). Isso garante que o especificador do `printf` (ex: `%d`, `%s`, `%f`) e comandos de atribuição de string (`strcpy`) sejam resolvidos com precisão cirúrgica de acordo com o escopo ativo.

4. **Tradução de Comandos de I/O**:
   - `escreva(...)`: Mapeado para múltiplos comandos `printf` em C, derivando dinamicamente os especificadores de formato a partir do tipo semântico da expressão.
   - `leia(...)`: Mapeado para `scanf` (usando `&` para variáveis padrão) ou `gets` (para ler cadeias de caracteres completas).

5. **Instruções de Controle de Fluxo**:
   - `se` / `senao`: Convertidos diretamente para blocos estruturados `if` / `else`.
   - `caso` / `seja`: Convertidos para blocos `switch` em C. A expansão de intervalos de constantes (`1..5`) é traduzida dinamicamente em casos múltiplos sequenciais (`case 1: case 2: ...`).
   - `para`: Convertido para a estrutura clássica `for (i = inicio; i <= fim; i++)`.
   - `enquanto`: Traduzido para loops `while (...)`.
   - `faca ... ate`: Traduzido para blocos `do { ... } while (...);`.

## 3. Resultados Obtidos

Após a instalação do compilador `gcc` (através do Chocolatey) no ambiente de desenvolvimento local, rodamos a suíte inteira contendo 20 casos de teste complexos.

O compilador C executou sem erros em todos os cenários gerados pelo corretor oficial, atingindo a seguinte pontuação:

```bash
Nota do grupo "800199, 824757":
CT 5 = 10.0 (20/20)
```

O projeto do compilador LA está agora 100% funcional em todas as fases, desde a análise léxica (T1) até a geração final de código executável em C (T5).
