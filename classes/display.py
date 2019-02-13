import pygame
from config import *

class Display:
    """This class, contains every action that must output or modify the display
    of the game window, like moving the character, remove items or show infos
    """

    def __init__(self, width, height, title):
        """init the class by creating the pygame window"""
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def game_over(self, message):
        """#When the game is over, display the end message and close the game"""
        self.window.fill((0, 0, 0))
        text = BIG_FONT.render(message, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = 300, 300
        self.window.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def _loot_item(self, gyver, items):
        """check if MacGyver meet an uncollected item,
        if he does, add it to the bag and mark the item as looted
        """
        for item in items:
            if(gyver.x_pos == item.x_pos and gyver.y_pos == item.y_pos and
                    item.looted is False):
                gyver.bag += 1
                item.looted = True
                self.show_message('You collected the {}'.format(item.name), BOT_LEFT)
                self.window.blit(FLOOR, (TILE_SIZE*item.x_pos, TILE_SIZE*item.y_pos))
                bag_message = "You collected {}/3 items".format(gyver.bag)
                self.show_message(bag_message, BOT_RIGHT)
                return item
        return None

    def set_map(self, mapping):
        """display the floor and wall tiles"""
        for y_pos, line in enumerate(mapping.map):
            for x_pos, tile in enumerate(line):
                if tile == '#':
                    self.window.blit(WALL, (x_pos*TILE_SIZE, y_pos*TILE_SIZE))
                else:
                    self.window.blit(FLOOR, (x_pos*TILE_SIZE, y_pos*TILE_SIZE))

    def show_looted_items(self, items):
        """display the items looted in bottom screen"""
        for x_pos, item in enumerate(items):
            if item.looted:
                self.window.blit(item.pygame_img, (300+TILE_SIZE*x_pos, 605))
        pygame.display.flip()

    def set_characters(self, gyver, bad_guy):
        """display both characters"""
        gyver_position = (gyver.x_pos * TILE_SIZE, gyver.y_pos * TILE_SIZE)

        bad_guy_position = (bad_guy.x_pos * TILE_SIZE, bad_guy.y_pos * TILE_SIZE)

        self.window.blit(gyver.pygame_img, gyver_position)
        self.window.blit(bad_guy.pygame_img, bad_guy_position)

    def set_items(self, items):
        """display the items on the map"""
        for item in items:
            image = item.pygame_img
            self.window.blit(image, (item.x_pos * TILE_SIZE, item.y_pos * TILE_SIZE))

    def show_message(self, message, rect):
        """Display the given message in the given rect"""
        self.window.fill((0, 0, 0), rect)
        text = message
        text_render = FONT.render(text, True, (255, 255, 255))
        self.window.blit(text_render, rect)
        pygame.display.update(rect)

    def move_character(self, mapping, gyver, items, old_y, old_x):
        """move the character, to his new position, check if the position
        is available and return his old position if not and display the
        message "Invalid destination" else display the character on his
        new position and check if he meet item or guardian
        """
        self.window.fill((0, 0, 0), BOT_LEFT)
        pygame.display.update(BOT_LEFT)
        if (mapping.is_path_available(gyver.y_pos, gyver.x_pos) and
                (old_y != gyver.y_pos or old_x != gyver.x_pos)):
            mapping.move_character(old_y, old_x, gyver.y_pos, gyver.x_pos)
            self._loot_item(gyver, items)
            self.show_looted_items(items)
            self.window.blit(gyver.pygame_img,
                             (gyver.x_pos * TILE_SIZE, gyver.y_pos * TILE_SIZE))
            self.window.blit(FLOOR, (old_x * TILE_SIZE, old_y * TILE_SIZE))
            pygame.display.update()
        else:
            gyver.y_pos = old_y
            gyver.x_pos = old_x
            message = 'Invalid Destination'
            self.show_message(message, BOT_LEFT)
