from os import system, name 

def clear():
    system('cls' if name == 'nt' else 'clear')