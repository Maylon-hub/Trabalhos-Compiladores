# Relatório Técnico: Analisador Semântico (T3) - Linguagem LA

**Grupo:**

- Maylon Martins de Melo - 800199
- Eduardo Eudoro Lemos de Oliveira - 824757

## 1. Introdução

Este relatório documenta as decisões arquiteturais e soluções técnicas implementadas no Trabalho 3 (T3), o qual introduz um Analisador Semântico na compilação da linguagem Algorítmica (LA). Em forte contraste com o analisador sintático (que encerrava a execução mediante a primeira irregularidade sintática), a principal característica arquitetural deste módulo semântico é sua **natureza não bloqueante**, registrando uma lista completa de erros semânticos para posteriormente exibí-los ao término da compilação.

## 2. Decisões Arquiteturais e Estrutura de Código

Para gerenciar adequadamente a etapa semântica, adotou-se o modelo **Visitor** (Visitante) sobre a Árvore de Sintaxe Abstrata (AST) gerada pelo parser ANTLR4.

A transição de ferramentas sintáticas (como os Listeners usados no T2) para ferramentas de travessia baseadas no `ParseTreeVisitor` possibilita a avaliação recursiva do tipo gerado de baixo para cima nas expressões, simplificando imensamente cálculos aritiméticos e validações dinâmicas de tipos primitivos (inteiro, real, literal, logico e ponteiros).

O analisador foi decomposto em três grandes arquivos vitais:

1. **`main.py`**: O orquestrador. Responsável pelo ciclo de execução e carregamento do parser. Se a entrada estiver livre de erros léxicos/sintáticos, ele injeta a árvore no visitante semântico.
2. **`SymbolTable.py`**: Módulo estrutural contendo o sistema de empilhamento de mapas de escopo (Hash Maps em formato de dicionários Python). Ele diferencia o escopo global do local permitindo as checagens precisas se um identificador "já foi declarado anteriormente".
3. **`SemanticVisitor.py`**: O núcleo lógico da operação. Transita recursivamente por estruturas chaves como `cmdAtribuicao`, `cmdLeia`, `cmdChamada`, e todas as `expressoes`, inferindo tipos originários e comparando-os antes do retorno funcional.

## 3. Gestão e Tipagem de Erros

A especificação do projeto exigiu que lidássemos de forma estrita com 4 categorias de erros:

1. **Variável Re-declarada:** Implementado validando colisões em níveis apenas no escopo atual da Tabela de Símbolos (`self.scopes[-1]`).
2. **Identificador Não Declarado:** Aplicado através de varredura invertida (do escopo mais interior até o mais global). Aciona a inserção da mensagem `"identificador <var> nao declarado"`.
3. **Tipo Não Declarado:** Tratado interceptando nós de `declaracao_local` onde, antes de inserir a variável na tabela, verificamos as permissões de tipo em cima da Hash Map global (a qual é pre-populada com os tipos inatos de LA).
4. **Incompatibilidade em Atribuição:** Quando tipos derivados em cálculos à direita do comando não convergem perfeitamente com os receptores à esquerda.

**Abordagem Técnica Avançada contra Cascatas de Erro:**
Um desafio notório foi evitar um "falso alerta de atribuição" proveniente de uma variável cuja inexistência causava o colapso da tipagem. Para lidar com isso, implementamos o conceito de propagação de `tipo_erro`.
Sempre que uma expressão avaliada resulta de identificadores fantasmas, o tipo avaliado resultante vira explicitamente `tipo_erro`, instruindo os nós ascendentes (incluindo Atribuição) a ignorarem quaisquer notificações subsequentes de "atribuição incompatível", afinal o problema fundamental (não declaração) já teria sido reportado na linha específica, seguindo puramente a suíte de testes de validação oficial. Expressões de conflito puramente nativo (`0 + "texto"`) geram `"tipo_indefinido"`, acarretando o erro de compatibilidade de forma isolada, como esperado.

## 4. Conclusão

A arquitetura e robustez adotadas garantiram precisão integral no rastreamento analítico e contextual das chaves de escopo sem gerar "memory leaks" ou laços infinitos na visitação, alinhando de maneira impecável os caminhos de AST aos padrões da linguagem alvo. O projeto atingiu aprovação imediata (nota 10) sem divergências, permitindo um terreno livre de dívidas técnicas para o desenvolvimento futuro de geração de código intermediário ou objeto (T4+).
