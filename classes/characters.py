class MacGyver:

    def __init__(self,position):
    	self.alive = True
    	self.position = position
    	self.got_needle = False
    	self.got_tube = False
    	self.got_syringe = False

    def moving(self,direction):
    	if(direction == 'left'):
    		pass
    	elif(direction == 'right'):
    		pass
    	elif(direction == 'bottom'):
    		pass
    	elif(direction == 'top'):
    		pass
    	else:
    		raise Warning('Incorrect direction, please use : left, right, bottom or top')

        


class Guardian:

    def __init__(self,position):
    	self.asleep = False
    	self.position = position
