#!/usr/bin/env python3
# coding: utf-8
import pygame
from classes.characters import Character
from classes.display import Display
from classes.map import Map
from classes.items import Item
from classes.gyver import MacGyver

class Main():

    def __init__(self):
        """function to set the game : creating the map, placing the items randomly,
        MacGyver and the Guardian's location must be specified (y, x).
        Once it's done, starting the game.
        """
        mapping = Map("mapping.txt")

        #Setting the characters
        bad_guy = Character(1, 14, "guardian.png", mapping)
        gyver = MacGyver(14, 0, "macgyver.png", mapping)

        title = "MacGyver's Labyrinth"
        display = Display(600, 650, title)

        #Setting the items
        tube = Item('tube', 'tube.png', mapping)
        ether = Item('ether', 'ether.png', mapping)
        needle = Item('needle', 'needle.png', mapping)
        items = [tube, ether, needle]

        self.create_labyrinth(mapping, gyver, bad_guy, items, display)

        pygame.display.flip()

        self._start_game(mapping, gyver, bad_guy, items, display)

    def create_labyrinth(self, mapping, gyver, bad_guy, items, display):
       #create the labyrinth with pygame
        #set the map with floor & walls
        display.set_map(mapping)

        #set the characters
        display.set_characters(gyver, bad_guy)

        #set the items
        display.set_items(items)

    def _check_encounter(self, gyver, bad_guy, display):
        """check if MacGyver meets the Guardian,
        if he does, check if all items have been collected,
        you win if they are, you lose otherwise"""
        if(gyver.x == bad_guy.x and gyver.y == bad_guy.y):
            if gyver.bag == 3:
                end = "Congratulations, you won !"
            else:
                end = "You lost !"
            display.game_over(end)
            return True
        return None

    def _start_game(self, mapping, gyver, bad_guy, items, display):
        """Once the elements of the game are set by set_game(),
        this function will loop an input asking direction
        until the game is over
        """
        display.show_bag(gyver)
        message = 'Collect all items to defeat the guardian'
        display.show_info(message)

        game_over = False
        while not game_over:
            for event in pygame.event.get():
                old_y = gyver.y
                old_x = gyver.x
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

                    display.move_character(mapping, gyver, items, old_y, old_x)
                    game_over = self._check_encounter(gyver, bad_guy, display)


if __name__ == "__main__":
    main = Main()
