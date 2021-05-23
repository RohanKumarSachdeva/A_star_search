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


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x_pos = row * width
        self.y_pos = col * width
        self.color = WHITE
        self.neighbours = []

    def get_position(self):
        return self.row, self.col

    # Functions to check the state of the node.
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    # Functions to set the state of the node.
    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE


run = True

while run:
    pygame.time.delay(50)
    # capture the click on CROSS and make run false
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# terminating the game
pygame.quit()
