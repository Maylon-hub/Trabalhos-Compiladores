# Roteiro de Apresentação (Pitch de Vendas) - PixelArtDSL

**Duração Estimada:** 2 a 3 minutos (Simples e Direto).
**Apresentadores:** Eduardo e Maylon.

---

## Cena 1: O que é a PixelArtDSL? (Como Funciona)
* **Visual:** Compartilhamento de tela com o arquivo `casos_de_teste/6_shapes_valido.pxl` aberto. Destacar o cabeçalho `canvas`, a paleta de cores `palette`, os blocos `shape` e `draw`.
* **Áudio (Apresentador 1):** 
  > *"Olá! Esta é a **PixelArtDSL**, uma linguagem declarativa projetada especificamente para a criação e renderização de pixel arts vetoriais em alta resolução via HTML/SVG. Com ela, você define o tamanho do canvas, mapeia uma paleta de cores amigável e expressa seu desenho de forma intuitiva, como círculos, retângulos e linhas."*
* **Áudio (Apresentador 2):**
  > *"A linguagem também suporta recursos avançados como **Imports** de arquivos externos e **Shapes**, permitindo que você crie formatos reutilizáveis e aplique translação (`at`), rotação (`rotate`) e espelhamento (`flip`) neles, além de contar com primitivas prontas como triângulos, quadrados, losangos, estrelas e a bandeira do Brasil."*

---

## Cena 2: Compilando e Mostrando a Mágica (Demonstração Prática)
* **Visual:** Abrir o terminal e executar o compilador:
  `python main.py casos_de_teste/6_shapes_valido.pxl output.html`
  Em seguida, abrir o arquivo `output.html` gerado no navegador, mostrando os desenhos nítidos, a bandeira e as rotações dos smileys.
* **Áudio (Apresentador 1):**
  > *"Vamos rodar o compilador! Com um único comando, o arquivo `.pxl` é processado e gera um HTML autônomo. O resultado é renderizado usando SVG nativo. Graças à propriedade CSS `shape-rendering: crispEdges`, o pixel art mantém bordas perfeitamente nítidas e escaláveis sem borrão."*

---

## Cena 3: Validações Semânticas e Alerta de Limites (Warnings)
* **Visual:** Mostrar o terminal rodando o caso de teste `7_warnings_limites.pxl`. Destacar os warnings no console e o banner amarelo flutuante no HTML gerado.
* **Áudio (Apresentador 2):**
  > *"O compilador também realiza análise semântica inteligente. Em vez de abortar por erros de coordenadas fora do canvas, ele gera **warnings (avisos)** amigáveis no console e insere este banner flutuante premium no HTML. Isso permite ao usuário criar cortes geométricos (como semicírculos) sabendo exatamente quais elementos passaram dos limites."*

---

## Cena 4: Encerramento
* **Visual:** Mostrar o link do repositório GitHub e os créditos dos integrantes.
* **Áudio (Apresentadores juntos):**
  > *"A PixelArtDSL é leve, modular e pronta para dar vida aos seus designs de pixel art. O código-fonte está disponível no nosso repositório. Muito obrigado!"*
