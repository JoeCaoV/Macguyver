import random
import os
import pygame.image

class Item():

    def __init__(self, name, img, mapping):
        self.name = name
        self.set_position(mapping)
        self.looted = False
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.img = os.path.join(self.root, "ressource", "image", img)
        self.pygame_img = pygame.image.load(self.img)

    def set_position(self, mapping):
        rand_y = random.randint(0, 15) -1
        rand_x = random.randint(0, 15) -1
        if mapping.is_tile_empty(rand_y, rand_x):
            self.y = rand_y
            self.x = rand_x
            mapping.set_item(rand_y, rand_x)

        else:
            return self.set_position(mapping)
