import pygame
import math
from queue import PriorityQueue
# initializing pygame
pygame.init()
# Setting up game window, inserting a tuple (800,800)
screen_width = 800
screen_height = 800
bg_color = (0, 0, 0)
screen_window = pygame.display.set_mode((screen_width, screen_height))
# Giving window caption name
pygame.display.set_caption('A* Path Finding Algorithm')
# Color Codes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


run = True

while run:
    pygame.time.delay(50)
    # capture the click on CROSS and make run false
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# terminating the game
pygame.quit()

