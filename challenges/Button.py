import random
import time

class ButtonChallenge:
    def __init__(self):
        self.number = random.randint(1, 10)
        self.bomb_name = "TNT"
        self.secret_number = random.randint(1, 10)

    def show_button(self):
        print("\n--- DESAFIO DO BOTÃO ---")
        if self.number < 3:
            print(f'''      ______________________
     |                      |
     |    PRESS TO DEFUSE   |
     |______________________|  ({self.number} vezes)''')

        elif self.number == 4:
            print(f'''      ______________________
     |                      |
     |  TWO CLICK TO DISARM |
     |______________________|  ({self.number} vezes)''')

        else:
            print(f'''      ______________________
     |                      |
     |    CLICK TO DISARM   |
     |______________________|  ({self.number} segundos)''')

    def start(self):
        self.show_button()

        if self.number <= 3:
            print(f"Você precisa pressionar o botão {self.number} vezes.")
            time.sleep(self.number)
            print("Bomba desarmada!")

        elif self.number == 4:
            print(f"Você precisa pressionar o botão {self.number} vezes.")
            time.sleep(1)
            print("Essa bomba é uma TNT especial, ela exige uma frase secreta!")

            while True:
                resposta = input("Digite o nome da bomba e o valor de Pi (ex: TNT 3.14): ").strip().lower()
                if resposta == "tnt 3.14":
                    print(f"Pressione o botão por {self.number} segundos.")
                    time.sleep(self.number)
                    print("Bomba desarmada!")
                    break
                else:
                    print("Frase incorreta! Tente novamente.")

        else:
            print(f"Essa é uma bomba especial. Tente adivinhar o número secreto entre 1 e 10.")
            while True:
                tentativa = int(input("Adivinhe o número: "))
                if tentativa == self.secret_number:
                    print(f"Pressione o botão por {self.number} segundos.")
                    time.sleep(self.number)
                    print("Bomba desarmada!")
                    break
                else:
                    print("Número incorreto! Tente novamente.")