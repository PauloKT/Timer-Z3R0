from wires_challenge.wires import WiresChallenge
from cipher_challenge.CesarCypher import cifradeCesar

class Bomb:
    def __init__(self):
        self.challenges = [
            cifradeCesar(),
            WiresChallenge(),
            # Outros desafios
        ]

    def start(self):
        for challenge in self.challenges:
            challenge.start()
            print("Desafio concluído! Próximo desafio...")