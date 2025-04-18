# Importações necessárias
from random import randint, shuffle, choice  # Para gerar números aleatórios e embaralhar listas
from time import sleep  # Para criar pausas no programa
from os import system, name  # Para limpar o terminal
from colors import colors, color_print  # Para manipular cores no terminal

# Função para limpar o terminal
def clear():
    system('cls' if name == 'nt' else 'clear')  # 'cls' para Windows, 'clear' para outros sistemas

# Classe que representa um fio da bomba
class Wire:
    def __init__(self, color):
        self.colorName = color  # Nome da cor do fio
        self.colorCode = colors[color]  # Código da cor para exibição no terminal
        self.cutted = False  # Indica se o fio foi cortado
        self.isCorrectWire = False  # Indica se é o fio correto para desarmar a bomba

    # Método para cortar o fio
    def cut(self):
        print(f"Fio {colors['NEGRITO']}{self.colorCode}{self.colorName}{colors['BRANCO']} cortado!")
        self.cutted = True  # Marca o fio como cortado
        return self

# Classe que representa a bomba
class Bomb:
    def __init__(self, difficulty):
        self.difficulty = difficulty  # Nível de dificuldade da bomba
        self.wires = {}  # Dicionário para armazenar os fios
        self.wiresCompleted = False  # Indica se a bomba foi desarmada

    # Método principal para iniciar a lógica da bomba
    def start(self):
        self.initialize_wires()  # Inicializa os fios da bomba
        self.show_wires()  # Mostra os fios no terminal

        while True:
            # Solicita ao jogador que escolha um fio para cortar
            option = input("Qual fio você vai cortar?\nResposta: ").upper()
            clear()  # Limpa o terminal após a entrada do jogador

            selectedWire = None
            # Verifica se o fio escolhido existe
            for wire in self.wires.values():
                if wire.colorName == option:
                    selectedWire = wire

            if selectedWire:
                selectedWire.cut()  # Corta o fio escolhido

                # Verifica se o fio cortado é o correto
                if selectedWire.isCorrectWire:
                    color_print("Boa lek, acertou", "VERDE")
                    self.wiresCompleted = True  # Marca a bomba como desarmada
                else:
                    color_print("Porra lek, errou", "VERMELHO")

                # Remove o fio cortado da lista de fios
                del self.wires[selectedWire.colorName]
            else:
                color_print("O doidão, essa cor nem existe", "VERMELHO")

            # Continua mostrando os fios até que a bomba seja desarmada
            if not self.wiresCompleted:
                self.show_wires()
            else:
                break

    # Método para inicializar os fios da bomba
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

    # Método para exibir os fios no terminal
    def show_wires(self):
        for _ in range(5):  # Exibe os fios 5 vezes para simular um efeito visual
            row = ""
            for wire in self.wires.values():
                row += f'{colors["NEGRITO"]} {wire.colorCode}| {colors["BRANCO"]}'
            print(row)

# Início do programa
clear()  # Limpa o terminal antes de começar
bomb = Bomb(1)  # Cria uma bomba com dificuldade 1
bomb.start()  # Inicia o jogo