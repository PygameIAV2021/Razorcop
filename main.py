# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2020.

import pygame
import module as mod

FPS = 120  # Frames per second

# initialize Pygame and create window

pygame.init()  # start pygame library
pygame.mixer.init()  # start sounds library
screen = pygame.display.set_mode((mod.Screensize.width, mod.Screensize.height))  # define windows and window's size
pygame.display.set_caption("Razorcop")  # name on the windows bar
icon = pygame.image.load("icon_Ship.png")  # load icon image
pygame.display.set_icon(icon)
clock = pygame.time.Clock()  # create an object to help track time

# Scrolling Background
background = pygame.image.load("BGBig1600.png").convert()  # (convert) Pygame reading optimize
speed_background_y = 0  # background only has movement on Y axis


# Sprite Group
player = mod.Player()  # adds sprite player to the Sprite-Group on module.py
all_sprites = pygame.sprite.Group()  # Object with name Group for all the sprites like ship an enemies
all_sprites.add()
all_sprites.add(player)


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
    rel_y = speed_background_y % background.get_rect().height
    '''dividing speed_background_y by the width and returning the remainder, Relative X now only references
    between 0 and the width of the display surface and overlaps the empty space by updating/drawing'''

    # Draw / Render
    screen.blit(background, (0, rel_y - background.get_rect().height))  # blit = render
    if rel_y < mod.Screensize.height:
        screen.blit(background, (0, rel_y))
    speed_background_y += 0.3  #

    all_sprites.draw(screen)  # draws sprites group on the "screen" variable
    pygame.display.flip()  # Double Buffering refresh optimization (after drawing everything flips the display).

pygame.quit()
