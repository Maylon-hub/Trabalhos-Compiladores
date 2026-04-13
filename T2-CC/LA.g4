grammar LA;

/* 
   =============================================================================
   REGRAS SINTÁTICAS (PARSER)
   Baseadas na sintaxe da Linguagem Algorítmica (LA)
   =============================================================================
*/

// Regra inicial do programa
programa : declaracoes 'algoritmo' corpo 'fim_algoritmo' EOF ;

// Agrupamento de declarações globais ou locais
declaracoes : decl_local_global* ;

decl_local_global : declaracao_local | declaracao_global ;

// Declarações permitidas em escopo local ou global
declaracao_local : 'declare' variavel
                 | 'constante' IDENT ':' tipo_basico '=' valor_constante
                 | 'tipo' IDENT ':' tipo ;

// Definição de variáveis com lista de identificadores
variavel : identificador (',' identificador)* ':' tipo ;

// Identificadores que podem ser compostos (registros) e possuir dimensões (arrays)
identificador : IDENT ('.' IDENT)* dimensao ;

dimensao : ('[' exp_aritmetica ']')* ;

// Tipagem: Registros ou Tipos Estendidos (ponteiros/identificadores)
tipo : registro | tipo_estendido ;

tipo_basico : 'literal' | 'inteiro' | 'real' | 'logico' ;

tipo_basico_ident : tipo_basico | IDENT ;

tipo_estendido : '^'? tipo_basico_ident ;

valor_constante : CADEIA | NUM_INT | NUM_REAL | 'verdadeiro' | 'falso' ;

// Estrutura de registro
registro : 'registro' variavel* 'fim_registro' ;

// Sub-rotinas: Procedimentos e Funções
declaracao_global : 'procedimento' IDENT '(' parametros? ')' declaracao_local* cmd* 'fim_procedimento'
                  | 'funcao' IDENT '(' parametros? ')' ':' tipo_estendido declaracao_local* cmd* 'fim_funcao' ;

parametro : 'var'? identificador (',' identificador)* ':' tipo_estendido ;

parametros : parametro (',' parametro)* ;

corpo : declaracao_local* cmd* ;

// Blocos de comandos imperativos
cmd : cmdLeia 
    | cmdEscreva 
    | cmdSe 
    | cmdCaso 
    | cmdPara 
    | cmdEnquanto
    | cmdFaca 
    | cmdAtribuicao 
    | cmdChamada 
    | cmdRetorne ;

// Comandos de I/O
cmdLeia : 'leia' '(' '^'? identificador (',' '^'? identificador)* ')' ;

cmdEscreva : 'escreva' '(' expressao (',' expressao)* ')' ;

// Estruturas de controle de fluxo
cmdSe : 'se' expressao 'entao' cmd* ('senao' cmd*)? 'fim_se' ;

cmdCaso : 'caso' exp_aritmetica 'seja' selecao ('senao' cmd*)? 'fim_caso' ;

cmdPara : 'para' IDENT '<-' exp_aritmetica 'ate' exp_aritmetica 'faca' cmd* 'fim_para' ;

cmdEnquanto : 'enquanto' expressao 'faca' cmd* 'fim_enquanto' ;

cmdFaca : 'faca' cmd* 'ate' expressao ;

// Atribuição (aceita ponteiros)
cmdAtribuicao : '^'? identificador '<-' expressao ;

// Chamada de procedimento e retorno de função
cmdChamada : IDENT '(' expressao (',' expressao)* ')' ;

cmdRetorne : 'retorne' expressao ;

// Seleção de casos
selecao : item_selecao* ;

item_selecao : constantes ':' cmd* ;

constantes : numero_intervalo (',' numero_intervalo)* ;

numero_intervalo : op_unario? NUM_INT ('..' op_unario? NUM_INT)? ;

op_unario : '-' ;

/* --- Hierarquia de Expressões --- */

exp_aritmetica : termo (op1 termo)* ;

termo : fator (op2 fator)* ;

fator : parcela (op3 parcela)* ;

op1 : '+' | '-' ;

op2 : '*' | '/' ;

op3 : '%' ;

parcela : op_unario? parcela_unario | parcela_nao_unaria ;

parcela_unaria : '^'? identificador 
               | IDENT '(' expressao (',' expressao)* ')' 
               | NUM_INT 
               | NUM_REAL 
               | '(' expressao ')' ;

parcela_nao_unaria : '&' identificador | CADEIA ;

exp_relacional : exp_aritmetica (op_relacional exp_aritmetica)? ;

op_relacional : '=' | '<>' | '>=' | '<=' | '>' | '<' ;

expressao : termo_logico (op_logico_1 termo_logico)* ;

termo_logico : fator_logico (op_logico_2 fator_logico)* ;

fator_logico : 'nao'? parcela_logica ;

parcela_logica : 'verdadeiro' | 'falso' | exp_relacional ;

op_logico_1 : 'ou' ;

op_logico_2 : 'e' ;


/* 
   =============================================================================
   REGRAS LÉXICAS (LEXER)
   =============================================================================
*/

// Ignorar espaços e quebras de linha
WS : [ \t\r\n]+ -> skip ;

// Comentários: Bloco {} ou Linha /* */ (conforme especificação)
COMENTARIO_BLOCO : '{' ~( '}' )* '}' -> skip ;
COMENTARIO_LINHA : '/*' .*? '*/' -> skip ;

// Tokens básicos
IDENT : [a-zA-Z_] [a-zA-Z0-9_]* ;

NUM_INT : [0-9]+ ;

NUM_REAL : [0-9]+ '.' [0-9]+ ;

CADEIA : '"' ~('"'|'\r'|'\n')* '"' ;

// ----- CAPTURA DE ERROS (Retrocompatibilidade T1) -----
// Estas regras capturam padrões inválidos para que o compilador os reporte de forma customizada
CADEIA_NAO_FECHADA : '"' ~('"'|'\r'|'\n')* ; 
COMENTARIO_NAO_FECHADO : '{' ~'}'* ;
ERRO : . ;
