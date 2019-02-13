from classes.characters import Character

class MacGyver(Character):
    """Class for the man character : MacGyver"""

    def __init__(self, y, x, img, mapping):
        """Extends character class, but got a bag"""
        Character.__init__(self, y, x, img, mapping)
        self.bag = 0

    def set_onmap(self, mapping):
        """Set the hero on the map"""
        mapping.set_bad_guy(self.y_pos, self.x_pos)

    def moving(self, direction):
        """when the keypad is used to move Macgyver,
        change his position"""
        if direction == 'left':
            self.x_pos -= 1
        elif direction == 'right':
            self.x_pos += 1
        elif direction == 'bottom':
            self.y_pos += 1
        elif direction == 'top':
            self.y_pos -= 1
