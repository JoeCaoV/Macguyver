#!/usr/bin/env python3
# coding: utf-8

import pygame
#pylint: disable=W0614, W0401
from pygame.locals import *
import classes.characters as ch
import classes.map as mp
import classes.items as itm

pygame.init()
pygame.display.set_caption("MacGyver's Challenger")

WINDOW = pygame.display.set_mode((600, 650))
TILE_SIZE = 40
PATH = 'ressource/image/'
FLOOR = pygame.image.load('{}floor.jpg'.format(PATH))
WALL = pygame.image.load('{}WALL.jpg'.format(PATH))
BOT_LEFT = pygame.Rect(15, 615, 300, 50)
BOT_RIGHT = pygame.Rect(450, 615, 300, 50)
FONT = pygame.font.Font(None, 20)

def create_labyrinth(mapping, gyver, bad_guy, items):
   #create the labyrinth with pygame

    #set the map with floor & walls
    #pylint: disable=C0103
    for y, line in enumerate(mapping.map):
        for x, tile in enumerate(line):
            if tile == '#':
                WINDOW.blit(WALL, (x*TILE_SIZE, y*TILE_SIZE))
            else:
                WINDOW.blit(FLOOR, (x*TILE_SIZE, y*TILE_SIZE))

    #set the characters

    gyver_position = (gyver.x * TILE_SIZE, gyver.y * TILE_SIZE)

    bad_guy_position = (bad_guy.x * TILE_SIZE, bad_guy.y * TILE_SIZE)

    WINDOW.blit(gyver.pygame_img, gyver_position)
    WINDOW.blit(bad_guy.pygame_img, bad_guy_position)

    #set the items
    for item in items:
        image = item.pygame_img
        WINDOW.blit(image, (item.x * TILE_SIZE, item.y * TILE_SIZE))

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

    create_labyrinth(mapping, gyver, bad_guy, items)

    pygame.display.flip()

    _start_game(mapping, gyver, bad_guy, items)


def _check_encounter(gyver, bad_guy):
    """check if MacGyver meets the Guardian,
    if he does, check if all items have been collected,
    you win if they are, you lose otherwise"""
    if(gyver.x == bad_guy.x and gyver.y == bad_guy.y):
        if gyver.bag == 3:
            end = "Congratulations, you won !"
        else:
            end = "You lost !"
        WINDOW.fill((0, 0, 0))
        font = pygame.font.Font(None, 40)
        text = font.render(end, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = 300, 300
        WINDOW.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        return True
    return None

def _loot_item(gyver, items):
    """check if MacGyver meet an uncollected item,
    if he does, add it to the bag and mark the item as looted
    """
    for item in items:
        if gyver.x == item.x and gyver.y == item.y and item.looted is False:
            gyver.bag += 1
            item.looted = True
            display_info('You collected the {}'.format(item.name))
            display_bag(gyver)
            return item
    return None

def display_info(message):
    """This function display the message given on the bottom left corner"""
    WINDOW.fill((0, 0, 0), BOT_LEFT)
    info_message = message
    info_render = FONT.render(info_message, True, (255, 255, 255))
    WINDOW.blit(info_render, BOT_LEFT)
    pygame.display.update(BOT_LEFT)

def display_bag(gyver):
    """This function display the number of collected item on the bottom right corner"""
    WINDOW.fill((0, 0, 0), BOT_RIGHT)
    bag_message = 'You collected {}/3 items'.format(gyver.bag)
    bag_render = FONT.render(bag_message, True, (255, 255, 255))
    WINDOW.blit(bag_render, BOT_RIGHT)
    pygame.display.update(BOT_RIGHT)

def _start_game(mapping, gyver, bad_guy, items):
    """Once the elements of the game are set by set_game(),
    this function will loop an input asking direction
    until the game is over
    """
    display_bag(gyver)
    message = 'Collect all items to defeat the guardian'
    display_info(message)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == KEYDOWN:
                old_y = gyver.y
                old_x = gyver.x
                if event.key == K_UP:
                    gyver.moving('top')
                elif event.key == K_DOWN:
                    gyver.moving('bottom')
                elif event.key == K_RIGHT:
                    gyver.moving('right')
                elif event.key == K_LEFT:
                    gyver.moving('left')

                WINDOW.fill((0, 0, 0), BOT_LEFT)
                pygame.display.update(BOT_LEFT)
                if(old_y != gyver.y or old_x != gyver.x):
                    if mapping.is_path_available(gyver.y, gyver.x):
                        mapping.move_character(old_y, old_x, gyver.y, gyver.x)
                        _loot_item(gyver, items)
                        WINDOW.blit(gyver.pygame_img, (gyver.x * TILE_SIZE, gyver.y * TILE_SIZE))
                        WINDOW.blit(FLOOR, (old_x * TILE_SIZE, old_y * TILE_SIZE))
                        pygame.display.update()
                        game_over = _check_encounter(gyver, bad_guy)
                    else:
                        gyver.y = old_y
                        gyver.x = old_x
                        message = 'Invalid Destination'
                        display_info(message)


if __name__ == "__main__":
    main()
