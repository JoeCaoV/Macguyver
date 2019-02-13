import os
import pygame.image

class Character:
    """this class alone while set the guardian, but will be extended
    to create the MacGyver class"""
    def __init__(self, y_pos, x_pos, img, mapping):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.path_img = self.root + "/ressource/image/"
        self.img = os.path.join(self.path_img, img)
        self.pygame_img = pygame.image.load(self.img)
        self.set_onmap(mapping)

    def set_onmap(self, mapping):
        #set the guardian on the map
        mapping.set_bad_guy(self.y_pos, self.x_pos)
