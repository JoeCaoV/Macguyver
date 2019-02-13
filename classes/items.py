import random
import os
import pygame.image
from config import IMG_PATH

class Item():
    """This class create a item, and generate randomly his position."""

    def __init__(self, name, img, mapping):
        """create the item and his position"""
        self.name = name
        self.set_position(mapping)
        self.looted = False
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.img = os.path.join(self.root, IMG_PATH, img)
        self.pygame_img = pygame.image.load(self.img)

    def set_position(self, mapping):
        """Generate a random position, check if the position is availale, else repeat"""
        rand_y = random.randint(0, 15) -1
        rand_x = random.randint(0, 15) -1
        if mapping.is_tile_empty(rand_y, rand_x):
            self.y_pos = rand_y
            self.x_pos = rand_x
            mapping.set_item(rand_y, rand_x)
        else:
            self.set_position(mapping)
