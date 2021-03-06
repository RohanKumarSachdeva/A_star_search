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

    def draw_node(self, window):
        node_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.width)
        pygame.draw.rect(window, self.color, node_rect)

    def update_neighbours(self, grid):
        pass

    # Comparing two Spot objects
    def __lt__(self, other):
        return False


def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
    return manhattan_distance


# Making a grid of Spots
def make_grid(rows, columns, width):
    # Grid is a 2-D list
    grid = []
    gap = width // rows
    for row in range(rows):
        # for every i append a list, creating a row
        grid.append([])
        # for every column in this row add a spot
        for col in range(columns):
            spot = Spot(row, col, gap, rows)
            grid[row].append(spot)
    return grid


def draw_grid_lines(window, rows, columns, width):
    gap = width // rows
    for row in range(rows):
        start_co = (0, row * gap)
        end_co = (width, row * gap)
        pygame.draw.line(window, GREY, start_co, end_co)
        for col in range(columns):
            start_co = (col * gap, 0)
            end_co = (col * gap, width)
            pygame.draw.line(window, GREY, start_co, end_co)


def draw(window, grid, rows, columns, width):
    screen_window.fill(WHITE)
    # Get a row from the 2D grid.
    for row in grid:
        # Get Spot object from this row and draw
        for spot in row:
            spot.draw_node(window)
    draw_grid_lines(window, rows, columns, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


def main(window, width):
    rows = 50
    columns = 50
    grid = make_grid(rows, columns, width)
    start_pos = None
    end_pos = None
    run = True
    started = False
    while run:
        draw(window, grid, rows, columns, width)
        # capture the click on CROSS and make run false
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed(3)[0]:  # 0 for Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                if not start_pos:
                    start_pos = spot
                    start_pos.make_start()
                elif not end_pos:
                    end_pos = spot
                    end_pos.make_end()
                elif spot != start_pos and spot != end_pos:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed(3)[2]:  # 2 for Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                if spot.is_start():
                    start_pos = None
                elif spot.is_end():
                    end_pos = None
                spot.reset()
    # terminating the game
    pygame.quit()


main(screen_window, screen_width)
