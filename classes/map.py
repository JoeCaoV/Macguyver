import os
import logging as lg
import numpy as np

class Map:

    MAP_SIZE = 15
    
    #check if the destination is available
    def is_path_available(self, y, x):
        if(y >= 0 and y < 15 and x >= 0 and x < 15):
            return True if self.map[y][x] == '0' else False
        else:
            return False

    #replaces the available by our lord and savior MacGyver
    def set_character(self, y, x):
        self.map[y][x] = 'G'
        return self.map

    def move_character(self, old_y, old_x, y, x):
        self.map[old_y][old_x] = '0'
        self.map[y][x] = 'G'
        return self.map

    #create the labyrinth from a txt file
    def create_map(self, data_file):
        mapping = []
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_file = os.path.join(directory, "ressource", "data", data_file)
        try:
            with open(path_to_file, 'r') as f:
                lines = f.readlines()
                list_array = [x.strip() for x in lines]
                for line in list_array:
                    if (len(line) == 15):
                        mapping.append(list(line))
                    else:
                        raise IncorrectFileError("The map should be a 15 tiles width square")
        except FileNotFoundError as e:
            lg.critical('File not found : {}'.format(e))
        
        self.map = np.array(mapping)
        return self.map

    #Display the map for the terminal
    def show_map(self):
        print(np.vstack(self.map))
