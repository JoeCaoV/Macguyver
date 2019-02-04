import random

class Items():

	def __init__(self, name, img, mapping):
        self.name = name
        self.img = img
        self._set_position(mapping)
        
    def _set_position(self, mapping):
    	available = mapping.list_every_path()
    	rand_ind = random.randomint(0, len(available)) -1
    	self.y = available[rand_int][0]
    	self.x = available[rand_int][1]



