# PixelArtDSL - Compilador T6 (Trabalho Final)

Este projeto implementa a **PixelArtDSL**, uma Linguagem de Domínio Específico (DSL) declarativa focada na criação e renderização de pixel arts vetoriais de alta resolução via HTML/SVG. O compilador foi desenvolvido como o Trabalho Final (T6) da disciplina de Compiladores (DC/UFSCar).

## Integrantes do Grupo

* Eduardo Eudoro Lemos de Oliveira - RA 824757
* Maylon Martins de Melo - RA 800199

---

## Estrutura da Linguagem

A linguagem é dividida em blocos: `canvas`, `palette`, seções opcionais `shape` e o bloco de pintura principal `draw`. Ela permite ainda importar shapes de outros arquivos pxl utilizando a palavra-chave `import`.

### Exemplo de Programa Completo com Imports e Shapes

```text
// 1. Importação de shapes externos (arquivos reutilizáveis)
import "shapes_lib.pxl"

// 2. Definição da área de pintura e cor de fundo
canvas 64 x 64 background #1E1E1E

// 3. Definição dos nomes amigáveis para cores hexadecimais
palette {
    red = #FF5555
    green = #50FA7B
    blue = #8BE9FD
    yellow = #F1FA8C
    white = #F8F8F2
    black = #000000
    pink = #FF79C6
}

// 4. Definição de Shapes Locais (com coordenadas relativas)
shape star_pink {
    star (0, 0) 5 pink
}

// 5. Comandos de Pintura no Canvas
draw {
    // Figuras geométricas básicas com sintaxe simplificada (palavras-chave como "to", "center" e "radius" são opcionais)
    rect (5, 5) (15, 15) blue
    line (0, 0) (63, 63) red
    circle (32, 32) 8 yellow
    
    // Novas primitivas geométricas implementadas
    ellipse (32, 10) 6 3 red                              // Elipse com raios horizontal e vertical
    triangle (5, 45) (15, 45) (10, 55) pink               // Triângulo definido por 3 vértices
    square center (15, 30) size 6 green                    // Quadrado (definido pelo centro ou topo-esquerdo)
    rhombus center (50, 45) width 6 height 10 red          // Losango
    
    // Primitiva especial: Bandeira do Brasil (proporcionalidades oficiais e faixa branca em arco)
    brazilFlag (25, 25) 20                                 // Desenha no topo-esquerdo (25, 25) com largura 20
    
    // Instanciação e transformação de shapes
    drawShape smiley at (15, 15)                           // Smiley importado
    drawShape smiley at (45, 15) rotate 90                 // Smiley rotacionado 90 graus no sentido horário
    drawShape smiley at (45, 45) flip vertical             // Smiley espelhado verticalmente
    drawShape star_pink at (15, 45)                        // Shape local de estrela rosa
}
```

---

## Recursos e Funcionalidades do Compilador

### 1. Análise Léxica e Sintática (ALS)
A gramática `PixelArt.g4` define a sintaxe da linguagem. As coordenadas aceitam números assinados `(X, Y)` e as cores seguem o formato hexadecimal `#XXXXXX`. Palavras auxiliares como `to`, `center`, `radius`, `rx`, `ry`, `points`, `size`, `width` e `height` são opcionais, simplificando consideravelmente a codificação de desenhos.

### 2. Análise Semântica (AS)
Realiza validações cruciais antes de emitir o código final:
1. **Uso de Cores Indefinidas**: Acusa erro se usar uma cor inexistente no bloco `palette` ou nas paletas dos arquivos importados.
2. **Cores Redefinidas**: Evita que nomes de cores sejam redefinidos com valores diferentes.
3. **Resolução de Shapes e Imports**: Garante que shapes referenciados em `drawShape` existam (seja no próprio arquivo ou nos arquivos importados) e impede importações circulares e recursão infinita de shapes.
4. **Warnings de Limites (Out-of-Bounds)**: Ao invés de abortar a compilação por erro de coordenadas fora do canvas, o compilador gera **Avisos (Warnings)** amigáveis. Ele calcula a posição final transformada de todos os pontos (incluindo rotações e espelhamentos de shapes) e alerta o usuário sobre quais elementos estão fora da tela, permitindo que faça cortes (como desenhar círculos fora do limite para simular semicírculos).

### 3. Geração de Código (GCI)
A compilação de programas válidos gera um arquivo **HTML autônomo**. O compilador converte os comandos na estrutura de elementos vetoriais `<svg>` do W3C:
- Shapes instanciados pelo usuário são envelopados em blocos de transformação do SVG: `<g transform="translate(x, y) rotate(deg) scale(sx, sy)">`.
- Se houver warnings de limites, um banner de aviso flutuante premium e semitransparente (glassmorphic) é inserido no canto superior direito do HTML gerado, instruindo o usuário sobre o corte das coordenadas.

---

## Instalação e Execução

### Dependências
- Python 3
- ANTLR4 Runtime (`pip install antlr4-python3-runtime==4.13.2`)
- Java JRE (necessário apenas caso queira alterar e recompilar a gramática `.g4`)

### Compilar e Rodar o Gerador
Para compilar um arquivo de entrada e gerar a saída HTML:
```bash
python main.py <arquivo_entrada.pxl> <arquivo_saida.html>

# Exemplo de teste incluso:
python main.py casos_de_teste/6_shapes_valido.pxl teste_shapes.html
```

### Rodar a Suite de Testes
O projeto inclui uma suite de testes que executa testes sintáticos, semânticos, de warnings e de shapes com imports:
```bash
# Windows
test.bat
```

### Re-gerar o Parser ANTLR
Caso modifique a gramática no arquivo `PixelArt.g4`, execute o comando abaixo para atualizar os arquivos gerados:
```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor PixelArt.g4
```
