grammar PixelArt;

// Regras Sintáticas

programa: definicaoCanvas definicaoPalette definicaoDraw EOF ;

definicaoCanvas: 'canvas' NUM 'x' NUM 'background' HEX_COLOR ;

definicaoPalette: 'palette' '{' definicaoCor* '}' ;

definicaoCor: IDENT '=' HEX_COLOR ;

definicaoDraw: 'draw' '{' comando* '}' ;

comando: cmdPixel | cmdRect | cmdLine | cmdCircle ;

cmdPixel: 'pixel' coordenada IDENT ;

cmdRect: 'rect' coordenada 'to' coordenada IDENT ;

cmdLine: 'line' coordenada 'to' coordenada IDENT ;

cmdCircle: 'circle' 'center' coordenada 'radius' NUM IDENT ;

coordenada: '(' NUM ',' NUM ')' ;

// Regras Léxicas

NUM: [0-9]+ ;
IDENT: [a-zA-Z_][a-zA-Z0-9_]* ;
HEX_COLOR: '#' [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
