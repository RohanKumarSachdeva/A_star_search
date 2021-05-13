import pygame, random
# initializing pygame
pygame.init()
# Setting up game window, inserting a tuple (800,600)
screen_width = 800
screen_height = 600
bg_color = (0, 0, 0)
screen_window = pygame.display.set_mode((screen_width, screen_height))
# Giving window caption name
pygame.display.set_caption('MyGame')
# drawing a character
x_pos = 0
y_pos = 0
width = 50
height = 50
velocity = 50
player_color = (250, 0, 0)
run = True

while run:
    pygame.time.delay(50)
    # capture the click on CROSS and make run false
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Upon holding a key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_pos - velocity >= 0:
        y_pos = y_pos - velocity
    if keys[pygame.K_DOWN] and y_pos + velocity + height <= screen_height:
        y_pos = y_pos + velocity
    if keys[pygame.K_LEFT] and x_pos - velocity >= 0:
        x_pos = x_pos - velocity
    if keys[pygame.K_RIGHT] and x_pos + velocity + width <= screen_width:
        x_pos = x_pos + velocity

    # fill the screen with back-ground colour
    red = random.randint(0, 250)
    green = random.randint(0, 250)
    blue = random.randint(0, 250)
    screen_window.fill(bg_color)
    # Drawing a character on screen
    pygame.draw.rect(screen_window, (red, green, blue),
                     (x_pos, y_pos, height, width))
    # To make the character visible we have to keep on refreshing
    pygame.display.update()

# terminating the game
pygame.quit()

