# O professor nao ensinou funções assincronas, entao nao tem como fazer um contador real (executar algo dentro de um for enquanto o resto do código roda junto)
# Logo, vamos fazer um contador falso xd

class Timer:
    def __init__(self, timer):
        self.timer = timer

    def printTime(self):
        print(f"Timer atual: {self.timer/60}m")
        
    def removeTime(self, amount):
        newTime = self.timer - amount
        if newTime <= 0:
            print(f"O tempo foi excedido.\n")
            self.timer = 0
            return True
        else:
            print(f"Foi removido {amount/60}m do tempo da bomba\n")
            self.printTime()
            self.timer = newTime
            return False