from challenges.wires import WiresChallenge

class Bomb:
    def __init__(self):
        self.challenges = [
            WiresChallenge(),
            # Outros desafios
        ]

    def start(self):
        for challenge in self.challenges:
            challenge.start()
            print("Desafio concluído! Próximo desafio...")