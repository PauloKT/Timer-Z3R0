colors = {
    'GREEN': '\033[92m',
    'BLUE': '\033[94m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[0m',
    'BLACK': '\033[90m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
}

color_list = []

for key, value in colors.items():
    color_dict = {
        'name': key,
        'code': value
    }
    color_list.append(color_dict)
