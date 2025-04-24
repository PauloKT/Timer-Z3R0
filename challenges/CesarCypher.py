from random import randint
from time import sleep
from utils.helpers import clear
from utils.colors import colors, color_print

class CesarCypherChallenge:
    def __init__(self, bomb):
        self.bomb = bomb
        self.palavras_originais = ["bomba", "katto", "banguela", "gatão", "dancarino", "fiovermelho", "timerzero"]
        self.palavras_cifradas = []
        self.rotações = []

    def start(self):
        
        clear()
        self.gerar_cifras()
        tempo_bomba = 10

        i = randint(0, len(self.palavras_originais) - 1)
        palavra_cifrada = self.palavras_cifradas[i]
        rotacao_correta = self.rotações[i]
        
        color_print(f"\n🔐 Cifra recebida: {palavra_cifrada}", 'AMARELO', True)
        color_print("🔎 Descubra a rotação correta (1 a 25)", 'AZUL')
        color_print("⚠️  A cada erro, 1 minuto será perdido!", 'VERMELHO')
        color_print("===========================================\n", 'CIANO')

        while True:
            
            tentativa = input(f"{colors['NEGRITO']}Digite o número de rotações: {colors['BRANCO']}\n> ")
            if not tentativa.isdigit():
                color_print("❗Digite um número válido!\n", 'VERMELHO')
                continue

            tentativa = int(tentativa)

            if tentativa < 1 or tentativa > 25:
                color_print("⛔ Número fora do intervalo (1 a 25)!\n", 'VERMELHO')
                continue
            clear()

            palavra_tentativa = self.cifrar(palavra_cifrada, -tentativa)
            color_print(f"🧠 Descriptografado com rotação {tentativa}: {palavra_tentativa}", 'CIANO')
            color_print(f"\🔐 Cifra recebida: {palavra_cifrada}", 'AMARELO', True)
            color_print("🔎 Descubra a rotação correta (1 a 25)", 'AZUL')
            color_print("⚠️  A cada erro, 1 minuto será perdido!", 'VERMELHO')
            color_print("===========================================\n", 'CIANO')

            if tentativa == rotacao_correta:
                color_print(f"\n✅ Sucesso! A rotação correta era {rotacao_correta}.", 'VERDE', True)
                sleep(5)
                break
            else:
                tempo_bomba -= 1
                distancia = abs(tentativa - rotacao_correta)

                color_print("\n❌ Rotação incorreta!", 'VERMELHO')
                color_print(f"💣 Tempo restante: {tempo_bomba} minuto(s)", 'AMARELO')

                if tempo_bomba <= 0:
                    color_print("💥 O tempo acabou! A bomba explodiu!", 'VERMELHO', True)
                    break

                if distancia >= 10:
                    color_print("📉 Você está MUITO longe da rotação correta!\n", 'VERMELHO')
                elif 6 <= distancia <= 9:
                    color_print("🔍 Você está chegando perto!\n", 'AMARELO')
                elif 2 <= distancia <= 5:
                    color_print("🔥 Muito perto!\n", 'CIANO')
                elif distancia == 1:
                    color_print("🚨 VOCÊ ESTÁ DO LADO DA RESPOSTA CERTA!!!\n", 'VERDE')

                sleep(1)


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