from random import randint
from time import sleep
from os import system

class cifradeCesar:
    def __init__(self):
        self.palavras_originais = ["bomba", "fiovermelho", "timerzero", "paulo", "guilherme", "fabinho", "dancarino", "emo", "katto", "café"]
        self.palavras_cifrada = []
        self.rotações = []
        self.gerar_cifras = ()

    def gerar_cifras(self):
        for palavras in self.palavras_originais:
            rotação = randint(1, 25)
            cifra = self.cifrar(palavras, rotação)
            self.palavras_cifrada.append(cifra)
            self.rotações.append(rotação)

    def transformar(self, texto, deslocamento):
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
    
chave = cifradeCesar()
mensagem_cifrada = ""
print("Use numeros negativos para decifrar")

chave.decifrar(mensagem_cifrada)