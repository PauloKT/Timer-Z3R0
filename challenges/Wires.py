from random import randint, choice
from time import sleep
from utils.colors import colors, color_print
from utils.helpers import clear

class Wire:
    def __init__(self, color):
        self.colorName = color
        self.colorCode = colors[color]
        self.cutted = False
        self.isCorrectWire = False

    def cut(self):
        for i in range(5):
            clear()
            print("Cortando fio... \n")
            print(f'{" " * (4 - i)}✂️')
            for _ in range(5):
                print(f"{colors['NEGRITO']} {self.colorCode}|{colors['BRANCO']}")
            sleep(0.5)

        clear()
        print(f"Fio {colors['NEGRITO']}{self.colorCode}{self.colorName}{colors['BRANCO']} cortado!")
        self.cutted = True
        sleep(1)
        return self


class WiresChallenge():
    def __init__(self, bomb):
        self.bomb = bomb
        self.serial_number = bomb.serial_number
        self.wires = []

    def start(self):
        
        color_print("\n=== DESAFIO DOS FIOS ===", "NEGRITO")
        color_print("Você está prestes a encarar o módulo de fios explosivo!", "CIANO")
        print(f"Se quiser ver o guia antes de começar, digite: {colors['AMARELO']}Guia {colors['BRANCO']}e pressione Enter.\n")
        
        resposta = input("> ")
        
        clear()
        
        if resposta.lower() == "guia":
            self.show_guide()
            
        color_print("\nPreparando o módulo de fios...\n\n", "AZUL")
        sleep(3)

        self.initialize_wires()
        self.show_wires()

        print(f"Número de série da bomba: {self.serial_number}\n")
        
        while True:
            option = input("Qual fio você vai cortar?\n> ")

            if not option.isdigit() or not (1 <= int(option) <= len(self.wires)):
                color_print("Entrada inválida. Digite um número válido do fio.", "VERMELHO")
                continue

            selectedWire = self.wires[int(option) - 1]

            if selectedWire.cutted:
                color_print("Esse fio já está cortado", "VERMELHO")
                sleep(1)
            else:
                selectedWire.cut()
                if selectedWire.isCorrectWire:
                    color_print("Você cortou o fio correto ✅", "VERDE")
                    sleep(1)
                    return True
                else:
                    color_print("Você cortou o fio incorreto!", "VERMELHO")
                    sleep(1)
                    timeOver = self.bomb.timer.removeTime(120)
                    if timeOver == True:
                        return False

            self.show_wires()
                
    def show_guide(self):
        
        texts = [
            {"text": "\nA Respeito dos Fios", "color": "NEGRITO"},

            {"text": "Fios são o sangue vital dos eletrônicos! Espere, não, eletricidade é o sangue vital. Fios são tipo artérias. Ou veias? Não importa...\n", "color": "CIANO"},

            {"text": "Um módulo de fios pode ter de 3 a 6 fios nele", "color": "AZUL"},
            {"text": "Apenas um fio correto precisa ser cortado para desarmar o módulo.", "color": "AZUL"},
            {"text": "A ordem dos fios começa com o primeiro no topo.\n", "color": "AZUL"},

            {"text": "3 fios:", "color": "NEGRITO"},
            {"text": "- Se não houver fios vermelhos, corte o segundo fio.", "color": "VERMELHO"},
            {"text": "- Caso contrário, se o último fio for branco, corte o último fio.", "color": "BRANCO"},
            {"text": "- Caso contrário, se houver mais de um fio azul, corte o último fio azul.", "color": "AZUL"},
            {"text": "- Caso contrário, corte o último fio.\n", "color": "CIANO"},

            {"text": "4 fios:", "color": "NEGRITO"},
            {"text": "- Se houver mais de um fio vermelho e o último dígito do serial for ímpar, corte o último fio vermelho.", "color": "VERMELHO"},
            {"text": "- Caso contrário, se o último fio for amarelo e não houver fios vermelhos, corte o primeiro fio.", "color": "AMARELO"},
            {"text": "- Caso contrário, se houver exatamente um fio azul, corte o primeiro fio.", "color": "AZUL"},
            {"text": "- Caso contrário, se houver mais de um fio amarelo, corte o último fio.", "color": "AMARELO"},
            {"text": "- Caso contrário, corte o segundo fio.\n", "color": "CIANO"},

            {"text": "5 fios:", "color": "NEGRITO"},
            {"text": "- Se o último fio for roxo e o último dígito do número de serial for ímpar, corte o quarto fio.", "color": "ROXO"},
            {"text": "- Caso contrário, se houver exatamente um fio vermelho e mais que um fio amarelo, corte o primeiro fio.", "color": "VERMELHO"},
            {"text": "- Caso contrário, se não houver fios roxos, corte o segundo fio.", "color": "ROXO"},
            {"text": "- Caso contrário, corte o primeiro fio.\n", "color": "CIANO"},

            {"text": "6 fios:", "color": "NEGRITO"},
            {"text": "- Se não houver fios amarelos e o último dígito do número de serial for ímpar, corte o terceiro fio.", "color": "AMARELO"},
            {"text": "- Caso contrário, se houver exatamente um fio amarelo e houver mais de um fio branco, corte o quarto fio.", "color": "AMARELO"},
            {"text": "- Caso contrário, se não houver fios vermelhos, corte o último fio.", "color": "VERMELHO"},
            {"text": "- Caso contrário, corte o quarto fio.\n", "color": "CIANO"},
        ]

        # Loop para exibir os textos com delay
        for item in texts:
            color_print(item["text"], item["color"])
            sleep(0.1)


    def generate_balanced_colors(self, amount, available_colors):
        wires = []
        max_per_color = 2
        color_count = {}

        while len(wires) < amount:
            color = choice(available_colors)
            count = color_count.get(color, 0)

            if count < max_per_color:
                wires.append(Wire(color))
                color_count[color] = count + 1

        return wires

    def initialize_wires(self):
        wires_amount = randint(3, 6)
        possible_colors = ["VERMELHO", "AZUL", "AMARELO", "VERDE", "BRANCO", "ROXO"]
        self.wires = self.generate_balanced_colors(wires_amount, possible_colors)
        correct_index = self.determine_correct_wire_index()
        self.wires[correct_index].isCorrectWire = True

    def determine_correct_wire_index(self):
        num_wires = len(self.wires)
        serial_last_digit = int(self.serial_number[-1])

        colors_list = []
        for wire in self.wires:
            colors_list.append(wire.colorName)

        def count(color):
            return colors_list.count(color)

        def indexes_of(color):
            result = []
            for i, c in enumerate(colors_list):
                if c == color:
                    result.append(i)
            return result

        def last_wire():
            return self.wires[-1].colorName
        
        def condition_3_wires():
            if count("VERMELHO") == 0:
                return 1
            elif last_wire() == "BRANCO":
                return num_wires - 1
            elif count("AZUL") > 1:
                return indexes_of("AZUL")[-1]
            else:
                return num_wires - 1

        def condition_4_wires():
            if count("VERMELHO") > 1 and serial_last_digit % 2 == 1:
                return indexes_of("VERMELHO")[-1]
            elif last_wire() == "AMARELO" and count("VERMELHO") == 0:
                return 0
            elif count("AZUL") == 1:
                return indexes_of("AZUL")[0]
            elif count("AMARELO") > 1:
                return indexes_of("AMARELO")[-1]
            else:
                return 1

        def condition_5_wires():
            if last_wire() == "ROXO" and serial_last_digit % 2 == 1:
                return 3
            elif count("VERMELHO") == 1 and count("AMARELO") > 1:
                return 0
            elif count("ROXO") == 0:
                return 1
            else:
                return 0

        def condition_6_wires():
            if count("AMARELO") == 0 and serial_last_digit % 2 == 1:
                return 2
            elif count("AMARELO") == 1 and count("BRANCO") > 1:
                return 3
            elif count("VERMELHO") == 0:
                return num_wires - 1
            else:
                return 3

        wire_rules = {
            3: condition_3_wires,
            4: condition_4_wires,
            5: condition_5_wires,
            6: condition_6_wires
        }

        if num_wires in wire_rules:
            return wire_rules[num_wires]()

        return 0

    def show_wires(self):
        for i in range(5):
            row = ""
            for wire in self.wires:
                if wire.cutted and i == 2:
                    row += f'{colors["NEGRITO"]} {wire.colorCode}  {colors["BRANCO"]}'
                else:
                    row += f'{colors["NEGRITO"]} {wire.colorCode}| {colors["BRANCO"]}'
            print(row)
            
        # Mostrar o número e o nome da cor de cada fio abaixo do visual
        print("\n")
        
        labels = ""
        
        for i, wire in enumerate(self.wires):
            formatted_text = f"{i + 1}-{wire.colorName}  "
            labels = labels + formatted_text

        print(labels)
