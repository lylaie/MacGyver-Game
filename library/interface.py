import pygame as pg

from library.config import FLOOR, HEROS, GUARDIAN, WALL, NEEDLE, PIPE, ETHER



class Interface:
    """
        Control the view of the game using pygame
    """

    def __init__(self, game):

        """
            Initializes the game.
        """
        self.game = game

        pg.init()
        self.window = pg.display.set_mode((680, 600))
        self.window.fill((230, 230, 230))
        pg.display.set_caption("MacGseyver Escape")

        # We preload corresponding images for every type of items, floor, wall and characters.
        self.sprites = {
            FLOOR: pg.image.load('ressources/floor.png').convert_alpha(),
            WALL: pg.image.load('ressources/wall.png').convert_alpha(),
            NEEDLE: pg.image.load('ressources/aiguillem.png').convert_alpha(),
            PIPE: pg.image.load('ressources/pipe.png').convert_alpha(),
            ETHER: pg.image.load('ressources/ether.png').convert_alpha(),
            HEROS: pg.image.load('ressources/MacGyver.png').convert_alpha(),
            GUARDIAN: pg.image.load('ressources/Gardien.png').convert_alpha()
        }

        #We direction
        self.movement = {
            pg.K_UP: 'UP',
            pg.K_DOWN: 'DOWN',
            pg.K_RIGHT: 'RIGHT',
            pg.K_LEFT: 'LEFT'
        }

    def show_maze(self):
        """
            Show the labyrinth
        """
        for i, row in enumerate(self.game.maze):
            for j, cell in enumerate(row):
                self.show_cell(cell, i, j)
        
    def show_cell(self, cell, i, j):
        """
            Print the image corresponding to the cell at the given coordinates
        """
        sprite = self.sprites[cell]
        if cell not in (WALL, FLOOR):
            self.show_cell(FLOOR, i, j)
        self.window.blit(sprite, (40*j, 40*i))

    def run(self):
        """
            Loop to run and refresh the view of the game
        """
        runing = True
        while runing:
            self.show_maze()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    runing = False
                elif event.type == pg.KEYDOWN:
                    if event.key in self.movement:
                        self.game.move_hero(self.movement[event.key])
                    elif event.key == pg.K_q:
                        exit(0)

            pg.display.flip()
