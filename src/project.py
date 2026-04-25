import pygame
from pygame.locals import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
 
clock = pygame.time.Clock()
fps = 60
 
screen_width = 1000
screen_height = 1000
 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Get out')