# Essa é a classe base para os desafios, que será herdada por cada desafio específico

class BaseChallenge:
    def __init__(self):
        self.completed = False  # Indica se o desafio foi concluído

    def start(self):
        """Método principal para iniciar o desafio."""
        raise NotImplementedError("O método 'start' deve ser implementado pela subclasse.")