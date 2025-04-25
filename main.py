# Dev's
# Paulo Henrique Amaral Martins
# Fabio Henrique Massucatto Sousa
# José Guilherme Oliveira Martins



from bomb import Bomb
from utils.helpers import clear
from utils.colors import colors, color_print
from time import sleep

from artes.artes_timerZ3R0 import arte_timer_z3r0

if __name__ == "__main__":
    clear()

    split_index = 40

    color_print("Bem-vindo ao", "NEGRITO")

    for line in arte_timer_z3r0.strip().split("\n"):
        timer_part = line[:split_index]
        z3r0_part = line[split_index:]
        print(f"{colors["VERMELHO"]}{timer_part}{colors["BRANCO"]}{z3r0_part}")
    
    color_print("Envie qualquer coisa para começar o jogo", "AMARELO")
    input("> ")
    clear()

    color_print("Armando bomba...", "VERMELHO", True)
    sleep(1)
    
    bomb = Bomb()
    bomb.start()