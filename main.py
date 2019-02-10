#! /usr/bin/env python3
# coding:utf-8

from library.view import runView
from library.board import initMaze

def main():
    initMaze()
    runView()


if __name__ == "__main__":
    main()
