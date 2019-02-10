#! /usr/bin/env python3
# coding:utf-8

from library.view import Interface
from library.board import initMaze

def main():
    initMaze()
    gui = Interface()
    gui.run()


if __name__ == "__main__":
    main()
