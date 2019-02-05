#!/usr/bin/env python3
# coding: utf-8
import logging as lg
import classes.characters as ch
import classes.map as mp
import classes.items as itm

def main():
    """function to set the game : creating the map, placing the items randomly,
    MacGyver and the Guardian's location must be specified (y, x).
    Once it's done, starting the game.
    """
    mapping = mp.Map("mapping.txt")

    #Setting the characters
    guardian = ch.Guardian(1, 14, mapping)
    gyver = ch.MacGyver(14, 0, mapping)


    #Setting the items
    tube = itm.Item('tube', 'tube.png', mapping)
    ether = itm.Item('ether', 'ether.png', mapping)
    needle = itm.Item('needle', 'needle.png', mapping)
    
    mapping.show_map()

    _start_game(mapping, gyver)

def _start_game(mapping, gyver):
    """Once the elements of the game are set by set_game(),
    this function will loop an input asking direction
    until the game is over
    """
    game_over = False
    while not game_over:
        deplacement = input('Choose were you want to move MacGyver : ')
        old_y = gyver.y
        old_x = gyver.x
        gyver.moving(deplacement)
        if mapping.is_path_available(gyver.y, gyver.x):
            mapping.move_character(old_y, old_x, gyver.y, gyver.x)
            mapping.show_map()
        else:
            gyver.y = old_y
            gyver.x = old_x
            print('Invalid destination, try again')


if __name__ == "__main__":
    main()
