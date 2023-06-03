from random import choice
import time
import os

class Forca:
    def __init__(self):
        self.pontos_pc = 0
        self.empate = 0
        self.pontos_jogador = 0
        self.quantidade_de_jogadas = 0
        #escolha da jogada 
        self.escolha = 0
        self.escolha_pc = 0
    
    def cabecalho(self):
        titulo = 'JOKEMPÔ'
        print("╔═════════════════════════════════════════════════════╗")
        print(f"║{titulo.center(53)}║")
        print("╠═════════════════════════════════════════════════════╣")
        print("╠═════════════════════════════════════════════════════╣")
        print(f"║       Vitorias: {self.pontos_jogador}                Derrotas: {self.pontos_pc}        ║")
        print("║                                                     ║")
        print(f"║       Empates: {self.empate}       Para sair digite: 999        ║")
        print("║                                                     ║")
        print("╚═════════════════════════════════════════════════════╝")

    def pedra(self):
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")

    def papel(self):
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")

    def tesoura(self):
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
    
    def versus(self):
        print("V    V  SSSS")
        print("V    V S")
        print("V    V  SSS")
        print(" V  V      S")
        print("  V    SSSS")

    def escolha_Do_Jogador(self):

        while True:
            print('Escolha a sua jogada:\n [1] PEDRA\n [2] PAPEL\n [3]  TESOURA')
            valor = input()
            if valor in '123':
                try:
                    self.escolha = int(valor)
                    break
                except ValueError:
                    print("Digite um valor válido e inteiro.")
            else:
                print("Por favor, escolha um valor válido acima.")

    def escolha_Do_pc(self):
        pc = [1, 2, 3]
        self.escolha_pc = choice(pc)

    def cleamTime(self, time=0, clear=False):
        time.sleep(time)
        if clear:
            os.system("cls")
    
    def vencedor(self):
        








if __name__ == '__main__':
    obj = Forca()
    obj.cabecalho()
    # obj.pedra()
    # obj.tesoura()
    # obj.versus()
    # obj.papel()
    obj.escolha_Do_Jogador()
    print(obj.escolha)

    