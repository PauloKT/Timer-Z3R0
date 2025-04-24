from challenges.Wires import WiresChallenge
from challenges.CesarCypher import CesarCypherChallenge
from challenges.Button import ButtonChallenge

from utils.helpers import clear
from time import sleep

class Bomb:
    def __init__(self):
        self.challenges = [
            WiresChallenge(),
            ButtonChallenge(),
            CesarCypherChallenge(),
            # Outros desafios
        ]

    def start(self):
        for challenge in self.challenges:
            challenge.start()
            clear()
            print("Desafio concluído! Próximo desafio...\n")
            sleep(2)