from Class.CesarCypher import cifradeCesar
from os import system
from time import sleep

def limpar_tela():
    system('cls')

def iniciar_jogo():
    system('cls')
    cifra = cifradeCesar()
    tempo_bomba = 10
    erros = 0

    i = randint(0, 9)
    palavra_cifrada = cifra.palavras_cifradas[i]
    rotacao_correta = cifra.rotação[i]

    print("========= TIMER Z3R0 =========")
    print(f"\nA cifra é : {palavra_cifrada}")
    print("Você precisa descobrir a rotção correta de 1 a 25")
    print("A cada erro 3 erros, 1 minuto será removido do tempo da bomba")
    print("==============================\n")

    while True:
        tentativa =  input("Digite o numero de rotações: ")
        tentativa = int(tentativa)

        if tentativa < 1 or tentativa > 25:
            print("Digite um número válido!\n")

        if tentativa == rotacao_correta:
            print(f"\nSucesso! A rotação correta er {rotacao_correta}")
            break
        else:
            erros += 1
            distancia = tentativa - rotacao_correta

            if distancia > 10 or distancia < -10:
                print("Você está MUITO longe do numero certo!\n")
            elif distancia > 7 or distancia < -7:
                print("Você está quase chegando no numero correto!\n")
            elif distancia > 4 or distancia < -4:
                print("Você está MUITO perto do numero certo!\n")
            elif distancia > 1 or distancia < -1:
                print("VOCÊ TA LITERALMENTE DO LADO DO NUMERO CERTO!!!\n")

            if erros % 3 == 0:
                tempo_bomba -= 1
                print(f"Você perdeu 1 minuto! Tempo restante {tempo_bomba} min.")
                if tempo_bomba <= 0:
                    print("O tempo acabou!")
                    break
                sleep(1)

            print("Você errou!\n")

iniciar_jogo()