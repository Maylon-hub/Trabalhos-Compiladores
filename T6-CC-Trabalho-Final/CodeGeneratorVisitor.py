from PixelArtVisitor import PixelArtVisitor
from PixelArtParser import PixelArtParser

class CodeGeneratorVisitor(PixelArtVisitor):
    def __init__(self):
        self.output = []
        self.colors = {}
        self.canvas_width = 0
        self.canvas_height = 0
        self.bg_color = "#FFFFFF"

    def visitPrograma(self, ctx: PixelArtParser.ProgramaContext):
        self.visit(ctx.definicaoCanvas())
        self.visit(ctx.definicaoPalette())
        
        # Start HTML/SVG
        self.output.append("<!DOCTYPE html>")
        self.output.append('<html lang="pt-BR">')
        self.output.append("<head>")
        self.output.append('    <meta charset="UTF-8">')
        self.output.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        self.output.append("    <title>PixelArtDSL Render</title>")
        self.output.append("    <style>")
        self.output.append("        body { background: #1e1e1e; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }")
        self.output.append("        svg { shape-rendering: crispEdges; border: 2px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 80vmin; height: 80vmin; }")
        self.output.append("    </style>")
        self.output.append("</head>")
        self.output.append("<body>")
        self.output.append(f'    <svg viewBox="0 0 {self.canvas_width} {self.canvas_height}" xmlns="http://www.w3.org/2000/svg">')
        self.output.append(f'        <rect width="{self.canvas_width}" height="{self.canvas_height}" fill="{self.bg_color}" />')

        self.visit(ctx.definicaoDraw())

        self.output.append("    </svg>")
        self.output.append("</body>")
        self.output.append("</html>")

        return "\n".join(self.output)

    def visitDefinicaoCanvas(self, ctx: PixelArtParser.DefinicaoCanvasContext):
        self.canvas_width = int(ctx.NUM(0).getText())
        self.canvas_height = int(ctx.NUM(1).getText())
        self.bg_color = ctx.HEX_COLOR().getText()

    def visitDefinicaoPalette(self, ctx: PixelArtParser.DefinicaoPaletteContext):
        for definicao_cor in ctx.definicaoCor():
            self.visit(definicao_cor)

    def visitDefinicaoCor(self, ctx: PixelArtParser.DefinicaoCorContext):
        color_name = ctx.IDENT().getText()
        self.colors[color_name] = ctx.HEX_COLOR().getText()

    def get_color_hex(self, color_name):
        return self.colors.get(color_name, "#000000")

    def visitCmdPixel(self, ctx: PixelArtParser.CmdPixelContext):
        x = int(ctx.coordenada().NUM(0).getText())
        y = int(ctx.coordenada().NUM(1).getText())
        color = self.get_color_hex(ctx.IDENT().getText())
        self.output.append(f'        <rect x="{x}" y="{y}" width="1" height="1" fill="{color}" />')

    def visitCmdRect(self, ctx: PixelArtParser.CmdRectContext):
        x1 = int(ctx.coordenada(0).NUM(0).getText())
        y1 = int(ctx.coordenada(0).NUM(1).getText())
        x2 = int(ctx.coordenada(1).NUM(0).getText())
        y2 = int(ctx.coordenada(1).NUM(1).getText())
        color = self.get_color_hex(ctx.IDENT().getText())
        
        x = min(x1, x2)
        y = min(y1, y2)
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        
        self.output.append(f'        <rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" />')

    def visitCmdLine(self, ctx: PixelArtParser.CmdLineContext):
        x1 = int(ctx.coordenada(0).NUM(0).getText())
        y1 = int(ctx.coordenada(0).NUM(1).getText())
        x2 = int(ctx.coordenada(1).NUM(0).getText())
        y2 = int(ctx.coordenada(1).NUM(1).getText())
        color = self.get_color_hex(ctx.IDENT().getText())
        
        # In SVG, a line stroke needs a width, but since this is pixel art, we can use shape-rendering: crispEdges
        # Note: SVG line stroke is centered. A line from 0,0 to 0,5 with width 1 might bleed. 
        # Using x1+0.5, y1+0.5 helps aligning stroke perfectly to pixel grid.
        self.output.append(f'        <line x1="{x1+0.5}" y1="{y1+0.5}" x2="{x2+0.5}" y2="{y2+0.5}" stroke="{color}" stroke-width="1" stroke-linecap="square"/>')

    def visitCmdCircle(self, ctx: PixelArtParser.CmdCircleContext):
        cx = int(ctx.coordenada().NUM(0).getText())
        cy = int(ctx.coordenada().NUM(1).getText())
        radius = int(ctx.NUM().getText())
        color = self.get_color_hex(ctx.IDENT().getText())
        
        # Center of pixel is cx + 0.5, cy + 0.5
        self.output.append(f'        <circle cx="{cx+0.5}" cy="{cy+0.5}" r="{radius}" fill="{color}" />')
