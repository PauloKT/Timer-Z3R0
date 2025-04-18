class cifradeCesar:
    def __init__(self, chave):
        self.chave = chave

    def decifrar(self, texto): 
        textoDecifrado = self.transformar(texto, self.chave)
        print(f"Texto descriptografado: {textoDecifrado}")

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