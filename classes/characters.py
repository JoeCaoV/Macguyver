import os
import pygame.image

class Character:

    def __init__(self, y, x, img, mapping):
        self.x = x
        self.y = y
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.path_img = self.root + "/ressource/image/"
        self.img = os.path.join(self.path_img, img)
        self.pygame_img = pygame.image.load(self.img)
        self.set_onmap(mapping)

    def set_onmap(self, mapping):
        mapping.set_bad_guy(self.y, self.x)
