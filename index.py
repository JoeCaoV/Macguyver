#!/usr/bin/env python3
# coding: utf-8
import argparse
import classes.map as mp
import classes.characters as ch
import logging as lg

def set_game():
    mapping = mp.Map()
    mapping.create_map("mapping.txt")

    gyver = ch.MacGyver(14, 0)
    mapping.set_character(gyver.y, gyver.x)
    mapping.show_map()
    __start_game(mapping, gyver)


def __start_game(mapping,gyver):
    game_over = False
    while not game_over:
        deplacement = input('Choose were you want to move MacGyver : ')
        old_y = gyver.y
        old_x = gyver.x
        gyver.moving(deplacement)
        if(mapping.is_path_available(gyver.y, gyver.x)):
            mapping.move_character(old_y, old_x, gyver.y, gyver.x)
            mapping.show_map()
        else:
            gyver.y = old_y
            gyver.x = old_x
            print('Invalid destination, try again')




def main():
    set_game()


if __name__ == "__main__":
    main()
