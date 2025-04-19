from bomb import Bomb
from utils.helpers import clear
from time import sleep

if __name__ == "__main__":
    clear()
    print("Bem-vindo ao Timer-Z3R0!")
    while True:
        bomb = Bomb(debugMode=True)
        bomb.start()
        print("Parabéns! Você desarmou a bomba!")
        sleep(1)