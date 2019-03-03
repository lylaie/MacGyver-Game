import os


"""
    Constantes whom can be easily change by a user.
    Here you are the original maze, the initial position of the hero and the guardian.
    The visual notation of each items are defined here.
"""


HEROS = 'H'
GUARDIAN = 'G'
NEEDLE = 'N'
PIPE = 'P'
ETHER = 'E'
WALL = 'M'
FLOOR = 'o'


def launch_analysis(data_file):
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, 'data', data_file)
    
    with open(path_to_file, 'r') as f:
        preview = f.readline()
        maze = []
        j = 0
        while preview:
            current_line = []
            for i, character in enumerate(preview):
                if character == ' ':
                    current_line.append(FLOOR)
                elif character == '#':
                    current_line.append(WALL)
                elif character == 'H':
                    ini_hero = (i-1,j-1)
                    current_line.append(character)
                elif character == 'G':
                    guardian = (i-1, j-1)
                    current_line.append(character)
                else:
                   pass
            if current_line:
                maze.append(current_line)
            preview = f.readline()
            j += 1
            
    return maze, ini_hero, guardian


MAZE, INI_HERO, LOC_GUARDIAN = launch_analysis('maze1.txt')

print(MAZE)
print(INI_HERO)
print(GUARDIAN)
