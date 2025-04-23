import random
import time
bomb_number=random.randint(1, 10)   
class Bomb:
    def __init__(self, text):
        self.text = text
        self.number = random.randint(1, 10)


    def press(self,):
     if self.number <3:
      print(f'''      ______________________
     |                      |
     |    PRESS TO DEFUSE   |
     |______________________|{self.number}''')
       
      



     elif self.number == 4:
      print(f'''      ______________________
     |                      |
     |  TWO CLICK TO DISARM |
     |______________________|{self.number}''')
      




     else:
      print(f'''      ______________________
     |                      |
     |    CLICK TO DISARM   |
     |______________________|{self.number}''')

class defuse(Bomb): 
    def __init__(self, text, number):
        super().__init__(text)
        self.text = text
        self.number = number
        

    def press(self):
        if self.number <= 3:
            click = str(input(f"Você precisa pressionar o botão {self.number} vezes: "))
            print(f"Pressione o botão por {self.number} vezes")
            time.sleep(self.number)
            print("Bomb defused!")

        elif self.number == 4:
            print(f"Você precisa pressionar o botão {self.number} vezes.")
            time.sleep(1)
            print("Cuidado, essa bomba é uma TNT específica e tem condições para desarmar.")
            
            # Certifique-se de que o while está dentro do método
            while True:
                click2 = input("Para desarmar, diga o nome da bomba e o valor de Pi: ")
                if click2.lower() == 'tnt 3.14':
                    print(f"Pressione o botão por {self.number} segundos.")
                    time.sleep(self.number)
                    print("Bomb defused!")
                    break
                else:
                    print("Resposta incorreta! Tente novamente.")


        else:
            print(f"Pressione o botão por {self.number} segundos.")
            print(f"amigo, esta bomba que encontraste é uma bomba especial. é necessario adivinhar um numero entre 1 e 10")
            while True:
                guess = int(input("Adivinhe o número entre 1 e 10: "))
                if guess == bomb_number:
                    print(f"Pressione o botão por {self.number} segundos.")
                    time.sleep(self.number)
                    print("Bomb defused!")
                    break
                else:
                    print("Número incorreto! Tente novamente.")
            



bomb=Bomb('bomb')
bomb.press()
bomb1=defuse('bomb',bomb.number)
bomb1.press()