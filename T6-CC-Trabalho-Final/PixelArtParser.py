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
        4,1,23,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,9,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,4,
        1,4,1,5,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,
        0,87,0,22,1,0,0,0,2,27,1,0,0,0,4,34,1,0,0,0,6,44,1,0,0,0,8,48,1,
        0,0,0,10,62,1,0,0,0,12,64,1,0,0,0,14,68,1,0,0,0,16,74,1,0,0,0,18,
        80,1,0,0,0,20,87,1,0,0,0,22,23,3,2,1,0,23,24,3,4,2,0,24,25,3,8,4,
        0,25,26,5,0,0,1,26,1,1,0,0,0,27,28,5,1,0,0,28,29,5,19,0,0,29,30,
        5,2,0,0,30,31,5,19,0,0,31,32,5,3,0,0,32,33,5,21,0,0,33,3,1,0,0,0,
        34,35,5,4,0,0,35,39,5,5,0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,41,1,
        0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,
        43,5,6,0,0,43,5,1,0,0,0,44,45,5,20,0,0,45,46,5,7,0,0,46,47,5,21,
        0,0,47,7,1,0,0,0,48,49,5,8,0,0,49,53,5,5,0,0,50,52,3,10,5,0,51,50,
        1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,
        55,53,1,0,0,0,56,57,5,6,0,0,57,9,1,0,0,0,58,63,3,12,6,0,59,63,3,
        14,7,0,60,63,3,16,8,0,61,63,3,18,9,0,62,58,1,0,0,0,62,59,1,0,0,0,
        62,60,1,0,0,0,62,61,1,0,0,0,63,11,1,0,0,0,64,65,5,9,0,0,65,66,3,
        20,10,0,66,67,5,20,0,0,67,13,1,0,0,0,68,69,5,10,0,0,69,70,3,20,10,
        0,70,71,5,11,0,0,71,72,3,20,10,0,72,73,5,20,0,0,73,15,1,0,0,0,74,
        75,5,12,0,0,75,76,3,20,10,0,76,77,5,11,0,0,77,78,3,20,10,0,78,79,
        5,20,0,0,79,17,1,0,0,0,80,81,5,13,0,0,81,82,5,14,0,0,82,83,3,20,
        10,0,83,84,5,15,0,0,84,85,5,19,0,0,85,86,5,20,0,0,86,19,1,0,0,0,
        87,88,5,16,0,0,88,89,5,19,0,0,89,90,5,17,0,0,90,91,5,19,0,0,91,92,
        5,18,0,0,92,21,1,0,0,0,3,39,53,62
    ]

class PixelArtParser ( Parser ):

    grammarFileName = "PixelArt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'canvas'", "'x'", "'background'", "'palette'", 
                     "'{'", "'}'", "'='", "'draw'", "'pixel'", "'rect'", 
                     "'to'", "'line'", "'circle'", "'center'", "'radius'", 
                     "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "IDENT", 
                      "HEX_COLOR", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_definicaoCanvas = 1
    RULE_definicaoPalette = 2
    RULE_definicaoCor = 3
    RULE_definicaoDraw = 4
    RULE_comando = 5
    RULE_cmdPixel = 6
    RULE_cmdRect = 7
    RULE_cmdLine = 8
    RULE_cmdCircle = 9
    RULE_coordenada = 10

    ruleNames =  [ "programa", "definicaoCanvas", "definicaoPalette", "definicaoCor", 
                   "definicaoDraw", "comando", "cmdPixel", "cmdRect", "cmdLine", 
                   "cmdCircle", "coordenada" ]

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
    NUM=19
    IDENT=20
    HEX_COLOR=21
    WS=22
    COMMENT=23

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

        def definicaoCanvas(self):
            return self.getTypedRuleContext(PixelArtParser.DefinicaoCanvasContext,0)


        def definicaoPalette(self):
            return self.getTypedRuleContext(PixelArtParser.DefinicaoPaletteContext,0)


        def definicaoDraw(self):
            return self.getTypedRuleContext(PixelArtParser.DefinicaoDrawContext,0)


        def EOF(self):
            return self.getToken(PixelArtParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.definicaoCanvas()
            self.state = 23
            self.definicaoPalette()
            self.state = 24
            self.definicaoDraw()
            self.state = 25
            self.match(PixelArtParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_definicaoCanvas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(PixelArtParser.T__0)
            self.state = 28
            self.match(PixelArtParser.NUM)
            self.state = 29
            self.match(PixelArtParser.T__1)
            self.state = 30
            self.match(PixelArtParser.NUM)
            self.state = 31
            self.match(PixelArtParser.T__2)
            self.state = 32
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
        self.enterRule(localctx, 4, self.RULE_definicaoPalette)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PixelArtParser.T__3)
            self.state = 35
            self.match(PixelArtParser.T__4)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 36
                self.definicaoCor()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(PixelArtParser.T__5)
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
        self.enterRule(localctx, 6, self.RULE_definicaoCor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(PixelArtParser.IDENT)
            self.state = 45
            self.match(PixelArtParser.T__6)
            self.state = 46
            self.match(PixelArtParser.HEX_COLOR)
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
        self.enterRule(localctx, 8, self.RULE_definicaoDraw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PixelArtParser.T__7)
            self.state = 49
            self.match(PixelArtParser.T__4)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13824) != 0):
                self.state = 50
                self.comando()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(PixelArtParser.T__5)
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
        self.enterRule(localctx, 10, self.RULE_comando)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.cmdPixel()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.cmdRect()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.cmdLine()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.cmdCircle()
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
        self.enterRule(localctx, 12, self.RULE_cmdPixel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(PixelArtParser.T__8)
            self.state = 65
            self.coordenada()
            self.state = 66
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
        self.enterRule(localctx, 14, self.RULE_cmdRect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PixelArtParser.T__9)
            self.state = 69
            self.coordenada()
            self.state = 70
            self.match(PixelArtParser.T__10)
            self.state = 71
            self.coordenada()
            self.state = 72
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
        self.enterRule(localctx, 16, self.RULE_cmdLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PixelArtParser.T__11)
            self.state = 75
            self.coordenada()
            self.state = 76
            self.match(PixelArtParser.T__10)
            self.state = 77
            self.coordenada()
            self.state = 78
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
        self.enterRule(localctx, 18, self.RULE_cmdCircle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(PixelArtParser.T__12)
            self.state = 81
            self.match(PixelArtParser.T__13)
            self.state = 82
            self.coordenada()
            self.state = 83
            self.match(PixelArtParser.T__14)
            self.state = 84
            self.match(PixelArtParser.NUM)
            self.state = 85
            self.match(PixelArtParser.IDENT)
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
        self.enterRule(localctx, 20, self.RULE_coordenada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(PixelArtParser.T__15)
            self.state = 88
            self.match(PixelArtParser.NUM)
            self.state = 89
            self.match(PixelArtParser.T__16)
            self.state = 90
            self.match(PixelArtParser.NUM)
            self.state = 91
            self.match(PixelArtParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





