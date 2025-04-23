from random import randint
from time import sleep
from utils.helpers import clear

class cifradeCesar:
    def __init__(self):
        self.palavras_originais = ["bomba", "katto", "banguela", "gatão", "dancarino", "fiovermelho", "timerzero"]
        self.palavras_cifradas = []
        self.rotações = []

    def start(self):
        clear()

        self.gerar_cifras()
        tempo_bomba = 10
        erros = 0

        i = randint(0, 7)
        print(i, self.palavras_cifradas)
        palavra_cifrada = self.palavras_cifradas[i]
        rotacao_correta = self.rotações[i]

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

            print(tentativa, rotacao_correta)
            if tentativa == rotacao_correta:
                print(f"\nSucesso! A rotação correta er {rotacao_correta}")
                break
            else:
                erros += 1
                distancia = tentativa - rotacao_correta

                print(distancia)

                if distancia > 10 or distancia < -10:
                    print("Você está MUITO longe do numero certo!\n")
                elif distancia > 7 or distancia < -7:
                    print("Você está quase chegando no numero correto!\n")
                elif distancia > 4 or distancia < -4:
                    print("Você está MUITO perto do numero certo!\n")
                elif distancia == 1 or distancia == -1:
                    print("VOCÊ TA LITERALMENTE DO LADO DO NUMERO CERTO!!!\n")

                if erros % 3 == 0:
                    tempo_bomba -= 1
                    print(f"Você perdeu 1 minuto! Tempo restante {tempo_bomba} min.")
                    if tempo_bomba <= 0:
                        print("O tempo acabou!")
                        break
                    sleep(1)

                print("Você errou!\n")

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