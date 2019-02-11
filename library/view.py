import pygame
from pygame.locals import *

from library.config import FLOOR, HEROS, GUARDIAN, WALL, NEEDLE, PIPE, ETHER
from library.board import Game


class Interface:
    
    def __init__(self, game):
        self.game = game
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
        self.movement = {
            K_UP: 'UP',
            K_DOWN: 'DOWN',
            K_RIGHT: 'RIGHT',
            K_LEFT: 'LEFT'
       }

    def show_maze(self):
        for i, row in enumerate(self.game.maze):
            for j, cell in enumerate(row):
                self.show_cell(cell, i, j)
        

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
                    self.game.move_hero(self.movement[event.key])
            pygame.display.flip()
