import pygame.image
import os

class Guardian:

    def __init__(self, y, x, mapping):
        self.asleep = False
        self.x = x
        self.y = y
        self.dir = "../" + os.path.dirname(__file__))
        self.img = os.path.join(self.dir, "ressource", "image", 'Gardien.png')
        self.pygame_img = pygame.image.load(self.img)
        mapping.set_bad_guy(y, x)


class MacGyver(Guardian):

    def __init__(self, y, x, mapping):
        self.alive = True
        self.x = x
        self.y = y
        self.bag = 0
        self.path = "../" + os.path.dirname(__file__)
        self.img = os.path.join(self.dir, "ressource", "image", 'MacGyver.png')
        self.pygame_img = pygame.image.load(self.img)
        mapping.set_character(y,x)

    def moving(self,direction):
        if direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'bottom':
            self.y += 1
        elif direction == 'top':
            self.y -= 1


