# This ist a Shoot em up game coded by Juan Rodriguez
import pygame
import random  # movement update for enemies.

# from pygame.locals import *

pygame.init()
# Initialize the Pygame.

#  classes
#  ----------------------------- Objects -------------------------------------

# -------- Background ----------------------
background = pygame.image.load('BGBig1600.png')

# Create the Screen.
screenWidth = 1600
screenHeight = 900
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Title and icon on the window bar mas 32px
pygame.display.set_caption("Razorcop")  # set windows Title.
icon = pygame.image.load("Ship.png")  # Load tiny icon image
pygame.display.set_icon(icon)  # set icon.

# La nave de Razorcop!
playerImg = pygame.image.load("Player_Ship.png")  # Image Loading
playerX = (screenWidth / 2) - (128 / 2)  # places the x coord. for PlayerImg object in the middle
playerY = 700  # places the y coord. for PlayerImg object in the middle
playerX_change = 0  # New coordinate point for X
playerY_change = 0  # New coordinate point for y
player_left = False
player_right = False
player_up = False
player_down = False
player_vel = 20

# Enemy 1
enemyImg = pygame.image.load("Gegner.png")  # Image Loading
enemyX = random.randint(500 - 190, 1100)  # places the x coord. for enemyImg object in the middle
enemyY = random.randint(50, 150)  # places the y coord. for enemyImg object in the middle
enemyX_change = 15  # New coordinate point for X
enemyY_change = 7  # New coordinate point for y
enemyX_vel = 15
enemyY_vel = 7

# Bullets

# Bullet1

bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 30
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))  # The term used for rendering objects is Blitting


def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # The term used for rendering objects is Blitting


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


# The window will close in few seconds, we need a while loop (or game loop).
# We need also a quit function (pygame.quit)

# Game Loop
running = True
while running:  # While running ist True, window stay open.

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
    elif keys[pygame.K_DOWN] and playerY < screenHeight - 128 - player_vel:
        playerY += player_vel
        player_up = False
        player_down = True

    if keys[pygame.K_SPACE]:
        if bullet_state is "ready":
            bulletX = playerX
            bullet(bulletX, bulletY)

    enemyX += enemyX_change
    if enemyX <= 300:
        enemyX_change = enemyX_vel
    elif enemyX >= 1200 - 360:
        enemyX_change = -enemyX_vel

    enemyY += enemyY_change
    if enemyY <= 10:
        enemyY_change = enemyY_vel
    elif enemyY >= 100:
        enemyY_change = -enemyY_vel

    # bullet Movement

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)  # Function for Player_ship will be called here

    enemy(enemyX, enemyY)  # Function for Enemy  will be called here
    pygame.display.update()
