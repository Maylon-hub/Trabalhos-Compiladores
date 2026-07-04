@echo off
echo ==== Testando 1_valido.pxl ====
python main.py casos_de_teste\1_valido.pxl casos_de_teste\1_valido.html
echo Saida gerada em casos_de_teste\1_valido.html
echo.

echo ==== Testando 2_erro_sintatico.pxl ====
python main.py casos_de_teste\2_erro_sintatico.pxl casos_de_teste\2_erro_sintatico.out
type casos_de_teste\2_erro_sintatico.out
echo.

echo ==== Testando 3_erro_cor_nao_declarada.pxl ====
python main.py casos_de_teste\3_erro_cor_nao_declarada.pxl casos_de_teste\3_erro_cor_nao_declarada.out
type casos_de_teste\3_erro_cor_nao_declarada.out
echo.

echo ==== Testando 4_erro_cor_redefinida.pxl ====
python main.py casos_de_teste\4_erro_cor_redefinida.pxl casos_de_teste\4_erro_cor_redefinida.out
type casos_de_teste\4_erro_cor_redefinida.out
echo.

echo ==== Testando 5_erro_fora_limites.pxl ====
python main.py casos_de_teste\5_erro_fora_limites.pxl casos_de_teste\5_erro_fora_limites.out
type casos_de_teste\5_erro_fora_limites.out
echo.

echo ==== Testando 6_shapes_valido.pxl ====
python main.py casos_de_teste\6_shapes_valido.pxl casos_de_teste\6_shapes_valido.html
echo Saida gerada em casos_de_teste\6_shapes_valido.html
echo.

echo ==== Testando 7_warnings_limites.pxl ====
python main.py casos_de_teste\7_warnings_limites.pxl casos_de_teste\7_warnings_limites.html
echo Saida gerada em casos_de_teste\7_warnings_limites.html
echo.
