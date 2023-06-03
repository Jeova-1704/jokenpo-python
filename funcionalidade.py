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
        self.escolha_j = 0
        self.escolha_pc = 0
    
    def cabecalho(self, titulo):
        if titulo == 'titulo':
            titulo = 'JOKEMPÔ'
        else:
            titulo = titulo
        vitorias = f"Vitorias: {self.pontos_jogador}"
        derrotas = f"Derrotas: {self.pontos_pc}"
        empates = f"Empates: {self.empate}"
        encerramento = f"para encerrar digite: 999"
        print("╔═════════════════════════════════════════════════════╗")
        print(f"║{titulo.center(53)}║")
        print("╠═════════════════════════════════════════════════════╣")
        print("╠═════════════════════════════════════════════════════╣")
        print(f"║{vitorias.center(26)} {derrotas.center(26)}║")
        print("║                                                     ║")
        print(f"║{empates.center(53)}║")
        print("║                                                     ║")
        print("╚═════════════════════════════════════════════════════╝")

    def __pedra(self):
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")

    def __papel(self):
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")

    def __tesoura(self):
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")

    def escolha_Do_Jogador(self):

        while True:
            print('Escolha a sua jogada:\n [1] PEDRA\n [2] PAPEL\n [3]  TESOURA')
            valor = input('→')
            if valor in '123':
                try:
                    self.escolha_j = int(valor)
                    break
                except ValueError:
                    self.cleamTime()
                    self.cabecalho('titulo')
                    print("Digite um valor válido e inteiro.")
            else:
                self.cleamTime()
                self.cabecalho('titulo')
                print("Por favor, escolha um valor abaixo.")

    def escolha_Do_pc(self):
        pc = [1, 2, 3]
        self.escolha_pc = choice(pc)

    def cleamTime(self, segundos=0):
        time.sleep(segundos)
        os.system("cls")
    
    def vencedor(self):
        self.cleamTime()
        if self.escolha_j == 1 and self.escolha_pc == 1:
            #se player escolher PEDRA e pc escolher pedra
            print('-=-'*10)
            print('JOGADOR:')
            self.__pedra()
            print('PC:')
            self.__pedra()
            print('-=-'*10)
            self.empate += 1
            self.cleamTime(3)
            self.cabecalho("O jogo deu empate")

        elif self.escolha_j == 1 and self.escolha_pc == 2:  
            # se player escolher PEDRA e pc escolher papel
            print('-=-'*10)
            print('JOGADOR:')
            self.__pedra()
            print('PC:')
            self.__papel()
            print('-=-'*10)
            self.pontos_pc += 1
            self.cleamTime(3)
            self.cabecalho("O pc ganhou")

        elif self.escolha_j == 1 and self.escolha_pc == 3:
            # se player escolher PEDRA e pc escolher tesoura
            print('-=-'*10)
            print('JOGADOR:')
            self.__pedra()
            print('PC:')
            self.__tesoura()
            print('-=-'*10)
            self.pontos_jogador += 1
            self.cleamTime(3)
            self.cabecalho("O jogador ganhou")

        elif self.escolha_j == 2 and self.escolha_pc == 1:
            #se player escolher PAPEL e pc escolher PEDRA
            print('-=-'*10)
            print('JOGADOR:')
            self.__papel()
            print('PC:')
            self.__pedra()
            print('-=-'*10)
            self.pontos_jogador += 1
            self.cleamTime(3)
            self.cabecalho("O jogador ganhou")

        elif self.escolha_j == 2 and self.escolha_pc == 2:#se player escolher PAPEL e pc escolher PAPEL
            print('-=-'*10)
            print('JOGADOR:')
            self.__papel()
            print('PC:')
            self.__papel()
            print('-=-'*10)
            self.empate += 1
            self.cleamTime(3)
            self.cabecalho("O jogo deu empate")

        elif self.escolha_j == 2 and self.escolha_pc == 3:
            # se player escolher PAPEL e pc escolhe tesoura
            print('-=-'*10)
            print('JOGADOR:')
            self.__papel()
            print('PC:')
            self.__tesoura()
            print('-=-'*10)
            self.pontos_pc += 1
            self.cleamTime(3)
            self.cabecalho("O pc ganhou")

        elif self.escolha_j == 3 and self.escolha_pc == 1:
            #se player escolher TESOURA e pc escolhe PEDRA
            print('-=-'*10)
            print('JOGADOR:')
            self.__tesoura()
            print('PC:')
            self.__pedra()
            print('-=-'*10)
            self.pontos_pc += 1
            self.cleamTime(3)
            self.cabecalho("O pc ganhou")

        elif self.escolha_j == 3 and self.escolha_pc == 2:  # se player escolher TESOURA e pc escolhe PAPEL
            print('-=-'*10)
            print('JOGADOR:')
            self.__tesoura()
            print('PC:')
            self.__papel()
            print('-=-'*10)
            self.pontos_jogador += 1
            self.cleamTime(3)
            self.cabecalho("O jogador ganhou")

        elif self.escolha_j == 3 and self.escolha_pc == 3:  # se player escolher TESOURA e pc escolhe TESOURA
            print('-=-'*10)
            print('JOGADOR:')
            self.__tesoura()
            print('PC:')
            self.__tesoura()
            print('-=-'*10)
            self.empate += 1
            self.cleamTime(3)
            self.cabecalho("O jogo deu empate")
    
    def encerramento(self):
        self.cleamTime()
        self.cabecalho('END GAME! Resultado final:')

    def jogarNovamente(self):
        jogarDeNovo = input("Você deseja jogar novamente [S/N]").lower().strip()
        while jogarDeNovo not in ['s', 'n', 'sim', 'não']:
            jogarDeNovo = input("Resposta inválida. Por favor, responda novamente [S/N]").lower().strip()
        if jogarDeNovo in ['s', 'sim']:
            self.cleamTime()
            return True
        else:
            self.cleamTime()
            self.encerramento()
            self.cleamTime(3)
            return False



if __name__ == '__main__':
    obj = Forca()
    obj.cabecalho('titulo')
    # obj.pedra()
    # obj.tesoura()
    # obj.versus()
    # obj.papel()
    # obj.escolha_Do_Jogador()
    # print(obj.escolha_j)
    obj.jogarNovamente()

    