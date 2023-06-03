from funcionalidade import *

forca = Forca()
jogarDeNovo = True

while jogarDeNovo:
    forca.cabecalho('titulo')
    forca.escolha_Do_Jogador()
    forca.escolha_Do_pc()
    forca.vencedor()
    jogarDeNovo = forca.jogarNovamente()
