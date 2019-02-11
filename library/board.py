from random import randint 

from library.config import *

class Game:
   
    directions = {
        'UP': (0,-1),
        'DOWN' : (0,1),
        'RIGHT': (1,0),
        'LEFT': (-1,0)
    }

    def __init__(self):
        """
            Initialize the data of the maze.
            The three objects (needle, plastic_pipe and ether) are created and placed on
            the board.
            You can change here the starting position of the heros and the emplacement of the guardian.
        """
        self.maze = maze

        self.hero_loc = INI_HERO
        self.maze[INI_HERO[0]][INI_HERO[1]] = HEROS
        self.maze[LOC_GUARDIAN[0]][LOC_GUARDIAN[1]] = GUARDIAN

        self.choose_place(NEEDLE)
        self.choose_place(PIPE)
        self.choose_place(ETHER)

        self.print_maze()
        
    def print_maze(self):
        """
            Print the Maze in the console.
            Using to develop the program and compare the pygame view
            with the encoded maze
        """

        for row in self.maze:
            for column in row:
                print(column, end=' ')
            print()


    def choose_place(self,item):
        """
            Computes a random abscissa and a random ordonate in relation
            to the free position in the maze. The free positions are the whole position
            without wall, objects or start and end point.
        """

        row = randint(0,14)
        column = randint(0,14)
        print(row, column)

        while self.maze[row][column] != FLOOR:
            print('Bad choice')
            row = randint(0,14)
            column = randint(0,14)
            print(row, column)

        print('Empty place')
        self.maze[row][column] = item
        return row,column

    def check_position(self, line, column):
        if 0 <= column <= 14 and 0 <= line <= 14:
            if maze[line][column] == FLOOR:
                return True
            if maze[line][column] == GUARDIAN:
                print('Fin du game')
                return True
            if maze[line][column] == WALL:
                print('Mur!')
                return False
            else:
                print("Vous avez trouvé un objet")
                return True

   
    def move_hero(self,keyaction):
        direction = self.directions[keyaction]
        print(keyaction, direction)
        new_hero_line = self.hero_loc[0] + direction[1]
        new_hero_column = self.hero_loc[1] + direction[0]
        new_hero_loc = (new_hero_line, new_hero_column)
        print(new_hero_loc)
        authorization = self.check_position(new_hero_line,new_hero_column )
        if authorization:
            self.maze[self.hero_loc[0]][self.hero_loc[1]] = FLOOR
            self.maze[new_hero_line][new_hero_column] = HEROS
            self.hero_loc = (new_hero_line,new_hero_column)
        else:
            print("Unauthorized move")
        
      
        
    
