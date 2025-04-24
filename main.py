from bomb import Bomb
from utils.helpers import clear
from time import sleep

from artes.artes_timerZ3R0 import arte_timer_z3r0

if __name__ == "__main__":
    clear()
    print(f"Bem-vindo ao\n{arte_timer_z3r0}")
    
    input("Envie qualquer caractere para começar o desafio")
    
    bomb = Bomb()
    sucesso = bomb.start()
    
    if sucesso:
        print("Parabéns! Você desarmou a bomba!")
    else:
        print("Deu ruim pae")