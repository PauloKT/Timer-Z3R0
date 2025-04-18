colors = {
    'VERDE': '\033[92m',
    'AZUL': '\033[94m',
    'AMARELO': '\033[93m',
    'VERMELHO': '\033[91m',
    'MAGENTA': '\033[95m',
    'CIANO': '\033[96m',
    'BRANCO': '\033[0m',
    'PRETO': '\033[90m',
    'NEGRITO': '\033[1m',
    'SUBLINHADO': '\033[4m',
}

def color_print(text, color_name):
    print(f"{colors[color_name]}{text}{colors["BRANCO"]}")