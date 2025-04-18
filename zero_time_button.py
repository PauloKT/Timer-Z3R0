import random
import time

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
    def __init__(self,text,number):
        super().__init__(text)
        self.text = text
        self.number = number
        print(f"Random number reused: {self.number}")


    def press(self):
        if self.number == 2:
         click=str(input(f"voce precisa pressionar o botão {self.number} vezes"))
         print(f"Pressione o botão por {self.number} vezes")
         time.sleep(self.number)
         print("Bomb defused!")


        elif self.number > 4:
            print("Bomb defused!")
        else:
            print("Bomb exploded!")


bomb=Bomb('bomb')
bomb.press()
bomb1=defuse('bomb',bomb.number)
bomb1.press()