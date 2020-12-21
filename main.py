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
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # define window's size
pygame.display.set_caption("Razorcop")  # Name on the windows bar
icon = pygame.image.load("icon_Ship.png")
clock = pygame.time.Clock()  # create an object to help track time
# Game Loop

running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():  # track for events inside the loop (keys events per example)
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    # Updates
    # Draw / Render
    screen.fill(BLACK)
    pygame.display.flip()  # Double Buffering refresh optimization (after drawing everything flips the display).

pygame.quit()
