import os

class Map:
    """Hello"""
    MAP_SIZE = 15

    def __init__(self, mapping):
        self.create_map(mapping)

    def list_every_path(self):
        """make an array of every available location"""
        available = []
        for y, line in enumarate(self.map):
            for x,  tile in line:
                if tile == ' ':
                    available.append([y, x])
        return available

    def is_path_available(self, y_pos, x_pos):
        """ Check if the destination is available """
        if(15 > y_pos >= 0 and 0 <= x_pos < 15):
            return True if self.map[y_pos][x_pos] == ' ' else False

    def set_character(self, y_pos, x_pos):
        """place the hero into the labyrinth"""
        self.map[y_pos][x_pos] = 'G'
        return self.map

    def set_item(self, y_pos, x_pos):
        """place the item into labyrinth"""
        self.map[y_pos][x_pos] = 'X'
        return self.map

    def set_bad_guy(self, y_pos, x_pos):
        """place the guardian into the labyrinth"""
        self.map[y_pos][x_pos] = 'W'
        return self.map

    def move_character(self, old_y, old_x, y_pos, x_pos):
        """replaces the available path by our lord and savior MacGyver"""
        self.map[old_y][old_x] = ' '
        self.map[y_pos][x_pos] = 'G'
        return self.map

    def create_map(self, data_file):
        """create the labyrinth from a txt file"""
        mapping = []
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_file = os.path.join(directory, "ressource", "data", data_file)
        with open(path_to_file, 'r') as file:
            lines = file.readlines()
            list_array = [x.strip('/n') for x in lines]
            for line in list_array:
                mapping.append(list(line))

        self.map = mapping
        return self.map

    def show_map(self):
        """Display the map in the terminal"""
        for line in self.map:
            print("".join(line))

        