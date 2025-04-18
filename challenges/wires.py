from random import randint, shuffle, choice
from time import sleep
from challenges.baseChallenge import BaseChallenge
from utils.colors import colors, color_print
from utils.helpers import clear

class Wire:
    def __init__(self, color):
        self.colorName = color
        self.colorCode = colors[color]
        self.cutted = False
        self.isCorrectWire = False

    def cut(self):
        # Simula o movimento da tesoura cortando o fio
        for i in range(5):
            clear()
            print("Cortando fio... \n")
            print(f'{" " * (4 - i)}✂️')
            for _ in range(5):
                print(f'{colors["NEGRITO"]} {self.colorCode}|{colors["BRANCO"]}')
            sleep(0.5)

        # Após a animação, o fio é cortado
        clear()
        print(f"Fio {colors['NEGRITO']}{self.colorCode}{self.colorName}{colors['BRANCO']} cortado!")
        self.cutted = True  # Marca o fio como cortado
        sleep(1)
        return self

class WiresChallenge(BaseChallenge):
    def __init__(self):
        super().__init__()
        self.wires = {}

    def initialize_wires(self):
        wires_amount = randint(3, 4)  # Define a quantidade de fios (entre 3 e 4)
        wires_colors = ["VERDE", "AZUL", "AMARELO", "VERMELHO"]  # Cores possíveis dos fios
        shuffle(wires_colors)  # Embaralha as cores

        # Cria os fios com base na quantidade definida
        for color in wires_colors[:wires_amount]:
            self.wires[color] = Wire(color)

        # Escolhe aleatoriamente o fio correto
        wire = self.wires[choice(wires_colors)]
        wire.isCorrectWire = True  # Marca o fio como o correto

        # Exibe uma mensagem de teste para identificar o fio correto (apenas para debug)
        color_print(f"[TESTE] O fio que precisa ser cortado é o {wire.colorName}", wire.colorName)

    def start(self):
        self.initialize_wires()  # Configura os fios da bomba
        self.show_wires()  # Mostra os fios no terminal

        while not self.completed:
            # Solicita ao jogador que escolha um fio para cortar
            option = input("Qual fio você vai cortar?\nResposta: ").upper()
            clear()

            # Verifica se o fio escolhido existe
            selectedWire = None
            for wire in self.wires.values():
                if wire.colorName == option:
                    selectedWire = wire
                    break

            if not selectedWire:
                color_print("Esse fio não existe", "VERMELHO")
            elif selectedWire.cutted:
                color_print("Esse fio já está cortado", "VERMELHO")
            else:
                selectedWire.cut()  # Corta o fio escolhido

                if selectedWire.isCorrectWire:
                    color_print("Você cortou o fio correto", "VERDE")
                    self.completed = True  # Marca a bomba como desarmada
                    break  # Sai do loop, pois a bomba foi desarmada
                else:
                    color_print("Você cortou o fio incorreto", "VERMELHO")

            # Mostra os fios após cada interação
            self.show_wires()

    def show_wires(self):
        for i in range(5):  # Exibe os fios 5 vezes para simular um efeito visual
            row = ""
            for wire in self.wires.values():
                if wire.cutted and i == 2:  # Mostra o fio cortado de forma diferente
                    row += f'{colors["NEGRITO"]} {wire.colorCode}  {colors["BRANCO"]}'
                else:
                    row += f'{colors["NEGRITO"]} {wire.colorCode}| {colors["BRANCO"]}'
            print(row)