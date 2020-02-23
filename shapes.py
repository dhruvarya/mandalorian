from colorama import Fore

def player_shape():
    return [[Fore.WHITE + "<", "@", ">"], [ Fore.WHITE + "/", "|", "\\"], [Fore.WHITE + "/", " ", "\\"]]

def gg1_shape():
    return [[Fore.BLUE + "Z"] * 174] * 5

def gg2_shape():
    return [[Fore.BLUE + "Z"] * 150] * 4

def gg2_down_shape():
    return [[Fore.BLUE + "Z"] * 174]

def score_shape():
    return [["S", "C", "O", "R", "E", ":", " ", "-", "-", "-"]]

def timer_shape():
    return [["T", "I", "M", "E", "R", ":", " ", "-", "-", "-"]]

def lives_shape():
    return [["L", "I", "v", "E", "S", ":", " ", "-", "-", "-"]]

def coin_shape():
    return [[Fore.YELLOW + "C"]]

def obstacle_shape():
    return [[Fore.RED + "O"]]

def hlines_shape():
    return [[Fore.RED + "O"] * 10]

def vlines_shape():
    return [[Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"], [Fore.RED + "O"]]

def gun_shape():
    return [[Fore.WHITE + "-", "-", ">"]]

def gun_l_shape():
    return [[Fore.RED + "<", "-", "-"]]

def magnet_shape():
    return [[Fore.RED + "m",Fore.WHITE + "m",Fore.BLUE + "m"]]

def powerup_shape():
    return [[Fore.GREEN + "(", "P", ")"]]

def dragon_shape():
    return [[Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ',', '=', '=', '=', ':', "'", '.', ',', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '-', '.', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', ':', '.', '`', '-', '-', '-', '.', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '-', '.', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', ':', '.', ' ', ' ', ' ', ' ', ' ', '`', '-', '-', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', '(', ',', ',', '(', ',', ' ', ' ', ' ', ' ', '\\', '\\', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', '_', '_', '_', '_', ',', '-', '`', '.', ','], [Fore.RED + ' ', ' ', ' ', ' ', '(', ',', "'", ' ', ' ', ' ', ' ', ' ', '`', '/', ' ', ' ', ' ', '\\', '\\', '.', ' ', ' ', ' ', ',', '-', '-', '.', '_', '_', '_', '`', '.', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ',', ' ', ' ', ',', "'", ' ', ' ', ',', '-', '-', '.', ' ', ' ', '`', ',', ' ', ' ', ' ', '\\', '\\', '.', ';', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', '`', '{', 'D', ',', ' ', '{', ' ', ' ', ' ', ' ', '\\', '\\', ' ', ' ', ':', ' ', ' ', ' ', ' ', '\\', '\\', ';', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', 'V', ',', ',', "'", ' ', ' ', ' ', ' ', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', '/', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', 'j', ';', ';', ' ', ' ', ' ', ' ', '/', ' ', ' ', ',', "'", ' ', ',', '-', '/', '/', '.', ' ', ' ', ' ', ' ', ',', '-', '-', '-', '.', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', '\\', '\\', ';', "'", ' ', ' ', ' ', '/', ' ', ' ', ',', "'", ' ', '/', ' ', ' ', '_', ' ', ' ', '\\', '\\', ' ', ' ', '/', ' ', ' ', '_', ' ', ' ', '\\', '\\', ' ', ' ', ' ', ',', "'", '/', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '\\', ' ', ' ', ' ', '`', "'", ' ', ' ', '/', ' ', '\\', '\\', ' ', ' ', '`', "'", ' ', ' ', '/', ' ', '\\', '\\', ' ', ' ', '`', '.', "'", ' ', '/', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '.', '_', '_', '_', ',', "'", ' ', ' ', ' ', '`', '.', '_', '_', ',', "'", ' ', ' ', ' ', '`', '.', '_', '_', ',', "'", ' ', ' ', ' ', ' ', ' ', ' ']]

def slant_obstacle_shape():
    return [[Fore.RED + 'o', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', 'o', 'o', ' ', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', 'o', 'o', ' ', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', 'o', 'o', ' ', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', 'o', 'o', ' ', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', ' '], [Fore.RED + ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o']]

def game_over():
    return [[' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', '.', '_', '_', '_', ' ', ' ', '_', '_', '_', '.', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', '_', '_', '_', '_', ' ', ' ', ' ', ' ', '_', '_', '_', '_', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', '.', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' '], [' ', '/', ' ', ' ', '_', '_', '_', '_', '_', '|', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\\', '/', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', '_', '_', '_', '_', '|', ' ', ' ', ' ', ' ', '/', ' ', ' ', '_', '_', ' ', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', '|', ' ', ' ', ' ', '_', '_', '_', '_', '|', '|', ' ', ' ', ' ', '_', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '], ['|', ' ', ' ', '|', ' ', ' ', '_', '_', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', '^', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '|', ' ', ' ', '\\', ' ', ' ', '/', ' ', ' ', '|', ' ', '|', ' ', ' ', '|', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '\\', ' ', ' ', ' ', '\\', '/', ' ', ' ', ' ', '/', ' ', ' ', '|', ' ', ' ', '|', '_', '_', ' ', ' ', ' ', '|', ' ', ' ', '|', '_', ')', ' ', ' ', '|', ' ', ' ', ' ', ' '], ['|', ' ', ' ', '|', ' ', '|', '_', ' ', '|', ' ', ' ', ' ', '/', ' ', ' ', '/', '_', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '|', ' ', ' ', '|', '\\', '/', '|', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', '_', '_', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '|', ' ', ' ', ' ', '_', '_', '|', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' '], ['|', ' ', ' ', '|', '_', '_', '|', ' ', '|', ' ', ' ', '/', ' ', ' ', '_', '_', '_', '_', '_', ' ', ' ', '\\', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', ' ', '|', '_', '_', '_', '_', ' ', ' ', ' ', ' ', '|', ' ', ' ', '`', '-', '-', "'", ' ', ' ', '|', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', '_', '_', '_', '_', ' ', '|', ' ', ' ', '|', '\\', ' ', ' ', '\\', '-', '-', '-', '-', '.'], [' ', '\\', '_', '_', '_', '_', '_', '_', '|', ' ', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', '\\', '_', '_', '\\', ' ', '|', '_', '_', '|', ' ', ' ', '|', '_', '_', '|', ' ', '|', '_', '_', '_', '_', '_', '_', '_', '|', ' ', ' ', ' ', ' ', '\\', '_', '_', '_', '_', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', '|', '_', '_', '_', '_', '_', '_', '_', '|', '|', ' ', '_', '|', ' ', '`', '.', '_', '_', '_', '_', '_', '|'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
