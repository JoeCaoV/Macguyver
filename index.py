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
    bad_guy = ch.Guardian(1, 14, mapping)
    gyver = ch.MacGyver(14, 0, mapping)


    #Setting the items
    tube = itm.Item('tube', 'tube.png', mapping)
    ether = itm.Item('ether', 'ether.png', mapping)
    needle = itm.Item('needle', 'needle.png', mapping)
    items = [tube, ether, needle]

    mapping.show_map()

    _start_game(mapping, gyver, bad_guy, items)

def _check_encounter(gyver, bad_guy):
    if(gyver.x == bad_guy.x and gyver.y == bad_guy.y):
        if gyver.bag == 3:
            print("Congratulations, you won !")
        else:
            print("The guard killed you, collect all the items next time")
        return False
    else:
        return True

def _loot_item(gyver, items):
    for item in items:
        if gyver.x == item.x and gyver.y == item.y and item.looted == False:
            print("you collected the {}".format(item.name))
            gyver.bag += 1
            item.looted = True

def _start_game(mapping, gyver, bad_guy, items):
    """Once the elements of the game are set by set_game(),
    this function will loop an input asking direction
    until the game is over
    """

    while _check_encounter(gyver, bad_guy):
        print('Items : {}/3'.format(gyver.bag))
        deplacement = input('Choose were you want to move MacGyver : ')
        old_y = gyver.y
        old_x = gyver.x
        gyver.moving(deplacement)
        if mapping.is_path_available(gyver.y, gyver.x):
            mapping.move_character(old_y, old_x, gyver.y, gyver.x)
            mapping.show_map()
            _loot_item(gyver, items)
        else:
            gyver.y = old_y
            gyver.x = old_x
            print('Invalid destination, try again')   

if __name__ == "__main__":
    main()
