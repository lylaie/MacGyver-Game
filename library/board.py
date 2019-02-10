from random import randint 

from library.constantes import *

class Board:
   
    def __init__(self):
        


    def printMaze():
        """
            Fonction whom print the Maze in the console.
            Using to develop the program and compare the pygame view
            with the encoded maze
        """

        for row in maze:
            for column in row:
                print(column, end=' ')
            print()


    def choosePlace(character):
        """
            choosePlace() calculates a random abscissa and a random ordonate in relation
            to the free position in the maze. The free positions are the whole position
            without wall, objects or start and end point.
        """

        abs = randint(0,14)
        ord = randint(0,14)
        print(abs, ord)

        while maze[abs][ord] != FLOOR:
            print('Bad choice')
            abs = randint(0,14)
            ord = randint(0,14)
            print(abs, ord)

        print('Empty place')
        maze[abs][ord] = character
        return abs,ord


    def initMaze():
        """
            The function initMaze() initialize the data of the maze.
            The three objects (needle, plastic_pipe and ether) are created and placed on
            the board.
            You can change here the starting position of the heros and the emplacement of the guardian.
        """

        needle = choosePlace(NEEDLE)
        plastic_pipe = choosePlace(PIPE)
        ether = choosePlace(ETHER)

        maze[position_heros[0]][position_heros[1]] = HEROS
        maze[position_guardian[0]][position_guardian[1]] = GUARDIAN

        maze
        printMaze()
