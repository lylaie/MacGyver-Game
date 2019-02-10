def valueCouple(coordonatesList, character, value):
   index_line = 0
   for row in maze:
        index_column = 0
        for column in row:
            if column == character:
                coordonatesList.append((index_line, index_column))
                value += 1
            index_column +=1
        index_line += 1
   return value









empty_cells = []
wall_cells = []

def viewFloor(fondImage, character,typeCells):
    index = 0
    counter = valueCouple(typeCells, character,counterI)
    fondURL = str(fondImage)
    fond = pygame.image.load(fondURL).convert_alpha()
    while index < counter:
        windows.blit(fond, (typeCells[index][1]*40, typeCells[index][0]*40))
        index +=1
   

viewFloor("ressources/floor.png", 'o', empty_cells)
viewFloor("ressources/wall.png", 'M', wall_cells)



def checkPositionHero(line, column):
    if 0 <= column <= 14 and 0 <= line <= 14:
        if maze[column][line] == 0:
            return True
        if maze[column][line] == 2:
            print("Vous avez trouvé un objet")
            return True
        if maze[column][line] == 'G':
            print('Fin du game')
            return True
    else:
        return False

def left_move(position_heros):
    authorization = checkPositionHero(position_heros[0]-1, position_heros[1])
    if authorization == True:
        position_heros = position_heros.move(-1,0)
        return position_heros
    else:
        print('mouvement impossible')
    return position_heros

def right_move(position_heros):
    authorization = checkPositionHero(position_heros[0]+1, position_heros[1])
    if authorization == True:
        position_heros = position_heros.move(1,0)
        print(position_heros)
    else:
        print('mouvement impossible')
    return position_heros

def up_move(position_heros):
    authorization = checkPositionHero(position_heros[0],position_heros[1]-1)
    if authorization == True:
        position_heros = position_heros.move(0,-1)
    else:
        print('mouvement impossible')
    return position_heros

def down_move(position_heros):
    authorization = checkPositionHero(position_heros[0], position_heros[1]+1)
    if authorization == True:
        position_heros = position_heros.move(0,1)
    else:
        print('mouvement impossible')
    return position_heros
