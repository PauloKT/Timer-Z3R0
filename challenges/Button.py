import random
import time

from utils.colors import colors, color_print

class ButtonChallenge:
    def __init__(self, bomb):
        self.bomb = bomb
        self.bomb_name = bomb.name
        self.number = random.randint(1, 10)
        self.secret_number = random.randint(1, 10)
        self.attempts = 0

    def show_button(self):
        color_print("\n--- DESAFIO DO BOTÃO ---", "NEGRITO")
        if self.number < 3:
            print(f'''      ______________________
     |                      |
     | {colors['VERDE']} PRESS TO DEFUSE {colors['BRANCO']}  |
     |______________________|  ({self.number} vezes)''')

        elif self.number == 4:
            print(f'''      ______________________
     |                      |
     | {colors['AMARELO']} BOMBA ESPECIAL - AUTENTICAÇÃO REQUERIDA {colors['BRANCO']} |
     |______________________|  ({self.number} vezes)''')

        else:
            print(f'''      ______________________
     |                      |
     | {colors['VERMELHO']} BOMBA DE ALTO RISCO - CÓDIGO SECRETO REQUERIDO {colors['BRANCO']} |
     |______________________|  ({self.number} segundos)''')

    def explosion(self):
        color_print("!!! BOOM !!!", "VERMELHO")
        color_print("A bomba explodiu... Missão fracassada.", "VERMELHO")

    def success(self):
        color_print("Desarmando...", "AZUL")
        time.sleep(self.number)
        color_print("✔ Bomba desarmada com sucesso!", "VERDE")

    def start(self):
        self.show_button()
        time.sleep(1)

        if self.number <= 3:
            color_print(f"Pressione o botão {self.number} vezes corretamente para desarmar!", "CIANO")
            for i in range(self.number):
                input(f"Pressione o botão #{i+1}\n> ")
                color_print("Clique registrado!", "AZUL")
            self.success()

        elif self.number == 4:
            color_print("Essa é uma TNT especial. Requer autenticação secreta!", "AMARELO")
            time.sleep(1)
            while True:
                resposta = input("Digite a senha secreta (nome da bomba + valor de Pi)\n> ").lower()
                if resposta == f"{self.bomb_name} 3.14":
                    color_print("Acesso concedido.", "VERDE")
                    self.success()
                    break
                else:
                    self.attempts += 1
                    color_print("Senha incorreta!", "VERMELHO")
                    if self.attempts >= 3:
                        self.explosion()
                        break

        else:
            color_print("Esta bomba requer um código secreto!", "VERMELHO")
            while True:
                try:
                    tentativa = int(input("Adivinhe o número secreto entre 1 e 10\n> "))
                except ValueError:
                    color_print("Entrada inválida! Digite um número.", "AMARELO")
                    continue

                if tentativa == self.secret_number:
                    color_print("Código aceito!", "VERDE")
                    self.success()
                    break
                else:
                    self.attempts += 1
                    color_print("Número incorreto!", "VERMELHO")
                    if self.attempts >= 5:
                        self.explosion()
                        break
