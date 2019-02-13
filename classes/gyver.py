from classes.characters import *

class MacGyver(Character):

    def __init__(self, y, x, img, mapping):
        Character.__init__(self, y, x, img, mapping)
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
