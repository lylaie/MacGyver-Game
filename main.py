#! /usr/bin/env python3
# coding:utf-8

"""
    Interface is the class to run the view
    Game is the class to create the board
"""

from library.interface import Interface
from library.game import Game

def main():

    """
        Calls the function who generates the board and runs the game
    """
    game = Game()
    gui = Interface(game)
    gui.run()


if __name__ == "__main__":
    main()
