# This ist a Shoot em up game coded by Juan Rodriguez
import pygame, sys, time
from pygame.locals import *

pygame.init()
FPS = 120


# Initialize the Pygame.
pygame.init()

#  classes
#  ----------------------------- Objects -------------------------------------
clock = pygame.time.Clock()

background = pygame.image.load('BGBig1600.png')

# Create the Screen.
screenWidth = 1600
screenHeight = 900
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Title and icon on the window bar mas 32px
pygame.display.set_caption("Razorcop")  # set windows Title.
icon = pygame.image.load("Ship.png")  # Load tiny icon image
pygame.display.set_icon(icon)   # set icon.

# La nave de Razorcop!
playerImg = pygame.image.load("Player_Ship.png")  # Image Loading
playerX = 730  # places the x coord. for PlayerImg object in the middle
playerY = 700  # places the y coord. for PlayerImg object in the middle
playerX_change = 0 # New coordinate point for X
playerY_change = 0  # New coordinate point for y
player_left = False
player_right = False
player_up = False
player_down = False
player_vel = 10

def player(x, y):
    screen.blit(playerImg, (x, y))  # The term used for rendering objects is blitting


# The window will close in few seconds, we need a while loop (or game loop).
# We need also a quit function (pygame.quit)


# Game Loop
running = True
while running:  # While running ist True, window stay open.
    clock.tick(FPS)
    screen.fill((0, 0, 0))  # Python needs updates from these changes, so we need a method for it.
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # take care about the QUIT characters (activates when the [x] button on window)
            running = False
        # Movement

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > player_vel:
        playerX -= player_vel
        player_left = True
        player_right = False
    elif keys[pygame.K_RIGHT] and playerX < screenWidth - 128 - player_vel:
        playerX += player_vel
        player_right = True
        player_left = False

    if keys[pygame.K_UP] and playerY > player_vel:
        playerY -= player_vel
        player_up = True
        player_down = False
    elif keys[pygame.K_DOWN] and playerY < screenHeight - 128 - player_vel :
        playerY += player_vel
        player_up = False
        player_down = True

    player(playerX, playerY)  # Function for Player_ship will be called here
    pygame.display.update()

