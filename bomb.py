from challenges.Wires import WiresChallenge
from challenges.CesarCypher import CesarCypherChallenge
from challenges.Button import ButtonChallenge
from timer import Timer

from utils.helpers import clear
from time import sleep
from random import randint

class Bomb:
    def __init__(self):
        
        self.timer = Timer(10 * 60)
        self.debugMode = False
        self.desarmed = False
        self.serial_number = self.generate_serial_number()
        self.name = "KABUM"
        
        self.challenges = [
            CesarCypherChallenge(self),
            ButtonChallenge(self),
            WiresChallenge(self),
        ]

    def start(self):
        for challenge in self.challenges:
            challenge.start()
            clear()
            print("Desafio concluído! Próximo desafio...\n")
            sleep(2)
            
    def generate_serial_number(self):
        return f"SN{randint(1000, 9999)}"