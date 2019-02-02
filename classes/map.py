import os
import logging as lg
import numpy as np

class Map:

    MAP_SIZE = 15

    #check if the destination is available
    def is_path_available(self, y, x):
        return True if self.map[y][x] == '0' else False

    #create the labyrinth from a txt file
    def create_map(self, data_file):
        mapping = []
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(directory)
        path_to_file = os.path.join(directory, "ressource", "data", data_file)
        try:
            with open(path_to_file, 'r') as f:
                lines = f.readlines()
                list = [x.strip() for x in lines]
                for i in list:
                    if (len(i) == 15):
                        mapping.append(i)
                    else:
                        raise IncorrectFileError("The map should be a 15 tiles width square")
        except FileNotFoundError as e:
            lg.critical('File not found : {}'.format(e))
        
        self.map = np.array(mapping)
        return np.vstack(self.map)

