import os
import math
from antlr4 import FileStream, CommonTokenStream
from PixelArtVisitor import PixelArtVisitor
from PixelArtParser import PixelArtParser
from PixelArtLexer import PixelArtLexer

class SemanticVisitor(PixelArtVisitor):
    def __init__(self, base_dir=""):
        super(SemanticVisitor, self).__init__()
        self.base_dir = base_dir
        self.errors = []
        self.warnings = []
        self.colors = {}
        self.shapes = {}  # shape_name -> shape_ctx
        self.canvas_width = 0
        self.canvas_height = 0
        self.imported_files = set()  # prevent circular imports

    def parse_coordenada(self, coord_ctx):
        tokens = [coord_ctx.getChild(i).getText() for i in range(coord_ctx.getChildCount())]
        comma_idx = tokens.index(',')
        x = int("".join(tokens[1:comma_idx]))
        y = int("".join(tokens[comma_idx+1:-1]))
        return x, y

    def transform_coordinate(self, x, y, tx, ty, rotate_deg, flip_type):
        # 1. Flip
        if flip_type == 'horizontal':
            x, y = -x, y
        elif flip_type == 'vertical':
            x, y = x, -y
        elif flip_type == 'both':
            x, y = -x, -y

        # 2. Rotate (clockwise standard Y-down)
        rad = math.radians(rotate_deg)
        cos_val = math.cos(rad)
        sin_val = math.sin(rad)
        rx = x * cos_val - y * sin_val
        ry = x * sin_val + y * cos_val

        # 3. Translate
        return round(rx + tx), round(ry + ty)

    def combine_flips(self, f1, f2):
        if not f1: return f2
        if not f2: return f1
        if f1 == 'both':
            if f2 == 'both': return None
            if f2 == 'horizontal': return 'vertical'
            if f2 == 'vertical': return 'horizontal'
        if f1 == 'horizontal':
            if f2 == 'both': return 'vertical'
            if f2 == 'horizontal': return None
            if f2 == 'vertical': return 'both'
        if f1 == 'vertical':
            if f2 == 'both': return 'horizontal'
            if f2 == 'horizontal': return 'both'
            if f2 == 'vertical': return None
        return None

    def check_global_coordinate(self, x, y, line):
        if x < 0 or x >= self.canvas_width or y < 0 or y >= self.canvas_height:
            self.warnings.append(
                f"Linha {line}: coordenada ({x},{y}) fora dos limites do canvas ({self.canvas_width}x{self.canvas_height})"
            )

    def check_color_exists(self, color_name, line):
        if color_name not in self.colors:
            self.errors.append(f"Linha {line}: cor '{color_name}' nao declarada na palette")

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

        # 4. Process shapes
        for shape in ctx.definicaoShape():
            self.visit(shape)

        # 5. Process draw
        if ctx.definicaoDraw():
            self.visit(ctx.definicaoDraw())

    def visitDefinicaoImport(self, ctx: PixelArtParser.DefinicaoImportContext):
        import_path_str = ctx.STRING().getText().strip('"')
        full_path = os.path.normpath(os.path.join(self.base_dir, import_path_str))

        if full_path in self.imported_files:
            return  # circular import prevention

        self.imported_files.add(full_path)

        if not os.path.exists(full_path):
            self.errors.append(f"Linha {ctx.start.line}: arquivo importado nao encontrado: '{import_path_str}'")
            return

        try:
            input_stream = FileStream(full_path, encoding='utf-8')
            lexer = PixelArtLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = PixelArtParser(stream)
            tree = parser.programa()

            # Process imports inside the imported file
            for imp in tree.definicaoImport():
                self.visit(imp)

            # Register palette colors from import (without triggering duplication errors on main)
            if tree.definicaoPalette():
                for definicao_cor in tree.definicaoPalette().definicaoCor():
                    color_name = definicao_cor.IDENT().getText()
                    color_val = definicao_cor.HEX_COLOR().getText()
                    if color_name in self.colors and self.colors[color_name] != color_val:
                        self.errors.append(
                            f"Linha {definicao_cor.start.line}: cor '{color_name}' redefinida com valor diferente no import"
                        )
                    else:
                        self.colors[color_name] = color_val

            # Register shapes from import
            for shape in tree.definicaoShape():
                self.visit(shape)

        except Exception as e:
            self.errors.append(f"Linha {ctx.start.line}: erro ao processar import '{import_path_str}': {e}")

    def visitDefinicaoCanvas(self, ctx: PixelArtParser.DefinicaoCanvasContext):
        self.canvas_width = int(ctx.NUM(0).getText())
        self.canvas_height = int(ctx.NUM(1).getText())
        if self.canvas_width <= 0 or self.canvas_height <= 0:
            self.errors.append(f"Linha {ctx.start.line}: canvas deve ter dimensoes maiores que zero")

    def visitDefinicaoPalette(self, ctx: PixelArtParser.DefinicaoPaletteContext):
        seen_in_palette = set()
        for definicao_cor in ctx.definicaoCor():
            color_name = definicao_cor.IDENT().getText()
            color_val = definicao_cor.HEX_COLOR().getText()
            if color_name in seen_in_palette:
                self.errors.append(f"Linha {definicao_cor.start.line}: cor '{color_name}' ja declarada")
            else:
                seen_in_palette.add(color_name)
                if color_name in self.colors and self.colors[color_name] != color_val:
                    self.errors.append(
                        f"Linha {definicao_cor.start.line}: cor '{color_name}' ja declarada com valor diferente"
                    )
                else:
                    self.colors[color_name] = color_val

    def visitDefinicaoShape(self, ctx: PixelArtParser.DefinicaoShapeContext):
        shape_name = ctx.IDENT().getText()
        if shape_name in self.shapes:
            self.errors.append(f"Linha {ctx.start.line}: shape '{shape_name}' ja definido")
        else:
            self.shapes[shape_name] = ctx

        # Static check colors of commands inside shape
        for cmd in ctx.comando():
            actual_cmd = cmd.getChild(0)
            if not isinstance(actual_cmd, (PixelArtParser.CmdDrawShapeContext, PixelArtParser.CmdBrazilFlagContext)):
                color_name = actual_cmd.IDENT().getText()
                self.check_color_exists(color_name, actual_cmd.start.line)

    def visitDefinicaoDraw(self, ctx: PixelArtParser.DefinicaoDrawContext):
        for cmd in ctx.comando():
            self.check_command_bounds(cmd.getChild(0), 0, 0, 0, None, set())

    def check_command_bounds(self, cmd, tx, ty, rotate_deg, flip_type, visited_shapes):
        if isinstance(cmd, PixelArtParser.CmdPixelContext):
            lx, ly = self.parse_coordenada(cmd.coordenada())
            gx, gy = self.transform_coordinate(lx, ly, tx, ty, rotate_deg, flip_type)
            self.check_global_coordinate(gx, gy, cmd.start.line)
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdRectContext):
            lx1, ly1 = self.parse_coordenada(cmd.coordenada(0))
            lx2, ly2 = self.parse_coordenada(cmd.coordenada(1))
            corners = [(lx1, ly1), (lx2, ly1), (lx1, ly2), (lx2, ly2)]
            for cx, cy in corners:
                gx, gy = self.transform_coordinate(cx, cy, tx, ty, rotate_deg, flip_type)
                self.check_global_coordinate(gx, gy, cmd.start.line)
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdLineContext):
            lx1, ly1 = self.parse_coordenada(cmd.coordenada(0))
            lx2, ly2 = self.parse_coordenada(cmd.coordenada(1))
            gx1, gy1 = self.transform_coordinate(lx1, ly1, tx, ty, rotate_deg, flip_type)
            gx2, gy2 = self.transform_coordinate(lx2, ly2, tx, ty, rotate_deg, flip_type)
            self.check_global_coordinate(gx1, gy1, cmd.start.line)
            self.check_global_coordinate(gx2, gy2, cmd.start.line)
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdCircleContext):
            lcx, lcy = self.parse_coordenada(cmd.coordenada())
            gcx, gcy = self.transform_coordinate(lcx, lcy, tx, ty, rotate_deg, flip_type)
            radius = int(cmd.NUM().getText())
            if radius < 0:
                self.errors.append(f"Linha {cmd.start.line}: raio do circulo nao pode ser negativo")
            else:
                if gcx - radius < 0 or gcx + radius >= self.canvas_width or gcy - radius < 0 or gcy + radius >= self.canvas_height:
                    self.warnings.append(
                        f"Linha {cmd.start.line}: circulo ({gcx},{gcy}) excede os limites do canvas"
                    )
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdEllipseContext):
            lcx, lcy = self.parse_coordenada(cmd.coordenada())
            gcx, gcy = self.transform_coordinate(lcx, lcy, tx, ty, rotate_deg, flip_type)
            rx = int(cmd.NUM(0).getText())
            ry = int(cmd.NUM(1).getText())
            if rx < 0 or ry < 0:
                self.errors.append(f"Linha {cmd.start.line}: raio da elipse nao pode ser negativo")
            else:
                rad = math.radians(rotate_deg)
                cos_val = math.cos(rad)
                sin_val = math.sin(rad)
                h_width = math.sqrt((rx * cos_val) ** 2 + (ry * sin_val) ** 2)
                h_height = math.sqrt((rx * sin_val) ** 2 + (ry * cos_val) ** 2)
                min_x = gcx - h_width
                max_x = gcx + h_width
                min_y = gcy - h_height
                max_y = gcy + h_height
                if min_x < 0 or max_x >= self.canvas_width or min_y < 0 or max_y >= self.canvas_height:
                    self.warnings.append(
                        f"Linha {cmd.start.line}: elipse ({gcx},{gcy}) excede os limites do canvas"
                    )
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdStarContext):
            lcx, lcy = self.parse_coordenada(cmd.coordenada())
            gcx, gcy = self.transform_coordinate(lcx, lcy, tx, ty, rotate_deg, flip_type)
            radius = int(cmd.NUM(0).getText())
            if radius < 0:
                self.errors.append(f"Linha {cmd.start.line}: raio da estrela nao pode ser negativo")
            else:
                if gcx - radius < 0 or gcx + radius >= self.canvas_width or gcy - radius < 0 or gcy + radius >= self.canvas_height:
                    self.warnings.append(
                        f"Linha {cmd.start.line}: estrela ({gcx},{gcy}) excede os limites do canvas"
                    )
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdTriangleContext):
            lx1, ly1 = self.parse_coordenada(cmd.coordenada(0))
            lx2, ly2 = self.parse_coordenada(cmd.coordenada(1))
            lx3, ly3 = self.parse_coordenada(cmd.coordenada(2))
            gx1, gy1 = self.transform_coordinate(lx1, ly1, tx, ty, rotate_deg, flip_type)
            gx2, gy2 = self.transform_coordinate(lx2, ly2, tx, ty, rotate_deg, flip_type)
            gx3, gy3 = self.transform_coordinate(lx3, ly3, tx, ty, rotate_deg, flip_type)
            self.check_global_coordinate(gx1, gy1, cmd.start.line)
            self.check_global_coordinate(gx2, gy2, cmd.start.line)
            self.check_global_coordinate(gx3, gy3, cmd.start.line)
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdSquareContext):
            lx, ly = self.parse_coordenada(cmd.coordenada())
            size = int(cmd.NUM().getText())
            is_centered = any(child.getText() == 'center' for child in cmd.getChildren())
            if size < 0:
                self.errors.append(f"Linha {cmd.start.line}: tamanho do quadrado nao pode ser negativo")
            else:
                if is_centered:
                    half = size / 2.0
                    corners = [
                        (lx - half, ly - half),
                        (lx + half, ly - half),
                        (lx - half, ly + half),
                        (lx + half, ly + half)
                    ]
                else:
                    corners = [
                        (lx, ly),
                        (lx + size, ly),
                        (lx, ly + size),
                        (lx + size, ly + size)
                    ]
                for cx, cy in corners:
                    gx, gy = self.transform_coordinate(cx, cy, tx, ty, rotate_deg, flip_type)
                    self.check_global_coordinate(gx, gy, cmd.start.line)
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdRhombusContext):
            lcx, lcy = self.parse_coordenada(cmd.coordenada())
            w = int(cmd.NUM(0).getText())
            h = int(cmd.NUM(1).getText())
            if w < 0 or h < 0:
                self.errors.append(f"Linha {cmd.start.line}: largura e altura do losango nao podem ser negativas")
            else:
                corners = [
                    (lcx, lcy - h / 2.0),
                    (lcx + w / 2.0, lcy),
                    (lcx, lcy + h / 2.0),
                    (lcx - w / 2.0, lcy)
                ]
                for cx, cy in corners:
                    gx, gy = self.transform_coordinate(cx, cy, tx, ty, rotate_deg, flip_type)
                    self.check_global_coordinate(gx, gy, cmd.start.line)
            self.check_color_exists(cmd.IDENT().getText(), cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdBrazilFlagContext):
            lx, ly = self.parse_coordenada(cmd.coordenada())
            w = int(cmd.NUM().getText())
            h = w * 0.7
            if w < 0:
                self.errors.append(f"Linha {cmd.start.line}: largura da bandeira nao pode ser negativa")
            else:
                corners = [
                    (lx, ly),
                    (lx + w, ly),
                    (lx, ly + h),
                    (lx + w, ly + h)
                ]
                for cx, cy in corners:
                    gx, gy = self.transform_coordinate(cx, cy, tx, ty, rotate_deg, flip_type)
                    self.check_global_coordinate(gx, gy, cmd.start.line)

        elif isinstance(cmd, PixelArtParser.CmdDrawShapeContext):
            inner_shape_name = cmd.IDENT().getText()
            if inner_shape_name not in self.shapes:
                self.errors.append(f"Linha {cmd.start.line}: shape '{inner_shape_name}' nao definido")
            else:
                itx, ity = self.parse_coordenada(cmd.coordenada())
                irotate = 0
                iflip = None
                for mod in cmd.shapeModifier():
                    if mod.NUM():
                        irotate = int(mod.NUM().getText())
                    elif mod.getChild(1):
                        iflip = mod.getChild(1).getText()

                citx, city = self.transform_coordinate(itx, ity, tx, ty, rotate_deg, flip_type)
                cflip = self.combine_flips(flip_type, iflip)
                crotate = (rotate_deg + irotate) % 360

                self.check_shape_bounds(inner_shape_name, citx, city, crotate, cflip, cmd.start.line, visited_shapes)

    def check_shape_bounds(self, shape_name, tx, ty, rotate_deg, flip_type, line, visited_shapes):
        if shape_name in visited_shapes:
            self.errors.append(f"Linha {line}: recursao detectada no shape '{shape_name}'")
            return

        visited_shapes.add(shape_name)
        shape_ctx = self.shapes.get(shape_name)
        if shape_ctx:
            for cmd in shape_ctx.comando():
                self.check_command_bounds(cmd.getChild(0), tx, ty, rotate_deg, flip_type, visited_shapes)
        visited_shapes.remove(shape_name)
