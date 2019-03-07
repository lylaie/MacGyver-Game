"""
    Random library to generate the position of the items
"""

import sys

from random import randint

from library.config import *

class Game:
    """
        Model the maze, the items and characters.
    """
    DIRECTIONS = {
        'UP': (0, -1),
        'DOWN' : (0, 1),
        'RIGHT': (1, 0),
        'LEFT': (-1, 0)
    }

    def __init__(self):
        """
            Initialize the data of the maze.
            The three objects (needle, plastic_pipe and ether) are created and placed on
            the board.
            You can change here the starting position of the heros and the guardian'emplacement.
        """
        self.maze = MAZE

        self.hero_loc = INI_HERO

        self.choose_place(NEEDLE)
        self.choose_place(PIPE)
        self.choose_place(ETHER)

        self.counter_items = 0
        self.list_objects = []

        self.okay = 0

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

    def choose_place(self, item):
        """
            Computes a random abscissa and a random ordonate in relation
            to the free position in the maze. The free positions are the whole position
            without wall, objects or start and end point.
        """

        row = randint(0, 14)
        column = randint(0, 14)
        print(row, column)
        while self.maze[row][column] != FLOOR:
            row = randint(0, 14)
            column = randint(0, 14)
            print(row, column)
        self.maze[row][column] = item
        return row, column

    def check_position(self, line, column):
        """
            Check the value of the next position in the Maze.
            If the value is FLOOR, the function returns True.
            If the value is WALL, the function returns False.
            If the value is NEEDLE, PIPE or ETHER, the function returns True
            and increases the counter_items of 1.
            If the value is GUARDIAN, the function checks the value of counter_items.
            If the counter_items is different to 3, the function returns False and GameOver
            If the counter_items equals to 3, the function returns True and prints 'You win!'

        """
        if 0 <= column <= 14 and 0 <= line <= 14:
            if self.maze[line][column] == FLOOR:
                return True
            elif self.maze[line][column] == GUARDIAN:
                if self.counter_items != 3:
                    print('Game Over')
                    self.okay = 1
                    return False
                self.okay = 2
                return True
            elif self.maze[line][column] == WALL:
                return False
            self.counter_items += 1
            self.list_objects.append(self.maze[line][column])
            return True
        return False

    def move_hero(self, keyaction):
        """
            Check the next position and if the movement is authorized or not. If it is,
            return the new value of the hero position, changes the value of floor and ini_hero
            in the maze.
        """
        direction = self.DIRECTIONS[keyaction]
        new_hero_line = self.hero_loc[0] + direction[1]
        new_hero_column = self.hero_loc[1] + direction[0]
        new_hero_loc = (new_hero_line, new_hero_column)
        authorization = self.check_position(new_hero_line, new_hero_column)
        if authorization:
            self.maze[self.hero_loc[0]][self.hero_loc[1]] = FLOOR
            self.maze[new_hero_line][new_hero_column] = HEROS
            self.hero_loc = (new_hero_line, new_hero_column)
        else:
            print("Unauthorized move")
