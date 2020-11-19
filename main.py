# This ist a Shoot em up game coded by Juan Rodriguez
import pygame

# Initialize the Pygame.
pygame.init()

#  classes
#  ----------------------------- Objects -------------------------------------
#  Background
background = pygame.image.load('BG_SHIP.jpeg')

# Create the Screen.
screen = pygame.display.set_mode((1600, 900))

# Title and icon on the window bar mas 32px
pygame.display.set_caption("Razorcop")  # set windows Title.
icon = pygame.image.load("Ship.png")  # Load tiny icon image
pygame.display.set_icon(icon)   # set icon.

# La nave de Razorcop!
playerImg = pygame.image.load("Player_Ship.png")  # Image Loading
playerX = 735  # places the x coord. for PlayerImg object in the middle
playerY = 700  # places the y coord. for PlayerImg object in the middle
playerX_change = 0  # New coordinate point for X
playerY_change = 0  # New coordinate point for y

def player(x,y):
    screen.blit(playerImg, (x, y))  # The term used for rendering objects is blitting


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
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change -= 0.01
        if event.key == pygame.K_RIGHT:
            playerX_change += 0.01
        if event.key == pygame.K_UP:
            playerY_change -= 0.01
        if event.key == pygame.K_DOWN:
            playerY_change += 0.01
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
            playerX_change = 0.0

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)  # Function  for Player_ship will be called here
    pygame.display.update()
