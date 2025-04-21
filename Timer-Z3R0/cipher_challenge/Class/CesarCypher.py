from random import randint

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