# Generated from PixelArt.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,249,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,3,0,50,8,0,1,0,3,0,53,8,
        0,1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,3,0,62,8,0,1,0,1,0,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,79,8,3,10,3,12,3,
        82,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,94,8,5,10,5,12,
        5,97,9,5,1,5,1,5,1,6,1,6,1,6,5,6,104,8,6,10,6,12,6,107,9,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,122,8,7,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,3,9,131,8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,
        139,8,10,1,10,1,10,1,10,1,11,1,11,3,11,146,8,11,1,11,1,11,3,11,150,
        8,11,1,11,1,11,1,11,1,12,1,12,3,12,157,8,12,1,12,1,12,3,12,161,8,
        12,1,12,1,12,3,12,165,8,12,1,12,1,12,1,12,1,13,1,13,3,13,172,8,13,
        1,13,1,13,3,13,176,8,13,1,13,1,13,1,13,3,13,181,8,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,3,15,193,8,15,1,15,1,15,3,
        15,197,8,15,1,15,1,15,1,15,1,16,1,16,3,16,204,8,16,1,16,1,16,3,16,
        208,8,16,1,16,1,16,3,16,212,8,16,1,16,1,16,1,16,1,17,1,17,1,17,1,
        17,1,18,1,18,1,18,1,18,1,18,5,18,226,8,18,10,18,12,18,229,9,18,1,
        19,1,19,1,19,1,19,3,19,235,8,19,1,20,1,20,3,20,239,8,20,1,20,1,20,
        1,20,3,20,244,8,20,1,20,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,0,2,1,0,34,36,1,0,38,39,264,
        0,45,1,0,0,0,2,65,1,0,0,0,4,68,1,0,0,0,6,75,1,0,0,0,8,85,1,0,0,0,
        10,89,1,0,0,0,12,100,1,0,0,0,14,121,1,0,0,0,16,123,1,0,0,0,18,127,
        1,0,0,0,20,135,1,0,0,0,22,143,1,0,0,0,24,154,1,0,0,0,26,169,1,0,
        0,0,28,184,1,0,0,0,30,190,1,0,0,0,32,201,1,0,0,0,34,216,1,0,0,0,
        36,220,1,0,0,0,38,234,1,0,0,0,40,236,1,0,0,0,42,44,3,2,1,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,
        47,45,1,0,0,0,48,50,3,4,2,0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,
        0,0,0,51,53,3,6,3,0,52,51,1,0,0,0,52,53,1,0,0,0,53,57,1,0,0,0,54,
        56,3,10,5,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,
        0,0,58,61,1,0,0,0,59,57,1,0,0,0,60,62,3,12,6,0,61,60,1,0,0,0,61,
        62,1,0,0,0,62,63,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,66,5,1,0,
        0,66,67,5,45,0,0,67,3,1,0,0,0,68,69,5,2,0,0,69,70,5,42,0,0,70,71,
        5,3,0,0,71,72,5,42,0,0,72,73,5,4,0,0,73,74,5,44,0,0,74,5,1,0,0,0,
        75,76,5,5,0,0,76,80,5,6,0,0,77,79,3,8,4,0,78,77,1,0,0,0,79,82,1,
        0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,
        84,5,7,0,0,84,7,1,0,0,0,85,86,5,43,0,0,86,87,5,8,0,0,87,88,5,44,
        0,0,88,9,1,0,0,0,89,90,5,9,0,0,90,91,5,43,0,0,91,95,5,6,0,0,92,94,
        3,14,7,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,
        96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,7,0,0,99,11,1,0,0,0,100,101,
        5,10,0,0,101,105,5,6,0,0,102,104,3,14,7,0,103,102,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,
        1,0,0,0,108,109,5,7,0,0,109,13,1,0,0,0,110,122,3,16,8,0,111,122,
        3,18,9,0,112,122,3,20,10,0,113,122,3,22,11,0,114,122,3,24,12,0,115,
        122,3,26,13,0,116,122,3,28,14,0,117,122,3,30,15,0,118,122,3,32,16,
        0,119,122,3,34,17,0,120,122,3,36,18,0,121,110,1,0,0,0,121,111,1,
        0,0,0,121,112,1,0,0,0,121,113,1,0,0,0,121,114,1,0,0,0,121,115,1,
        0,0,0,121,116,1,0,0,0,121,117,1,0,0,0,121,118,1,0,0,0,121,119,1,
        0,0,0,121,120,1,0,0,0,122,15,1,0,0,0,123,124,5,11,0,0,124,125,3,
        40,20,0,125,126,5,43,0,0,126,17,1,0,0,0,127,128,5,12,0,0,128,130,
        3,40,20,0,129,131,5,13,0,0,130,129,1,0,0,0,130,131,1,0,0,0,131,132,
        1,0,0,0,132,133,3,40,20,0,133,134,5,43,0,0,134,19,1,0,0,0,135,136,
        5,14,0,0,136,138,3,40,20,0,137,139,5,13,0,0,138,137,1,0,0,0,138,
        139,1,0,0,0,139,140,1,0,0,0,140,141,3,40,20,0,141,142,5,43,0,0,142,
        21,1,0,0,0,143,145,5,15,0,0,144,146,5,16,0,0,145,144,1,0,0,0,145,
        146,1,0,0,0,146,147,1,0,0,0,147,149,3,40,20,0,148,150,5,17,0,0,149,
        148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,5,42,0,0,152,
        153,5,43,0,0,153,23,1,0,0,0,154,156,5,18,0,0,155,157,5,16,0,0,156,
        155,1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,160,3,40,20,0,159,
        161,5,19,0,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,
        164,5,42,0,0,163,165,5,20,0,0,164,163,1,0,0,0,164,165,1,0,0,0,165,
        166,1,0,0,0,166,167,5,42,0,0,167,168,5,43,0,0,168,25,1,0,0,0,169,
        171,5,21,0,0,170,172,5,16,0,0,171,170,1,0,0,0,171,172,1,0,0,0,172,
        173,1,0,0,0,173,175,3,40,20,0,174,176,5,17,0,0,175,174,1,0,0,0,175,
        176,1,0,0,0,176,177,1,0,0,0,177,180,5,42,0,0,178,179,5,22,0,0,179,
        181,5,42,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,
        183,5,43,0,0,183,27,1,0,0,0,184,185,5,23,0,0,185,186,3,40,20,0,186,
        187,3,40,20,0,187,188,3,40,20,0,188,189,5,43,0,0,189,29,1,0,0,0,
        190,192,5,24,0,0,191,193,5,16,0,0,192,191,1,0,0,0,192,193,1,0,0,
        0,193,194,1,0,0,0,194,196,3,40,20,0,195,197,5,25,0,0,196,195,1,0,
        0,0,196,197,1,0,0,0,197,198,1,0,0,0,198,199,5,42,0,0,199,200,5,43,
        0,0,200,31,1,0,0,0,201,203,5,26,0,0,202,204,5,16,0,0,203,202,1,0,
        0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,207,3,40,20,0,206,208,5,
        27,0,0,207,206,1,0,0,0,207,208,1,0,0,0,208,209,1,0,0,0,209,211,5,
        42,0,0,210,212,5,28,0,0,211,210,1,0,0,0,211,212,1,0,0,0,212,213,
        1,0,0,0,213,214,5,42,0,0,214,215,5,43,0,0,215,33,1,0,0,0,216,217,
        5,29,0,0,217,218,3,40,20,0,218,219,5,42,0,0,219,35,1,0,0,0,220,221,
        5,30,0,0,221,222,5,43,0,0,222,223,5,31,0,0,223,227,3,40,20,0,224,
        226,3,38,19,0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,
        228,1,0,0,0,228,37,1,0,0,0,229,227,1,0,0,0,230,231,5,32,0,0,231,
        235,5,42,0,0,232,233,5,33,0,0,233,235,7,0,0,0,234,230,1,0,0,0,234,
        232,1,0,0,0,235,39,1,0,0,0,236,238,5,37,0,0,237,239,7,1,0,0,238,
        237,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,42,0,0,241,
        243,5,40,0,0,242,244,7,1,0,0,243,242,1,0,0,0,243,244,1,0,0,0,244,
        245,1,0,0,0,245,246,5,42,0,0,246,247,5,41,0,0,247,41,1,0,0,0,28,
        45,49,52,57,61,80,95,105,121,130,138,145,149,156,160,164,171,175,
        180,192,196,203,207,211,227,234,238,243
    ]

