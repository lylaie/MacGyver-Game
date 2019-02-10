import pygame
from pygame.locals import *
from library.board import *
from library.constantes import *

def showMaze(sprites):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            showCell(cell, i, j, sprites)

def showCell(cell, i, j, sprites):
    sprite = sprites[cell]
    if cell != WALL and cell != FLOOR:
        showCell(FLOOR,i,j, sprites)
    windows.blit(sprite, (40*j, 40*i))


def runView():
    pygame.init()
    global windows 
    windows = pygame.display.set_mode((600, 600), RESIZABLE)


    sprites = constantes.sprites


    
    showMaze(sprites)


    pygame.display.flip()

    run = 1
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
            elif event.type == KEYDOWN:
                checkKey(event.key)
               
        showMaze(sprites)
        pygame.display.flip()
