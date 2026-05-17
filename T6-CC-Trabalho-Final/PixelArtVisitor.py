# Generated from PixelArt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PixelArtParser import PixelArtParser
else:
    from PixelArtParser import PixelArtParser

# This class defines a complete generic visitor for a parse tree produced by PixelArtParser.

class PixelArtVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PixelArtParser#programa.
    def visitPrograma(self, ctx:PixelArtParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#definicaoCanvas.
    def visitDefinicaoCanvas(self, ctx:PixelArtParser.DefinicaoCanvasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#definicaoPalette.
    def visitDefinicaoPalette(self, ctx:PixelArtParser.DefinicaoPaletteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#definicaoCor.
    def visitDefinicaoCor(self, ctx:PixelArtParser.DefinicaoCorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#definicaoDraw.
    def visitDefinicaoDraw(self, ctx:PixelArtParser.DefinicaoDrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#comando.
    def visitComando(self, ctx:PixelArtParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#cmdPixel.
    def visitCmdPixel(self, ctx:PixelArtParser.CmdPixelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#cmdRect.
    def visitCmdRect(self, ctx:PixelArtParser.CmdRectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#cmdLine.
    def visitCmdLine(self, ctx:PixelArtParser.CmdLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#cmdCircle.
    def visitCmdCircle(self, ctx:PixelArtParser.CmdCircleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PixelArtParser#coordenada.
    def visitCoordenada(self, ctx:PixelArtParser.CoordenadaContext):
        return self.visitChildren(ctx)



del PixelArtParser