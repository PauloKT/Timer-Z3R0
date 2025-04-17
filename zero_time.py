#tres bombas tres maneiras de defuzar// cada uma com um tipo de enigma diferente e dependendo da resposta a bomba explode

import random
import os
from colors import colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Bomb:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.wires = [] 
        self.wire_completed = False
        self.correct_wire = None

    def start(self):
        self.initialize_wires()
        self.show_wires()

        while True:
            option = input("Qual fio você vai cortar?\nResposta: ").upper()
            clear()

            if option in self.wires:
                print(f"Fio {colors[option]}{option}{colors["BRANCO"]} cortado!")
                if option == self.correct_wire:
                    print(f"{colors["VERDE"]}Boa lek, acertou{colors["BRANCO"]}")
                    self.wire_completed = True
                else:
                    print(f"{colors["VERMELHO"]}Porra lek, errou{colors["BRANCO"]}")
                self.wires.remove(option)
            else:
                print(f"{colors["VERMELHO"]}O doidão, essa cor nem existe{colors["BRANCO"]}")

            if len(self.wires) > 0 and not self.wire_completed:
                self.show_wires()
            else:
                break


    def initialize_wires(self):
        wires_amount = random.randint(3, 4)
        wires_colors = ["VERDE", "AZUL", "AMARELO", "VERMELHO"]
        random.shuffle(wires_colors)

        self.correct_wire = random.choice(wires_colors)

        self.wires = wires_colors[:wires_amount] # Corta a lista até o número inteiro

    def show_wires(self):
        print(f"{colors[self.correct_wire]}[TESTE] O fio que precisa ser cortado é o {str.capitalize(self.correct_wire)}")
        for _ in range(5):
            row = ""
            for colorName in self.wires:
                colorCode = colors[colorName]
                row += f'{colors["NEGRITO"]} {colorCode}| {colors["BRANCO"]}'
            print(row)

clear()
bomb = Bomb(1)
bomb.start()