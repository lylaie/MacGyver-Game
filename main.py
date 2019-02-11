#! /usr/bin/env python3
# coding:utf-8

from library.view import Interface
from library.board import Game

def main():
    game = Game()
    gui = Interface(game)
    gui.run()


if __name__ == "__main__":
    main()
