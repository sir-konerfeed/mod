#модули
import os
import sys
import pygame
import random
from pygame import *

#запуск 
pygame.init()

#сеттинги
scr_size = (width,height) = (700,400)
FPS = 60
gravity = 0.6

#цвета RGB
BLACK =          (  0,    0,    0)
WHITE =          (255,  255,  255)
background_col = (235,  235,  235)

#счётчик
high_score = 0

#экран игры
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Dino")

#sound
jump_sound = pygame.mixer.Sound('sound/jump.wav')
die_sound = pygame.mixer.Sound('sound/die.wav')
checkPoint_sound = pygame.mixer.Sound('sound/checkpoint.wav')
