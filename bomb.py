    from challenges.wires import WiresChallenge

    class Bomb:
        def __init__(self, debugMode):
            self.challenges = [
                WiresChallenge(debugMode),
                # Outros desafios
            ]

        def start(self):
            for challenge in self.challenges:
                challenge.start()
                print("Desafio concluído! Próximo desafio...")