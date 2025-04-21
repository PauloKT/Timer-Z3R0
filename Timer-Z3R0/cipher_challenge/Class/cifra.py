from random import randint
from time import sleep
from os import system

class cifradeCesar:
    def __init__(self):
        self.palavras_originais = ["bomba", "katto", "banguela", "gatão", "dancarino", "fiovermelho", "timerzero"]
        self.palavras_cifradas = []
        self.rotações = []
        self.gerar_cifras()

    def gerar_cifras(self):
        for palavra in self.palavras_originais:
             rotação = randint(1, 25)
             cifra = self.cifrar(palavra, rotação)
             self.palavras_cifradas.append(cifra)
             self.rotações.append(rotação)

    def cifrar(self, texto, deslocamento):
        resultado = ''
        for char in texto:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
                codigo = ord(char) + deslocamento
                if char.islower() and codigo > ord('z'):
                    codigo -= 26
                elif char.isupper() and codigo > ord('Z'):
                    codigo -= 26
                elif char.islower() and codigo < ord('a'):
                    codigo += 26
                elif char.isupper() and codigo < ord('A'):
                    codigo += 26
                resultado += chr(codigo)
            else:
                resultado += char
        return resultado
    
def iniciar_jogo():
    system('cls')
    cifra = cifradeCesar
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

    if tentativa < 1 or tentativa > 25:
        print("Digite um número válido!\n")

    tentativa = int(tentativa)

    if tentativa == rotacao_correta:
        print(f"\nSucesso! A rotação correta er {rotacao_correta}")
        break
    else:
        erros += 1
        print("Você errou!\n")
        if erros % 3 == 0:
            tempo_bomba -= 1
            print(f"Você perdeu 1 minuto! Tempo restante {tempo_bomba} min.")
            if tempo_bomba <= 0:
                print("O tempo acabou!")