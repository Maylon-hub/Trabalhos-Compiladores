# Compilador LA - Analisador Semântico Avançado (T4)

Este projeto implementa o Analisador Semântico Avançado para a Linguagem Algorítmica (LA), desenvolvido como parte do Trabalho 4 da disciplina de Compiladores (DC/UFSCar).

## Membros do Grupo

- Maylon Martins de Melo - RA 800199
- Eduardo Eudoro Lemos de Oliveira - RA 824757

## Dependências

- Python 3
- ANTLR4 Python3 Runtime (`antlr4-python3-runtime==4.13.2`)
- Java JRE (para executar a geração do ANTLR4 e o corretor automático)

## Instalação

Instale as dependências usando pip:

```bash
pip install -r requirements.txt
```

## Como executar

O script principal de execução é `main.py`, que pode ser chamado diretamente via Python ou usando o script em lote `run_t4.bat`.

### Usando o `run_t4.bat`

```bash
run_t4.bat <arquivo_de_entrada.txt> <arquivo_de_saida.txt>
```

### Execução direta no Python

```bash
python main.py <arquivo_de_entrada.txt> <arquivo_de_saida.txt>
```

## Estrutura do Analisador

Diferentemente do T3, o T4 adiciona análises contextuais e checagem de tipos profundas sobre elementos complexos da linguagem LA:

- **Registros (Structs)**: Mapeamento de sub-escopos contendo as propriedades e tipos das variáveis internas do registro. Suporte à resolução dinâmica recursiva de expressões de acesso como `ponto1.x`.
- **Arrays**: Varredura semântica para indexação de expressões dentro dos colchetes, resolvendo o tipo base para atribuições do tipo `valor[0]`.
- **Funções e Procedimentos**: O `SemanticVisitor` armazena a lista ordenada e os tipos específicos dos parâmetros formais e o tipo de retorno. Toda chamada exige a compatibilidade estrita da assinatura do método (`check_function_call`).
- **Validação de Retorno**: Verifica semanticamente o escopo no qual a palavra-chave `retorne` é utilizada, acusando erro fora de contextos de função.
- **Ponteiros**: Implementação dos operadores de endereço (`&`) e desreferenciamento (`^`), garantindo as regras rígidas de tipagem dos endereços.
- **`SymbolTable.py`**: Suporta o rastreamento avançado de tipos customizados, assinatura de sub-rotinas e registros.
- **`SemanticVisitor.py`**: Ponto central da lógica não bloqueante, acumulando e relatando múltiplos erros semânticos até o fim da execução.
