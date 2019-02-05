class MacGyver:

    def __init__(self, y, x, mapping):
        self.alive = True
        self.x = x
        self.y = y
        self.bag = 0
        mapping.set_character(y,x)

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
            print('Incorrect direction, please use : left, right, bottom or top')
        return self.y

        


class Guardian:

    def __init__(self, y, x, mapping):
        self.asleep = False
        self.x = x
        self.y = y
        mapping.set_bad_guy(y, x)
