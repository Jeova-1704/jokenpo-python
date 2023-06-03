# Importando o modulo funcionalidades
from funcionalidade import *

#Criando o objeto a partit da classe Forca do modulo importado acima 
forca = Forca()
jogarDeNovo = True

# Enquanto jogar de novo for verdade o jogo continua 
while jogarDeNovo:
    forca.cabecalho('titulo')
    forca.escolha_Do_Jogador()
    forca.escolha_Do_pc()
    forca.vencedor()
    jogarDeNovo = forca.jogarNovamente()
