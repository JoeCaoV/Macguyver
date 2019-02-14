#!/usr/bin/env python3
# coding: utf-8
"""import Pygame module to display the game
Then all the classes needed and the required constants
"""
import pygame
from classes.characters import Character
from classes.display import Display
from classes.map import Map
from classes.items import Item
from classes.gyver import MacGyver
from config import BOT_LEFT, BOT_RIGHT

#pylint: disable=E1101
class Main():
    """Class that will run the game using all the other ones"""

    def __init__(self):
        """function to set the game : creating the map, placing the items randomly,
        MacGyver and the Guardian's location must be specified (y, x).
        Once it's done, starting the game.
        """
        #setting the pygame window
        title = "MacGyver's Labyrinth"
        display = Display(600, 650, title)

        #Setting the map
        mapping = Map("mapping.txt")
        display.set_map(mapping)

        #Setting the characters
        bad_guy = Character(1, 14, "guardian.png", mapping)
        gyver = MacGyver(14, 0, "macgyver.png", mapping)
        display.set_characters(gyver, bad_guy)

        pygame.display.flip()

        self._start_game(mapping, gyver, bad_guy, display)

    @staticmethod
    def check_encounter(gyver, bad_guy, display):
        """check if MacGyver meets the Guardian,
        if he does, check if all items have been collected,
        you win if they are, you lose otherwise"""
        if(gyver.x_pos == bad_guy.x_pos and gyver.y_pos == bad_guy.y_pos):
            if gyver.bag == 3:
                end = "Congratulations, you won !"
            else:
                end = "You lost !"
            display.game_over(end)
            return True
        return None

    @staticmethod
    def set_items(mapping, display):  #pylint: disable=W0613
        """Setting the items"""
        tube = Item('tube', 'tube.png', mapping)
        ether = Item('ether', 'ether.png', mapping)
        needle = Item('needle', 'needle.png', mapping)
        items = [tube, ether, needle]
        display.set_items(items)
        pygame.display.flip()
        return items

    def _start_game(self, mapping, gyver, bad_guy, display):
        """Once the elements of the game are set by set_game(),
        this function will loop an input asking direction
        until the game is over
        """
        items = self.set_items(mapping, display)
        message = 'You collected 0/3 items'
        display.show_message(message, BOT_RIGHT)
        message = 'Collect all items to defeat the guardian'
        display.show_message(message, BOT_LEFT)

        game_over = False
        while not game_over:
            for event in pygame.event.get():
                old_position = {"y_pos": gyver.y_pos, "x_pos": gyver.x_pos}
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        gyver.moving('top')
                    elif event.key == pygame.K_DOWN:
                        gyver.moving('bottom')
                    elif event.key == pygame.K_RIGHT:
                        gyver.moving('right')
                    elif event.key == pygame.K_LEFT:
                        gyver.moving('left')

                    display.move_character(mapping, gyver, items, old_position)
                    game_over = self.check_encounter(gyver, bad_guy, display)


if __name__ == "__main__":
    MAIN = Main()
