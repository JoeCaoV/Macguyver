import pygame.image
import os

class Guardian:

    def __init__(self, y, x, img, mapping):
        self.alive = True
        self.x = x
        self.y = y
        self.root= os.path.dirname(os.path.dirname(__file__))
        self.path_img = self.root + "/ressource/image/"
        self.img = os.path.join(self.path_img, img)
        self.pygame_img = pygame.image.load(self.img)
        self.set_onmap(mapping)

    def set_onmap(self, mapping):
        mapping.set_bad_guy(self.y, self.x)


class MacGyver(Guardian):

    def __init__(self, y, x, img, mapping):
        Guardian.__init__(self, y, x, img, mapping)
        self.bag = 0


    def set_onmap(self, mapping):
        mapping.set_bad_guy(self.y, self.x)

    def moving(self, direction):
        if direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'bottom':
            self.y += 1
        elif direction == 'top':
            self.y -= 1


