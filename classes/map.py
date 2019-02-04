import os
import logging as lg
import numpy as np

class Map:
    """Hello"""
    MAP_SIZE = 15

    def list_every_path(self):
        """make an array of every available location"""
        available = []
        for y, line in enumarate(self.map):
            for x,  tile in line:
                if tile == '0':
                    available.append([y, x])
        return available

    def is_path_available(self, y_pos, x_pos):
        """ Check if the destination is available """
        if(15 > y_pos >= 0 and 0 <= x_pos < 15):
            return True if self.map[y_pos][x_pos] == '0' else False

    def set_character(self, y_pos, x_pos):
        """place the hero into the labyrinth"""
        self.map[y_pos][x_pos] = 'G'
        return self.map


    def set_bad_guy(self, y_pos, x_pos):
        """place the guardian into the labyrinth"""
        self.map[y_pos][x_pos] = 'W'
        return self.map

    def move_character(self, old_y, old_x, y_pos, x_pos):
        """replaces the available path by our lord and savior MacGyver"""
        self.map[old_y][old_x] = '0'
        self.map[y_pos][x_pos] = 'G'
        return self.map

    def create_map(self, data_file):
        """create the labyrinth from a txt file"""
        mapping = []
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_file = os.path.join(directory, "ressource", "data", data_file)
        try:
            with open(path_to_file, 'r') as file:
                lines = file.readlines()
                list_array = [x.strip() for x in lines]
                for line in list_array:
                    try:
                        if len(line) == 15:
                            mapping.append(list(line))
                    except ValueError:
                        lg.critical('The map must by 15 tiles width')
        except FileNotFoundError as error:
            lg.critical('File not found : %s', error)

        self.map = np.array(mapping)
        return self.map

    def show_map(self):
        """Display the map in the terminal"""
        print(np.vstack(self.map))
