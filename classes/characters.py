class MacGyver:

    def __init__(self, y, x):
        self.alive = True
        self.x = x
        self.y = y
        self.bag = 0
        self.got_needle = False
        self.got_tube = False
        self.got_syringe = False

    def moving(self,direction):
        if(direction == 'left'):
            self.x -= 1
        elif(direction == 'right'):
            self.x += 1
        elif(direction == 'bottom'):
            self.y += 1
        elif(direction == 'top'):
            self.y -= 1
        else:
            raise Warning('Incorrect direction, please use : left, right, bottom or top')

        


class Guardian:

    def __init__(self, x, y):
        self.asleep = False
        self.x = x
        self.y = y
