from PixelArtVisitor import PixelArtVisitor
from PixelArtParser import PixelArtParser

class SemanticVisitor(PixelArtVisitor):
    def __init__(self):
        self.errors = []
        self.colors = {}
        self.canvas_width = 0
        self.canvas_height = 0

    def visitPrograma(self, ctx: PixelArtParser.ProgramaContext):
        self.visit(ctx.definicaoCanvas())
        self.visit(ctx.definicaoPalette())
        self.visit(ctx.definicaoDraw())

    def visitDefinicaoCanvas(self, ctx: PixelArtParser.DefinicaoCanvasContext):
        self.canvas_width = int(ctx.NUM(0).getText())
        self.canvas_height = int(ctx.NUM(1).getText())
        
        if self.canvas_width <= 0 or self.canvas_height <= 0:
            self.errors.append(f"Linha {ctx.start.line}: canvas deve ter dimensoes maiores que zero")

    def visitDefinicaoPalette(self, ctx: PixelArtParser.DefinicaoPaletteContext):
        for definicao_cor in ctx.definicaoCor():
            self.visit(definicao_cor)

    def visitDefinicaoCor(self, ctx: PixelArtParser.DefinicaoCorContext):
        color_name = ctx.IDENT().getText()
        if color_name in self.colors:
            self.errors.append(f"Linha {ctx.start.line}: cor '{color_name}' ja declarada")
        else:
            self.colors[color_name] = ctx.HEX_COLOR().getText()

    def check_coordinate(self, coord_ctx, line):
        x = int(coord_ctx.NUM(0).getText())
        y = int(coord_ctx.NUM(1).getText())
        
        if x < 0 or x >= self.canvas_width or y < 0 or y >= self.canvas_height:
            self.errors.append(f"Linha {line}: coordenada ({x},{y}) fora dos limites do canvas ({self.canvas_width}x{self.canvas_height})")

    def check_color_exists(self, color_name, line):
        if color_name not in self.colors:
            self.errors.append(f"Linha {line}: cor '{color_name}' nao declarada na palette")

    def visitCmdPixel(self, ctx: PixelArtParser.CmdPixelContext):
        self.check_coordinate(ctx.coordenada(), ctx.start.line)
        self.check_color_exists(ctx.IDENT().getText(), ctx.start.line)

    def visitCmdRect(self, ctx: PixelArtParser.CmdRectContext):
        self.check_coordinate(ctx.coordenada(0), ctx.start.line)
        self.check_coordinate(ctx.coordenada(1), ctx.start.line)
        self.check_color_exists(ctx.IDENT().getText(), ctx.start.line)

    def visitCmdLine(self, ctx: PixelArtParser.CmdLineContext):
        self.check_coordinate(ctx.coordenada(0), ctx.start.line)
        self.check_coordinate(ctx.coordenada(1), ctx.start.line)
        self.check_color_exists(ctx.IDENT().getText(), ctx.start.line)

    def visitCmdCircle(self, ctx: PixelArtParser.CmdCircleContext):
        self.check_coordinate(ctx.coordenada(), ctx.start.line)
        self.check_color_exists(ctx.IDENT().getText(), ctx.start.line)
        
        radius = int(ctx.NUM().getText())
        if radius < 0:
            self.errors.append(f"Linha {ctx.start.line}: raio do circulo nao pode ser negativo")
        else:
            # Check if circle goes out of bounds
            cx = int(ctx.coordenada().NUM(0).getText())
            cy = int(ctx.coordenada().NUM(1).getText())
            
            if cx - radius < 0 or cx + radius >= self.canvas_width or cy - radius < 0 or cy + radius >= self.canvas_height:
                self.errors.append(f"Linha {ctx.start.line}: circulo excede os limites do canvas")
