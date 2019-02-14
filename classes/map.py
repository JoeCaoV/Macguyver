"""import os module to get map elements' file and const IMG_PATH"""
import os
from config import DATA_PATH

class Map:
    """Class to contain the map, ' ' is a road, '#' is a wall,
    'G' is Gyver, 'X' is an item, 'W' is the guardian.
    """
    def __init__(self, mapping):
        #init the class by creating the map
        self.create_map(mapping)

    def is_path_available(self, y_pos, x_pos):
        """ Check if the destination is available """
        if 15 > y_pos >= 0 and 0 <= x_pos < 15:
            return self.map[y_pos][x_pos] in [' ', 'G', 'X', 'W']
        return False

    def is_tile_empty(self, y_pos, x_pos):
        """ Check if the tile is empty """
        if 15 > y_pos >= 0 and 0 <= x_pos < 15:
            return self.map[y_pos][x_pos] == ' '
        return False

    def set_character(self, y_pos, x_pos):
        """place the hero into the labyrinth"""
        self.map[y_pos][x_pos] = 'G'

    def set_item(self, y_pos, x_pos):
        """place the item into labyrinth"""
        self.map[y_pos][x_pos] = 'X'

    def set_bad_guy(self, y_pos, x_pos):
        """place the guardian into the labyrinth"""
        self.map[y_pos][x_pos] = 'W'

    def move_character(self, old_y, old_x, y_pos, x_pos):
        """replaces the available path by our lord and savior MacGyver"""
        self.map[old_y][old_x] = ' '
        self.map[y_pos][x_pos] = 'G'

    def create_map(self, data_file):
        """create the labyrinth from a txt file"""
        mapping = []
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_file = os.path.join(root, DATA_PATH, data_file)
        with open(path_to_file, 'r') as file:
            lines = file.readlines()
            list_array = [x.strip('\n') for x in lines]
            for line in list_array:
                mapping.append(list(line))

        self.map = mapping

    def show_map(self):
        """Display the map in the terminal"""
        for line in self.map:
            print("".join(line))
