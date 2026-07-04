grammar PixelArt;

// Regras Sintáticas

programa: definicaoImport* definicaoCanvas? definicaoPalette? definicaoShape* definicaoDraw? EOF ;

definicaoImport: 'import' STRING ;

definicaoCanvas: 'canvas' NUM 'x' NUM 'background' HEX_COLOR ;

definicaoPalette: 'palette' '{' definicaoCor* '}' ;

definicaoCor: IDENT '=' HEX_COLOR ;

definicaoShape: 'shape' IDENT '{' comando* '}' ;

definicaoDraw: 'draw' '{' comando* '}' ;

comando: cmdPixel
       | cmdRect
       | cmdLine
       | cmdCircle
       | cmdEllipse
       | cmdStar
       | cmdTriangle
       | cmdSquare
       | cmdRhombus
       | cmdBrazilFlag
       | cmdDrawShape
       ;

cmdPixel: 'pixel' coordenada IDENT ;

cmdRect: 'rect' coordenada ('to')? coordenada IDENT ;

cmdLine: 'line' coordenada ('to')? coordenada IDENT ;

cmdCircle: 'circle' ('center')? coordenada ('radius')? NUM IDENT ;

cmdEllipse: 'ellipse' ('center')? coordenada ('rx')? NUM ('ry')? NUM IDENT ;

cmdStar: 'star' ('center')? coordenada ('radius')? NUM ('points' NUM)? IDENT ;

cmdTriangle: 'triangle' coordenada coordenada coordenada IDENT ;

cmdSquare: 'square' ('center')? coordenada ('size')? NUM IDENT ;

cmdRhombus: 'rhombus' ('center')? coordenada ('width')? NUM ('height')? NUM IDENT ;

cmdBrazilFlag: 'brazilFlag' coordenada NUM ;

cmdDrawShape: 'drawShape' IDENT 'at' coordenada shapeModifier* ;

shapeModifier: 'rotate' NUM
             | 'flip' ('horizontal' | 'vertical' | 'both')
             ;

coordenada: '(' ( '-' | '+' )? NUM ',' ( '-' | '+' )? NUM ')' ;

// Regras Léxicas

NUM: [0-9]+ ;
IDENT: [a-zA-Z_][a-zA-Z0-9_]* ;
HEX_COLOR: '#' [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] ;
STRING: '"' ~[\r\n"]* '"' ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
