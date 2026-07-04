import os
import math
from antlr4 import FileStream, CommonTokenStream
from PixelArtVisitor import PixelArtVisitor
from PixelArtParser import PixelArtParser
from PixelArtLexer import PixelArtLexer

class CodeGeneratorVisitor(PixelArtVisitor):
    def __init__(self, base_dir=""):
        super(CodeGeneratorVisitor, self).__init__()
        self.base_dir = base_dir
        self.output = []
        self.colors = {}
        self.shapes = {}  # shape_name -> shape_ctx
        self.canvas_width = 0
        self.canvas_height = 0
        self.bg_color = "#FFFFFF"
        self.imported_files = set()
        self.warnings = []

    def parse_coordenada(self, coord_ctx):
        tokens = [coord_ctx.getChild(i).getText() for i in range(coord_ctx.getChildCount())]
        comma_idx = tokens.index(',')
        x = int("".join(tokens[1:comma_idx]))
        y = int("".join(tokens[comma_idx+1:-1]))
        return x, y

    def get_color_hex(self, color_name):
        return self.colors.get(color_name, "#000000")

    def visitPrograma(self, ctx: PixelArtParser.ProgramaContext):
        # 1. Process imports first
        for imp in ctx.definicaoImport():
            self.visit(imp)

        # 2. Process canvas
        if ctx.definicaoCanvas():
            self.visit(ctx.definicaoCanvas())

        # 3. Process palette
        if ctx.definicaoPalette():
            self.visit(ctx.definicaoPalette())

        # 4. Register local shapes
        for shape in ctx.definicaoShape():
            self.visit(shape)

        # Start HTML/SVG GCI output
        self.output.append("<!DOCTYPE html>")
        self.output.append('<html lang="pt-BR">')
        self.output.append("<head>")
        self.output.append('    <meta charset="UTF-8">')
        self.output.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        self.output.append("    <title>PixelArtDSL Render</title>")
        self.output.append("    <style>")
        self.output.append("        body { background: #121214; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: system-ui, -apple-system, sans-serif; }")
        self.output.append("        svg { shape-rendering: crispEdges; border: 4px solid #1f1f23; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.6); width: 80vmin; height: 80vmin; background-color: #1e1e1e; }")
        self.output.append("    </style>")
        self.output.append("</head>")
        self.output.append("<body>")
        self.output.append(f'    <svg viewBox="0 0 {self.canvas_width} {self.canvas_height}" xmlns="http://www.w3.org/2000/svg">')
        self.output.append(f'        <rect width="{self.canvas_width}" height="{self.canvas_height}" fill="{self.bg_color}" />')

        # 5. Process draw
        if ctx.definicaoDraw():
            self.visit(ctx.definicaoDraw())

        self.output.append("    </svg>")

        # Inject Warning Banner if there are out-of-bounds warnings
        if self.warnings:
            self.output.append('    <div id="warning-banner" style="position: fixed; top: 20px; right: 20px; background: rgba(255, 179, 0, 0.95); color: #121214; padding: 16px 24px; border-radius: 12px; font-size: 14px; font-weight: 600; box-shadow: 0 10px 25px rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); z-index: 10000; max-width: 350px; display: flex; flex-direction: column; gap: 8px; transition: all 0.3s ease; height: fit-content; align-self: flex-start;">')
            self.output.append('        <div style="display: flex; align-items: center; gap: 8px;">')
            self.output.append('            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>')
            self.output.append('            <span>Aviso de Limites</span>')
            self.output.append('        </div>')
            self.output.append('        <div style="font-weight: 400; font-size: 13px; opacity: 0.9; line-height: 1.4;">')
            self.output.append('            Alguns elementos do desenho excedem os limites do canvas. Você pode mover/deslocar a coordenada do elemento se quiser que ele apareça completamente na tela.')
            self.output.append('        </div>')
            self.output.append('        <button onclick="document.getElementById(\'warning-banner\').style.display=\'none\'" style="align-self: flex-end; background: none; border: 1px solid #121214; padding: 4px 10px; border-radius: 6px; cursor: pointer; font-size: 11px; font-weight: 700; color: #121214;">Entendido</button>')
            self.output.append('    </div>')

        self.output.append("</body>")
        self.output.append("</html>")

        return "\n".join(self.output)

    def visitDefinicaoImport(self, ctx: PixelArtParser.DefinicaoImportContext):
        import_path_str = ctx.STRING().getText().strip('"')
        full_path = os.path.normpath(os.path.join(self.base_dir, import_path_str))

        if full_path in self.imported_files:
            return

        self.imported_files.add(full_path)

        if not os.path.exists(full_path):
            return  # Handled by semantic visitor

        try:
            input_stream = FileStream(full_path, encoding='utf-8')
            lexer = PixelArtLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = PixelArtParser(stream)
            tree = parser.programa()

            # Gather imports recursively
            for imp in tree.definicaoImport():
                self.visit(imp)

            # Gather colors
            if tree.definicaoPalette():
                for definicao_cor in tree.definicaoPalette().definicaoCor():
                    color_name = definicao_cor.IDENT().getText()
                    color_val = definicao_cor.HEX_COLOR().getText()
                    self.colors[color_name] = color_val

            # Register shapes
            for shape in tree.definicaoShape():
                self.visit(shape)

        except Exception as e:
            pass

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

    def visitDefinicaoShape(self, ctx: PixelArtParser.DefinicaoShapeContext):
        shape_name = ctx.IDENT().getText()
        self.shapes[shape_name] = ctx

    def visitCmdPixel(self, ctx: PixelArtParser.CmdPixelContext):
        x, y = self.parse_coordenada(ctx.coordenada())
        color = self.get_color_hex(ctx.IDENT().getText())
        self.output.append(f'        <rect x="{x}" y="{y}" width="1" height="1" fill="{color}" />')

    def visitCmdRect(self, ctx: PixelArtParser.CmdRectContext):
        x1, y1 = self.parse_coordenada(ctx.coordenada(0))
        x2, y2 = self.parse_coordenada(ctx.coordenada(1))
        color = self.get_color_hex(ctx.IDENT().getText())

        x = min(x1, x2)
        y = min(y1, y2)
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1

        self.output.append(f'        <rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" />')

    def visitCmdLine(self, ctx: PixelArtParser.CmdLineContext):
        x1, y1 = self.parse_coordenada(ctx.coordenada(0))
        y1 = y1
        x2, y2 = self.parse_coordenada(ctx.coordenada(1))
        color = self.get_color_hex(ctx.IDENT().getText())

        self.output.append(f'        <line x1="{x1+0.5}" y1="{y1+0.5}" x2="{x2+0.5}" y2="{y2+0.5}" stroke="{color}" stroke-width="1" stroke-linecap="square"/>')

    def visitCmdCircle(self, ctx: PixelArtParser.CmdCircleContext):
        cx, cy = self.parse_coordenada(ctx.coordenada())
        radius = int(ctx.NUM().getText())
        color = self.get_color_hex(ctx.IDENT().getText())

        self.output.append(f'        <circle cx="{cx+0.5}" cy="{cy+0.5}" r="{radius}" fill="{color}" />')

    def visitCmdEllipse(self, ctx: PixelArtParser.CmdEllipseContext):
        cx, cy = self.parse_coordenada(ctx.coordenada())
        rx = int(ctx.NUM(0).getText())
        ry = int(ctx.NUM(1).getText())
        color = self.get_color_hex(ctx.IDENT().getText())

        self.output.append(f'        <ellipse cx="{cx+0.5}" cy="{cy+0.5}" rx="{rx}" ry="{ry}" fill="{color}" />')

    def visitCmdStar(self, ctx: PixelArtParser.CmdStarContext):
        cx, cy = self.parse_coordenada(ctx.coordenada())
        r_outer = int(ctx.NUM(0).getText())
        num_points = 5
        if ctx.NUM(1):
            num_points = int(ctx.NUM(1).getText())
        color = self.get_color_hex(ctx.IDENT().getText())

        ccx = cx + 0.5
        ccy = cy + 0.5
        r_inner = r_outer * 0.4

        points = []
        for i in range(2 * num_points):
            angle = i * math.pi / num_points - math.pi / 2
            r = r_outer if i % 2 == 0 else r_inner
            px = ccx + r * math.cos(angle)
            py = ccy + r * math.sin(angle)
            points.append(f"{px},{py}")

        points_str = " ".join(points)
        self.output.append(f'        <polygon points="{points_str}" fill="{color}" />')

    def visitCmdTriangle(self, ctx: PixelArtParser.CmdTriangleContext):
        x1, y1 = self.parse_coordenada(ctx.coordenada(0))
        x2, y2 = self.parse_coordenada(ctx.coordenada(1))
        x3, y3 = self.parse_coordenada(ctx.coordenada(2))
        color = self.get_color_hex(ctx.IDENT().getText())

        self.output.append(f'        <polygon points="{x1+0.5},{y1+0.5} {x2+0.5},{y2+0.5} {x3+0.5},{y3+0.5}" fill="{color}" />')

    def visitCmdSquare(self, ctx: PixelArtParser.CmdSquareContext):
        lx, ly = self.parse_coordenada(ctx.coordenada())
        size = int(ctx.NUM().getText())
        color = self.get_color_hex(ctx.IDENT().getText())
        is_centered = any(child.getText() == 'center' for child in ctx.getChildren())

        if is_centered:
            x = lx - size / 2.0
            y = ly - size / 2.0
        else:
            x = lx
            y = ly

        self.output.append(f'        <rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" />')

    def visitCmdRhombus(self, ctx: PixelArtParser.CmdRhombusContext):
        cx, cy = self.parse_coordenada(ctx.coordenada())
        w = int(ctx.NUM(0).getText())
        h = int(ctx.NUM(1).getText())
        color = self.get_color_hex(ctx.IDENT().getText())

        # Proportions of vertices
        ccx = cx + 0.5
        ccy = cy + 0.5
        p1 = f"{ccx},{ccy - h/2.0}"
        p2 = f"{ccx + w/2.0},{ccy}"
        p3 = f"{ccx},{ccy + h/2.0}"
        p4 = f"{ccx - w/2.0},{ccy}"

        self.output.append(f'        <polygon points="{p1} {p2} {p3} {p4}" fill="{color}" />')

    def visitCmdBrazilFlag(self, ctx: PixelArtParser.CmdBrazilFlagContext):
        lx, ly = self.parse_coordenada(ctx.coordenada())
        w = int(ctx.NUM().getText())
        h = w * 0.7

        # Calculate coordinates for internal shapes
        cx = lx + w / 2.0
        cy = ly + h / 2.0
        rx = 0.415 * w
        ry = 0.2905 * w
        R = 0.175 * w

        self.output.append(f'        <!-- Bandeira do Brasil -->')
        self.output.append(f'        <g>')
        self.output.append(f'            <!-- Retangulo verde -->')
        self.output.append(f'            <rect x="{lx}" y="{ly}" width="{w}" height="{h}" fill="#009739" />')
        self.output.append(f'            <!-- Losango amarelo -->')
        self.output.append(f'            <polygon points="{cx},{cy-ry} {cx+rx},{cy} {cx},{cy+ry} {cx-rx},{cy}" fill="#FEDD00" />')
        self.output.append(f'            <!-- Circulo azul -->')
        self.output.append(f'            <circle cx="{cx}" cy="{cy}" r="{R}" fill="#012169" />')
        self.output.append(f'            <!-- Faixa branca em arco -->')
        self.output.append(f'            <path d="M {cx - 0.96*R} {cy + 0.25*R} Q {cx} {cy - 0.1*R} {cx + 0.96*R} {cy - 0.25*R}" fill="none" stroke="#FFFFFF" stroke-width="{0.08*R}" />')
        self.output.append(f'        </g>')

    def visitCmdDrawShape(self, ctx: PixelArtParser.CmdDrawShapeContext):
        shape_name = ctx.IDENT().getText()
        shape_ctx = self.shapes.get(shape_name)
        if not shape_ctx:
            return  # Handled by semantic visitor

        tx, ty = self.parse_coordenada(ctx.coordenada())

        # Collect modifiers
        rotate_deg = 0
        flip_type = None

        for mod in ctx.shapeModifier():
            if mod.NUM():
                rotate_deg = int(mod.NUM().getText())
            elif mod.getChild(1):
                flip_type = mod.getChild(1).getText()

        transform_parts = [f"translate({tx}, {ty})"]
        if rotate_deg != 0:
            transform_parts.append(f"rotate({rotate_deg})")
        if flip_type == 'horizontal':
            transform_parts.append("scale(-1, 1)")
        elif flip_type == 'vertical':
            transform_parts.append("scale(1, -1)")
        elif flip_type == 'both':
            transform_parts.append("scale(-1, -1)")

        transform_str = " ".join(transform_parts)

        self.output.append(f'        <!-- Instancia de {shape_name} -->')
        self.output.append(f'        <g transform="{transform_str}">')

        # Visit elements of this shape
        for cmd in shape_ctx.comando():
            self.visit(cmd)

        self.output.append('        </g>')
