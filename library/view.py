import pygame
from pygame.locals import *

from library.board import *
from library.constantes import *
from library.move import checkMove


class Interface:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600,600), RESIZABLE)

        # We preload corresponding images for every type of items, floor, wall and characters. 
        self.sprites = {
            FLOOR: pygame.image.load('ressources/floor.png').convert_alpha(),
            WALL: pygame.image.load('ressources/wall.png').convert_alpha(),
            NEEDLE: pygame.image.load('ressources/aiguillem.png').convert_alpha(),
            PIPE: pygame.image.load('ressources/pipe.png').convert_alpha(),
            ETHER: pygame.image.load('ressources/ether.png').convert_alpha(),
            HEROS: pygame.image.load('ressources/MacGyver.png').convert_alpha(),
            GUARDIAN: pygame.image.load('ressources/Gardien.png').convert_alpha()
       }

        #We direction
        self.direction = {
            K_UP: 'K_UP',
            K_DOWN: 'K_DOWN',
            K_RIGHT: 'K_RIGHT',
            K_LEFT: 'K_LEFT'
       }

    def show_maze(self):
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                self.show_cell(cell, i, j)
        pygame.display.flip()

    def show_cell(self, cell, i, j):
        sprite = self.sprites[cell]
        if cell != WALL and cell != FLOOR:
            self.show_cell(FLOOR,i,j)
        self.window.blit(sprite, (40*j, 40*i))

    def run(self):
       
        while True:
            self.show_maze()
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = 0
                elif event.type == KEYDOWN:
                    checkMove(pygame.key.name(event.key))
