# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2020.

import pygame
import module as mod

FPS = 120  # Frames per second

# initialize Pygame and create window

pygame.init()  # start pygame library
pygame.mixer.init()  # start sounds library
screen = pygame.display.set_mode((mod.Screensize.width, mod.Screensize.height))  # define windows and window's size
icon = pygame.image.load("icon_Ship.png")  # load icon image
pygame.display.set_icon(icon)
pygame.display.set_caption("Razorcop")
clock = pygame.time.Clock()  # create an object to help track time

# Scrolling Background
background = pygame.image.load("BGBig1600.png").convert()  # (convert) Pygame reading optimize
speed_background_y = 0  # background only has movement on Y axis

# Sprite Group
player = mod.Player()  # adds sprite player to the Sprite-Group on module.py
all_sprites = pygame.sprite.Group()  # Object with name Group for all the sprites like ship an enemies
all_sprites.add(player)

bullet_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
for e in range(8):
    enemy = mod.Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)  # add instance enemy to pygame.sprite.group


# Game Loop

running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)  # tells pygame to figure out how long the loop took.

    # Process input (events)
    for event in pygame.event.get():  # track for events inside the loop (keys events per example)
        if event.type == pygame.QUIT:  # check for closing window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_sprites.add(player.create_bullet())
    laser_beam = pygame.key.get_pressed()
    if laser_beam[pygame.K_b]:
        bullet_sprites.add(player.create_bullet())

    # Updates
    all_sprites.update()  # updates sprites group
    bullet_sprites.update()
    rel_y = speed_background_y % background.get_rect().height
    '''dividing speed_background_y by the width and returning the remainder, Relative X now only references
    between 0 and the width of the display surface and overlaps the empty space by updating/drawing'''

    # check to see if a bullet hits a enemy
    collisions = pygame.sprite.groupcollide(enemies, bullet_sprites, True, True)  # to enemies sprite groups collisions
    for collision in collisions:
        enemy = mod.Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    hits_to_player = pygame.sprite.spritecollide(player, enemies, False)  # to player simple Sprite collisions
    if hits_to_player:
        running = False

    # Draw / Render
    screen.blit(background, (0, rel_y - background.get_rect().height))  # blit = render
    if rel_y < mod.Screensize.height:
        screen.blit(background, (0, rel_y))
    speed_background_y += 0.5  #

    all_sprites.draw(screen)  # draws sprites group on the "screen" variable
    bullet_sprites.draw(screen)
    pygame.display.flip()  # Double Buffering refresh optimization (after drawing everything flips the display).

pygame.quit()
