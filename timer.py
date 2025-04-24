# O professor nao ensinou funções assincronas, entao nao tem como fazer um contador real (executar algo dentro de um for enquanto o resto do código roda junto)
# Logo, vamos fazer um contador falso xd

class Timer:
    def __init__(self, timer):
        self.timer = timer
        
    def printTime(self):
        print(f"Timer atual: {self.timer}")
        
    def removeTime(self, amount):
        newTime = self.timer - amount
        if newTime <= 0:
            print(f"O tempo foi excedido, a bomba equisplodiu\n")
        else:
            print(f"Foi removido 1 minuto da contagem da bomba\n")
            self.printTime()