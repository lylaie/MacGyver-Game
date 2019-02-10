from library.constantes import directions

def checkPosition(next_line, next_column):
    if 0 <= next_column <= 14 and 0 <= next_line <= 14:
        if maze[next_column][next_line] == 'o':
            return True
        if maze[column][line] == 'G':
            print('Fin du game')
            return True
        if maze[column][line] == 'M':
            print('Mur!')
            return False
        else:
            print("Vous avez trouvé un objet")
            return True

def checkMove(eventKeyName): 
    direction = directions[eventKeyName]
    print(direction)
    authorization = checkPosition(position_heros[0] + direction[0], position_heros[1] + direction[1])
    if authorization:
        position_heros = position_heros.move(direction)
        return position_heros
    else:
        print("Unauthorized move")
        return position_heros


