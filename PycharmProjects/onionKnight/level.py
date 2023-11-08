import pygame
from settings import *
from tile import *
from player import Player
class Level:
    def __init__(self):
        #get display
        self.display_surface = pygame.display.get_surface()

        # sprites setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for y_index, y in enumerate(WORLD_MAP):
            for x_index, x in enumerate(y):
                x_screen = x_index * TILESIZE
                y_screen = y_index * TILESIZE
                if x == 'x':
                    Tile((x_screen, y_screen),[self.visible_sprites])
                if x == 'p':
                    Player((x_screen,y_screen), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        pass
