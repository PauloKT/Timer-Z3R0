#tres bombas tres maneiras de defuzar// cada uma com um tipo de enigma diferente e dependendo da resposta a bomba explode

import random
from colors import colors, color_list

class Bomb:
    def __init__(self, wires, timer):
        self.wires = wires
        self.timer = timer
        self.is_defused = False
        self.exploded = False

    def show_wires(self):
        wires_amount = random.randint(3, 4)
        wires_order = []

        for i in range(wires_amount):
           wires_order.append(color_list[i])

        random.shuffle(wires_order)
        
        for i in wires_order:
            print(i['code'], '|')


        

class Bomb_One(Bomb):
    def __init__(self, wires, timer):
        super().__init__(wires, timer)

    def defuse(self):
        pass

bomb = Bomb([], 0)
bomb.show_wires()