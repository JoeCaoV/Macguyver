"""Pygame module is needed to load image, en create pygame obj"""
import pygame
#pylint: disable=E1101
pygame.init()

TILE_SIZE = 40
IMG_PATH = 'ressource/image/'
DATA_PATH = 'ressource/data/'
FLOOR = pygame.image.load('{}floor.jpg'.format(IMG_PATH))
WALL = pygame.image.load('{}wall.jpg'.format(IMG_PATH))
BOT_LEFT = pygame.Rect(15, 615, 250, 50)
BOT_RIGHT = pygame.Rect(450, 615, 250, 50)
FONT = pygame.font.Font(None, 20)
BIG_FONT = pygame.font.Font(None, 40)
