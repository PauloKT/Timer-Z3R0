from challenges.Wires import WiresChallenge
from challenges.CesarCypher import CesarCypherChallenge
from challenges.Button import ButtonChallenge
from timer import Timer

from utils.colors import color_print
from artes.artes_timerZ3R0 import arte_sucesso, arte_explosion

from utils.helpers import clear
from time import sleep
from random import randint, shuffle

class Bomb:
    def __init__(self):
        
        self.timer = Timer(10 * 60)
        self.debugMode = False
        self.desarmed = False
        self.serial_number = self.generate_serial_number()
        self.name = "TNT"
        
        self.challenges = [
            CesarCypherChallenge(self),
            ButtonChallenge(self),
            WiresChallenge(self),
        ]

        print("Embaralhando desafios")
        shuffle(self.challenges)
        sleep(1)

    def start(self):
        for challenge in self.challenges:
            success = challenge.start()
            print(success)
            clear()
            if success == True:
                print("Desafio concluído! Próximo desafio...\n")
            else:
                self.explode()
                return
            sleep(2)

        print("Parabéns! Você desarmou a bomba!\n")
        sleep(1)
        print(arte_sucesso)
        
    def explode(self):
        clear()
        print("Vixe, a bomba ta fazendo um barulho meio estranho...\n")
        sleep(2)
        color_print(arte_explosion, "AMARELO")

    def generate_serial_number(self):
        return f"SN{randint(1000, 9999)}"