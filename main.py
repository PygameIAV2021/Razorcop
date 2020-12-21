# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2020.

import pygame
import random

WIDTH = 640
HEIGHT = 480
FPS = 30  # Frames per second

# define colors ( just for educational purposes)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize Pygame and create window
pygame.init()  # start pygame library
pygame.mixer.init()  # start sounds library
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # define windows and window's size
pygame.display.set_caption("Razorcop")  # name on the windows bar
icon = pygame.image.load("icon_Ship.png")  # load icon image
pygame.display.set_icon(icon)
icon = pygame.image.load("icon_Ship.png")
clock = pygame.time.Clock()  # create an object to help track time


all_sprites = pygame.sprite.Group()  # Object with name Group for all the sprites

# Game Loop

running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)  # tells pygame to figure out how long the loop took.

    # Process input (events)
    for event in pygame.event.get():  # track for events inside the loop (keys events per example)
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    # Updates
    all_sprites.update()  # updates sprites

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)  # draws sprites group on the "screen" variable
    pygame.display.flip()  # Double Buffering refresh optimization (after drawing everything flips the display).

pygame.quit()
