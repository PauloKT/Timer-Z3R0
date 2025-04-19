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
        for i in range(5):
            clear()
            print("Cortando fio... \n")
            print(f'{" " * (4 - i)}✂️')
            for _ in range(5):
                print(f'{colors["NEGRITO"]} {self.colorCode}|{colors["BRANCO"]}')
            sleep(0.5)

        clear()
        print(f"Fio {colors['NEGRITO']}{self.colorCode}{self.colorName}{colors['BRANCO']} cortado!")
        self.cutted = True
        sleep(1)
        return self


class WiresChallenge(BaseChallenge):
    def __init__(self, debugMode):
        super().__init__(debugMode)
        self.wires = []
        self.serial_number = self.generate_serial_number()

    def generate_serial_number(self):
        return f"SN{randint(1000, 9999)}"

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
        possible_colors = ["VERMELHO", "AZUL", "AMARELO", "VERDE", "BRANCO", "PRETO"]
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
        
        self.debugPrint(f"Fios: {colors_list}")
        self.debugPrint(f"Último dígito do serial: {serial_last_digit}")

        def condition_3_wires():
            if count("VERMELHO") == 0:
                self.debugPrint("✔️ Nenhum fio vermelho → cortar o 2º fio")
                return 1
            elif last_wire() == "BRANCO":
                self.debugPrint("✔️ Último fio é branco → cortar o último fio")
                return num_wires - 1
            elif count("AZUL") > 1:
                self.debugPrint("✔️ Mais de um fio azul → cortar o último azul")
                return indexes_of("AZUL")[-1]
            else:
                self.debugPrint("✔️ Nenhuma outra condição → cortar o último fio")
                return num_wires - 1

        def condition_4_wires():
            if count("VERMELHO") > 1 and serial_last_digit % 2 == 1:
                self.debugPrint("✔️ Mais de um vermelho e serial ímpar → cortar o último vermelho")
                return indexes_of("VERMELHO")[-1]
            elif last_wire() == "AMARELO" and count("VERMELHO") == 0:
                self.debugPrint("✔️ Último fio é amarelo e não há vermelhos → cortar o 1º fio")
                return 0
            elif count("AZUL") == 1:
                self.debugPrint("✔️ Exatamente um fio azul → cortar o 1º fio azul")
                return indexes_of("AZUL")[0]
            elif count("AMARELO") > 1:
                self.debugPrint("✔️ Mais de um fio amarelo → cortar o último amarelo")
                return indexes_of("AMARELO")[-1]
            else:
                self.debugPrint("✔️ Nenhuma outra condição → cortar o 2º fio")
                return 1

        def condition_5_wires():
            if last_wire() == "PRETO" and serial_last_digit % 2 == 1:
                self.debugPrint("✔️ Último fio é preto e serial ímpar → cortar o 4º fio")
                return 3
            elif count("VERMELHO") == 1 and count("AMARELO") > 1:
                self.debugPrint("✔️ Um vermelho e mais de um amarelo → cortar o 1º fio")
                return 0
            elif count("PRETO") == 0:
                self.debugPrint("✔️ Nenhum fio preto → cortar o 2º fio")
                return 1
            else:
                self.debugPrint("✔️ Nenhuma outra condição → cortar o 1º fio")
                return 0

        def condition_6_wires():
            if count("AMARELO") == 0 and serial_last_digit % 2 == 1:
                self.debugPrint("✔️ Nenhum amarelo e serial ímpar → cortar o 3º fio")
                return 2
            elif count("AMARELO") == 1 and count("BRANCO") > 1:
                self.debugPrint("✔️ Um amarelo e mais de um branco → cortar o 4º fio")
                return 3
            elif count("VERMELHO") == 0:
                self.debugPrint("✔️ Nenhum vermelho → cortar o último fio")
                return num_wires - 1
            else:
                self.debugPrint("✔️ Nenhuma outra condição → cortar o 4º fio")
                return 3

        wire_rules = {
            3: condition_3_wires,
            4: condition_4_wires,
            5: condition_5_wires,
            6: condition_6_wires
        }

        if num_wires in wire_rules:
            return wire_rules[num_wires]()

        self.debugPrint("⚠️ Nenhuma regra encontrada → retornando o primeiro fio como padrão")
        return 0

    def start(self):
        self.initialize_wires()
        self.show_wires()

        print(f"Número de série da bomba: {self.serial_number}\n")

        while not self.completed:
            option = input("Qual fio você vai cortar?\nResposta: ")

            if not option.isdigit() or not (1 <= int(option) <= len(self.wires)):
                color_print("Entrada inválida. Digite um número válido do fio.", "VERMELHO")
                continue

            selectedWire = self.wires[int(option) - 1]

            if selectedWire.cutted:
                color_print("Esse fio já está cortado", "VERMELHO")
            else:
                selectedWire.cut()
                if selectedWire.isCorrectWire:
                    color_print("Você cortou o fio correto. Bomba desarmada! ✅", "VERDE")
                    self.completed = True
                    break
                else:
                    color_print("Você cortou o fio incorreto!", "VERMELHO")

            self.show_wires()

    def show_wires(self):
        for i in range(5):
            row = ""
            for wire in self.wires:
                if wire.cutted and i == 2:
                    row += f'{colors["NEGRITO"]} {wire.colorCode}  {colors["BRANCO"]}'
                else:
                    row += f'{colors["NEGRITO"]} {wire.colorCode}| {colors["BRANCO"]}'
            print(row)

        # Mostrar número e nome da cor abaixo
        
        labels = []
        for i, wire in enumerate(self.wires):
            labels.append(f"{i+1}-{wire.colorName}")

        print("\n" + "  ".join(label.center(12) for label in labels))
