#!/usr/bin/env python3
# coding: utf-8
import pygame
#pylint: disable=W0614, W0401
from pygame.locals import *
import classes.characters as ch
import classes.display as dp
import classes.map as mp
import classes.items as itm

def create_labyrinth(mapping, gyver, bad_guy, items, display):
   #create the labyrinth with pygame
    #set the map with floor & walls
    display.set_map(mapping)

    #set the characters
    display.set_characters(gyver, bad_guy)

    #set the items
    display.set_items(items)


def main():
    """function to set the game : creating the map, placing the items randomly,
    MacGyver and the Guardian's location must be specified (y, x).
    Once it's done, starting the game.
    """
    mapping = mp.Map("mapping.txt")

    #Setting the characters
    bad_guy = ch.Guardian(1, 14, mapping)
    gyver = ch.MacGyver(14, 0, mapping)

    title ="MacGyver's Labyrinth"
    display = dp.Display(600, 650, title)

    #Setting the items
    tube = itm.Item('tube', 'tube.png', mapping)
    ether = itm.Item('ether', 'ether.png', mapping)
    needle = itm.Item('needle', 'needle.png', mapping)
    items = [tube, ether, needle]

    create_labyrinth(mapping, gyver, bad_guy, items, display)

    pygame.display.flip()

    _start_game(mapping, gyver, bad_guy, items, display)


def _check_encounter(gyver, bad_guy, display):
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

def _start_game(mapping, gyver, bad_guy, items, display):
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
            if event.type == QUIT:
                game_over = True
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    gyver.moving('top')
                elif event.key == K_DOWN:
                    gyver.moving('bottom')
                elif event.key == K_RIGHT:
                    gyver.moving('right')
                elif event.key == K_LEFT:
                    gyver.moving('left')

                display.move_character(mapping, gyver, bad_guy, items, old_y, old_x)
                game_over = _check_encounter(gyver, bad_guy, display)


if __name__ == "__main__":
    main()
