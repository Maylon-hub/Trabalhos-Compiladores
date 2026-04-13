# Trabalho 2 - Analisador Sintático

## Relatório Técnico

**Grupo:**
- Maylon Martins de Melo - 800199
- Eduardo Eudoro Lemos de Oliveira - 824757

### 1. Introdução
Este trabalho consistiu no desenvolvimento de um analisador sintático para a linguagem LA (Linguagem Algorítmica). O objetivo principal foi evoluir o analisador léxico desenvolvido no Trabalho 1 para um sistema capaz de validar a estrutura gramatical do código-fonte, reportando erros de sintaxe de acordo com as especificações da disciplina.

### 2. Ferramentas Utilizadas
- **Linguagem de Programação:** Python 3.
- **Gerador de Parsers:** ANTLR4 (versão 4.13.2).
- **Ambiente:** VS Code / Terminal Windows.

A escolha pelo Python se deu pela facilidade de manipulação de fluxos de entrada/saída e pela excelente integração com o runtime do ANTLR4.

### 3. Implementação da Gramática
A gramática foi definida no arquivo `LA.g4`, seguindo as produções fornecidas no material de apoio da linguagem LA. As principais decisões de implementação incluíram:
- **Hierarquia de Expressões:** Estruturação das regras de expressões aritméticas e lógicas para garantir a precedência correta de operadores (parênteses, unários, multiplicativos, aditivos, relacionais e lógicos).
- **Comandos e Declarações:** Implementação de regras para declarações de variáveis (locais e globais), tipos customizados, registros e sub-rotinas (procedimentos e funções).
- **Tratamento de Retrocompatibilidade:** Manutenção das regras léxicas do T1 dentro do arquivo da gramática para permitir a captura de erros léxicos (comentários não fechados, cadeias não fechadas e símbolos desconhecidos) antes da análise sintática propriamente dita.

### 4. Tratamento de Erros
O sistema foi projetado para seguir rigorosamente o comportamento esperado pelo corretor automático:
- **Prioridade Léxica:** Antes de iniciar a análise sintática, o programa percorre os tokens gerados pelo Lexer. Se encontrar um erro léxico, a execução é interrompida imediatamente com a mensagem correspondente do T1.
- **Formatação de Erro Sintático:** Foi implementada a classe `CustomErrorListener`, que sobrescreve o método `syntaxError` do ANTLR. Isso permitiu formatar as mensagens exatamente como exigido: `Linha X: erro sintatico proximo a <lexema>`, seguido de `Fim da compilacao`.
- **Estratégia de Parada:** O analisador sintático é configurado para parar no primeiro erro encontrado, evitando a propagação de erros secundários que dificultariam a correção por parte do usuário.

### 5. Instruções de Execução
Para executar o analisador, é necessário ter o Python 3 e o runtime do ANTLR instalado (`pip install antlr4-python3-runtime==4.13.2`).

O comando para execução é:
```bash
python main.py <caminho_entrada> <caminho_saida>
```

Para Windows, foi disponibilizado um script auxiliar `run_t2.bat` para facilitar a integração com o corretor em Java:
```bash
run_t2.bat <entrada.txt> <saida.txt>
```

### 6. Conclusão
O analisador sintático foi validado em 100% dos casos de teste do T2 fornecidos, garantindo que a gramática cobre todas as variantes permitidas pela linguagem LA e que o tratamento de erros atende aos requisitos de formatação e interrupção de fluxo.
