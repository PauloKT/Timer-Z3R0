colors = {
    'VERDE': '\033[92m',
    'AZUL': '\033[94m',
    'AMARELO': '\033[93m',
    'VERMELHO': '\033[91m',
    'ROXO': '\033[95m',
    'CIANO': '\033[96m',
    'BRANCO': '\033[0m',
    'PRETO': '\033[90m',
    'NEGRITO': '\033[1m',
    'SUBLINHADO': '\033[4m',
}

def color_print(text, color_name='BRANCO', bold=False):
    prefix = colors[color_name]
    if bold:
        prefix += colors['NEGRITO']
    print(f"{prefix}{text}{colors['BRANCO']}")