class PixelArtParser ( Parser ):

    grammarFileName = "PixelArt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "'canvas'", "'x'", "'background'", 
                     "'palette'", "'{'", "'}'", "'='", "'shape'", "'draw'", 
                     "'pixel'", "'rect'", "'to'", "'line'", "'circle'", 
                     "'center'", "'radius'", "'ellipse'", "'rx'", "'ry'", 
                     "'star'", "'points'", "'triangle'", "'square'", "'size'", 
                     "'rhombus'", "'width'", "'height'", "'brazilFlag'", 
                     "'drawShape'", "'at'", "'rotate'", "'flip'", "'horizontal'", 
                     "'vertical'", "'both'", "'('", "'-'", "'+'", "','", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "IDENT", "HEX_COLOR", 
                      "STRING", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_definicaoImport = 1
    RULE_definicaoCanvas = 2
    RULE_definicaoPalette = 3
    RULE_definicaoCor = 4
    RULE_definicaoShape = 5
    RULE_definicaoDraw = 6
    RULE_comando = 7
    RULE_cmdPixel = 8
    RULE_cmdRect = 9
    RULE_cmdLine = 10
    RULE_cmdCircle = 11
    RULE_cmdEllipse = 12
    RULE_cmdStar = 13
    RULE_cmdTriangle = 14
    RULE_cmdSquare = 15
    RULE_cmdRhombus = 16
    RULE_cmdBrazilFlag = 17
    RULE_cmdDrawShape = 18
    RULE_shapeModifier = 19
    RULE_coordenada = 20

    ruleNames =  [ "programa", "definicaoImport", "definicaoCanvas", "definicaoPalette", 
                   "definicaoCor", "definicaoShape", "definicaoDraw", "comando", 
                   "cmdPixel", "cmdRect", "cmdLine", "cmdCircle", "cmdEllipse", 
                   "cmdStar", "cmdTriangle", "cmdSquare", "cmdRhombus", 
                   "cmdBrazilFlag", "cmdDrawShape", "shapeModifier", "coordenada" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    NUM=42
    IDENT=43
    HEX_COLOR=44
    STRING=45
    WS=46
    COMMENT=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PixelArtParser.EOF, 0)

        def definicaoImport(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.DefinicaoImportContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.DefinicaoImportContext,i)


        def definicaoCanvas(self):
            return self.getTypedRuleContext(PixelArtParser.DefinicaoCanvasContext,0)


        def definicaoPalette(self):
            return self.getTypedRuleContext(PixelArtParser.DefinicaoPaletteContext,0)


        def definicaoShape(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.DefinicaoShapeContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.DefinicaoShapeContext,i)


        def definicaoDraw(self):
            return self.getTypedRuleContext(PixelArtParser.DefinicaoDrawContext,0)


        def getRuleIndex(self):
            return PixelArtParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = PixelArtParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 42
                self.definicaoImport()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 48
                self.definicaoCanvas()


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 51
                self.definicaoPalette()


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 54
                self.definicaoShape()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 60
                self.definicaoDraw()


            self.state = 63
            self.match(PixelArtParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicaoImportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PixelArtParser.STRING, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_definicaoImport

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicaoImport" ):
                listener.enterDefinicaoImport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicaoImport" ):
                listener.exitDefinicaoImport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicaoImport" ):
                return visitor.visitDefinicaoImport(self)
            else:
                return visitor.visitChildren(self)




    def definicaoImport(self):

        localctx = PixelArtParser.DefinicaoImportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definicaoImport)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PixelArtParser.T__0)
            self.state = 66
            self.match(PixelArtParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicaoCanvasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PixelArtParser.NUM)
            else:
                return self.getToken(PixelArtParser.NUM, i)

        def HEX_COLOR(self):
            return self.getToken(PixelArtParser.HEX_COLOR, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_definicaoCanvas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicaoCanvas" ):
                listener.enterDefinicaoCanvas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicaoCanvas" ):
                listener.exitDefinicaoCanvas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicaoCanvas" ):
                return visitor.visitDefinicaoCanvas(self)
            else:
                return visitor.visitChildren(self)




    def definicaoCanvas(self):

        localctx = PixelArtParser.DefinicaoCanvasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definicaoCanvas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PixelArtParser.T__1)
            self.state = 69
            self.match(PixelArtParser.NUM)
            self.state = 70
            self.match(PixelArtParser.T__2)
            self.state = 71
            self.match(PixelArtParser.NUM)
            self.state = 72
            self.match(PixelArtParser.T__3)
            self.state = 73
            self.match(PixelArtParser.HEX_COLOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicaoPaletteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definicaoCor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.DefinicaoCorContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.DefinicaoCorContext,i)


        def getRuleIndex(self):
            return PixelArtParser.RULE_definicaoPalette

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicaoPalette" ):
                listener.enterDefinicaoPalette(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicaoPalette" ):
                listener.exitDefinicaoPalette(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicaoPalette" ):
                return visitor.visitDefinicaoPalette(self)
            else:
                return visitor.visitChildren(self)




    def definicaoPalette(self):

        localctx = PixelArtParser.DefinicaoPaletteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_definicaoPalette)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PixelArtParser.T__4)
            self.state = 76
            self.match(PixelArtParser.T__5)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 77
                self.definicaoCor()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(PixelArtParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicaoCorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def HEX_COLOR(self):
            return self.getToken(PixelArtParser.HEX_COLOR, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_definicaoCor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicaoCor" ):
                listener.enterDefinicaoCor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicaoCor" ):
                listener.exitDefinicaoCor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicaoCor" ):
                return visitor.visitDefinicaoCor(self)
            else:
                return visitor.visitChildren(self)




    def definicaoCor(self):

        localctx = PixelArtParser.DefinicaoCorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definicaoCor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(PixelArtParser.IDENT)
            self.state = 86
            self.match(PixelArtParser.T__7)
            self.state = 87
            self.match(PixelArtParser.HEX_COLOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicaoShapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.ComandoContext,i)


        def getRuleIndex(self):
            return PixelArtParser.RULE_definicaoShape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicaoShape" ):
                listener.enterDefinicaoShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicaoShape" ):
                listener.exitDefinicaoShape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicaoShape" ):
                return visitor.visitDefinicaoShape(self)
            else:
                return visitor.visitChildren(self)




    def definicaoShape(self):

        localctx = PixelArtParser.DefinicaoShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_definicaoShape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(PixelArtParser.T__8)
            self.state = 90
            self.match(PixelArtParser.IDENT)
            self.state = 91
            self.match(PixelArtParser.T__5)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1705302016) != 0):
                self.state = 92
                self.comando()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(PixelArtParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicaoDrawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.ComandoContext,i)


        def getRuleIndex(self):
            return PixelArtParser.RULE_definicaoDraw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicaoDraw" ):
                listener.enterDefinicaoDraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicaoDraw" ):
                listener.exitDefinicaoDraw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicaoDraw" ):
                return visitor.visitDefinicaoDraw(self)
            else:
                return visitor.visitChildren(self)




    def definicaoDraw(self):

        localctx = PixelArtParser.DefinicaoDrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_definicaoDraw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(PixelArtParser.T__9)
            self.state = 101
            self.match(PixelArtParser.T__5)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1705302016) != 0):
                self.state = 102
                self.comando()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(PixelArtParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdPixel(self):
            return self.getTypedRuleContext(PixelArtParser.CmdPixelContext,0)


        def cmdRect(self):
            return self.getTypedRuleContext(PixelArtParser.CmdRectContext,0)


        def cmdLine(self):
            return self.getTypedRuleContext(PixelArtParser.CmdLineContext,0)


        def cmdCircle(self):
            return self.getTypedRuleContext(PixelArtParser.CmdCircleContext,0)


        def cmdEllipse(self):
            return self.getTypedRuleContext(PixelArtParser.CmdEllipseContext,0)


        def cmdStar(self):
            return self.getTypedRuleContext(PixelArtParser.CmdStarContext,0)


        def cmdTriangle(self):
            return self.getTypedRuleContext(PixelArtParser.CmdTriangleContext,0)


        def cmdSquare(self):
            return self.getTypedRuleContext(PixelArtParser.CmdSquareContext,0)


        def cmdRhombus(self):
            return self.getTypedRuleContext(PixelArtParser.CmdRhombusContext,0)


        def cmdBrazilFlag(self):
            return self.getTypedRuleContext(PixelArtParser.CmdBrazilFlagContext,0)


        def cmdDrawShape(self):
            return self.getTypedRuleContext(PixelArtParser.CmdDrawShapeContext,0)


        def getRuleIndex(self):
            return PixelArtParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = PixelArtParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comando)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.cmdPixel()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.cmdRect()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.cmdLine()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.cmdCircle()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.cmdEllipse()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.cmdStar()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.cmdTriangle()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 8)
                self.state = 117
                self.cmdSquare()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 9)
                self.state = 118
                self.cmdRhombus()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 10)
                self.state = 119
                self.cmdBrazilFlag()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 11)
                self.state = 120
                self.cmdDrawShape()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdPixelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdPixel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdPixel" ):
                listener.enterCmdPixel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdPixel" ):
                listener.exitCmdPixel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdPixel" ):
                return visitor.visitCmdPixel(self)
            else:
                return visitor.visitChildren(self)




    def cmdPixel(self):

        localctx = PixelArtParser.CmdPixelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdPixel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(PixelArtParser.T__10)
            self.state = 124
            self.coordenada()
            self.state = 125
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdRectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.CoordenadaContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,i)


        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdRect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRect" ):
                listener.enterCmdRect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRect" ):
                listener.exitCmdRect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdRect" ):
                return visitor.visitCmdRect(self)
            else:
                return visitor.visitChildren(self)




    def cmdRect(self):

        localctx = PixelArtParser.CmdRectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdRect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(PixelArtParser.T__11)
            self.state = 128
            self.coordenada()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 129
                self.match(PixelArtParser.T__12)


            self.state = 132
            self.coordenada()
            self.state = 133
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.CoordenadaContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,i)


        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdLine" ):
                listener.enterCmdLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdLine" ):
                listener.exitCmdLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdLine" ):
                return visitor.visitCmdLine(self)
            else:
                return visitor.visitChildren(self)




    def cmdLine(self):

        localctx = PixelArtParser.CmdLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(PixelArtParser.T__13)
            self.state = 136
            self.coordenada()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 137
                self.match(PixelArtParser.T__12)


            self.state = 140
            self.coordenada()
            self.state = 141
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdCircleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def NUM(self):
            return self.getToken(PixelArtParser.NUM, 0)

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdCircle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdCircle" ):
                listener.enterCmdCircle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdCircle" ):
                listener.exitCmdCircle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdCircle" ):
                return visitor.visitCmdCircle(self)
            else:
                return visitor.visitChildren(self)




    def cmdCircle(self):

        localctx = PixelArtParser.CmdCircleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdCircle)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(PixelArtParser.T__14)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 144
                self.match(PixelArtParser.T__15)


            self.state = 147
            self.coordenada()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 148
                self.match(PixelArtParser.T__16)


            self.state = 151
            self.match(PixelArtParser.NUM)
            self.state = 152
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdEllipseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PixelArtParser.NUM)
            else:
                return self.getToken(PixelArtParser.NUM, i)

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdEllipse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdEllipse" ):
                listener.enterCmdEllipse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdEllipse" ):
                listener.exitCmdEllipse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdEllipse" ):
                return visitor.visitCmdEllipse(self)
            else:
                return visitor.visitChildren(self)




    def cmdEllipse(self):

        localctx = PixelArtParser.CmdEllipseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cmdEllipse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(PixelArtParser.T__17)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 155
                self.match(PixelArtParser.T__15)


            self.state = 158
            self.coordenada()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 159
                self.match(PixelArtParser.T__18)


            self.state = 162
            self.match(PixelArtParser.NUM)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 163
                self.match(PixelArtParser.T__19)


            self.state = 166
            self.match(PixelArtParser.NUM)
            self.state = 167
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdStarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PixelArtParser.NUM)
            else:
                return self.getToken(PixelArtParser.NUM, i)

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdStar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdStar" ):
                listener.enterCmdStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdStar" ):
                listener.exitCmdStar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdStar" ):
                return visitor.visitCmdStar(self)
            else:
                return visitor.visitChildren(self)




    def cmdStar(self):

        localctx = PixelArtParser.CmdStarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cmdStar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(PixelArtParser.T__20)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 170
                self.match(PixelArtParser.T__15)


            self.state = 173
            self.coordenada()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 174
                self.match(PixelArtParser.T__16)


            self.state = 177
            self.match(PixelArtParser.NUM)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 178
                self.match(PixelArtParser.T__21)
                self.state = 179
                self.match(PixelArtParser.NUM)


            self.state = 182
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdTriangleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.CoordenadaContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,i)


        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdTriangle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdTriangle" ):
                listener.enterCmdTriangle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdTriangle" ):
                listener.exitCmdTriangle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdTriangle" ):
                return visitor.visitCmdTriangle(self)
            else:
                return visitor.visitChildren(self)




    def cmdTriangle(self):

        localctx = PixelArtParser.CmdTriangleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cmdTriangle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(PixelArtParser.T__22)
            self.state = 185
            self.coordenada()
            self.state = 186
            self.coordenada()
            self.state = 187
            self.coordenada()
            self.state = 188
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdSquareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def NUM(self):
            return self.getToken(PixelArtParser.NUM, 0)

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdSquare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdSquare" ):
                listener.enterCmdSquare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdSquare" ):
                listener.exitCmdSquare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdSquare" ):
                return visitor.visitCmdSquare(self)
            else:
                return visitor.visitChildren(self)




    def cmdSquare(self):

        localctx = PixelArtParser.CmdSquareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cmdSquare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(PixelArtParser.T__23)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 191
                self.match(PixelArtParser.T__15)


            self.state = 194
            self.coordenada()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 195
                self.match(PixelArtParser.T__24)


            self.state = 198
            self.match(PixelArtParser.NUM)
            self.state = 199
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdRhombusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PixelArtParser.NUM)
            else:
                return self.getToken(PixelArtParser.NUM, i)

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdRhombus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRhombus" ):
                listener.enterCmdRhombus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRhombus" ):
                listener.exitCmdRhombus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdRhombus" ):
                return visitor.visitCmdRhombus(self)
            else:
                return visitor.visitChildren(self)




    def cmdRhombus(self):

        localctx = PixelArtParser.CmdRhombusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cmdRhombus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(PixelArtParser.T__25)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 202
                self.match(PixelArtParser.T__15)


            self.state = 205
            self.coordenada()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 206
                self.match(PixelArtParser.T__26)


            self.state = 209
            self.match(PixelArtParser.NUM)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 210
                self.match(PixelArtParser.T__27)


            self.state = 213
            self.match(PixelArtParser.NUM)
            self.state = 214
            self.match(PixelArtParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdBrazilFlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def NUM(self):
            return self.getToken(PixelArtParser.NUM, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdBrazilFlag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdBrazilFlag" ):
                listener.enterCmdBrazilFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdBrazilFlag" ):
                listener.exitCmdBrazilFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdBrazilFlag" ):
                return visitor.visitCmdBrazilFlag(self)
            else:
                return visitor.visitChildren(self)




    def cmdBrazilFlag(self):

        localctx = PixelArtParser.CmdBrazilFlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cmdBrazilFlag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(PixelArtParser.T__28)
            self.state = 217
            self.coordenada()
            self.state = 218
            self.match(PixelArtParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdDrawShapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(PixelArtParser.IDENT, 0)

        def coordenada(self):
            return self.getTypedRuleContext(PixelArtParser.CoordenadaContext,0)


        def shapeModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PixelArtParser.ShapeModifierContext)
            else:
                return self.getTypedRuleContext(PixelArtParser.ShapeModifierContext,i)


        def getRuleIndex(self):
            return PixelArtParser.RULE_cmdDrawShape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdDrawShape" ):
                listener.enterCmdDrawShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdDrawShape" ):
                listener.exitCmdDrawShape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdDrawShape" ):
                return visitor.visitCmdDrawShape(self)
            else:
                return visitor.visitChildren(self)




    def cmdDrawShape(self):

        localctx = PixelArtParser.CmdDrawShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cmdDrawShape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(PixelArtParser.T__29)
            self.state = 221
            self.match(PixelArtParser.IDENT)
            self.state = 222
            self.match(PixelArtParser.T__30)
            self.state = 223
            self.coordenada()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 224
                self.shapeModifier()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(PixelArtParser.NUM, 0)

        def getRuleIndex(self):
            return PixelArtParser.RULE_shapeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeModifier" ):
                listener.enterShapeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeModifier" ):
                listener.exitShapeModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShapeModifier" ):
                return visitor.visitShapeModifier(self)
            else:
                return visitor.visitChildren(self)




    def shapeModifier(self):

        localctx = PixelArtParser.ShapeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_shapeModifier)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(PixelArtParser.T__31)
                self.state = 231
                self.match(PixelArtParser.NUM)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(PixelArtParser.T__32)
                self.state = 233
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordenadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(PixelArtParser.NUM)
            else:
                return self.getToken(PixelArtParser.NUM, i)

        def getRuleIndex(self):
            return PixelArtParser.RULE_coordenada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordenada" ):
                listener.enterCoordenada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordenada" ):
                listener.exitCoordenada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordenada" ):
                return visitor.visitCoordenada(self)
            else:
                return visitor.visitChildren(self)




    def coordenada(self):

        localctx = PixelArtParser.CoordenadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_coordenada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(PixelArtParser.T__36)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==39:
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 240
            self.match(PixelArtParser.NUM)
            self.state = 241
            self.match(PixelArtParser.T__39)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==39:
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 245
            self.match(PixelArtParser.NUM)
            self.state = 246
            self.match(PixelArtParser.T__40)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





