# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2021.

import pygame
import module as mod
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'images')  # import images directory
snd_dir = path.join(path.dirname(__file__), 'sounds')  # import sounds directory


# ---------------------------------  initialize Pygame and create window ------------------------------------
pygame.init()  # start pygame library
pygame.mixer.init()  # start sounds library
screen = pygame.display.set_mode((mod.Screensize.width, mod.Screensize.height))  # define windows and window's size
# screen = pygame.display.set_mode((mod.Screensize.width, mod.Screensize.height), pygame.FULLSCREEN, 32)
icon = pygame.image.load(path.join(img_dir, "Icon_Ship.png"))  # load icon image
pygame.display.set_icon(icon)
pygame.display.set_caption("Razorcop")
FPS = 120  # Frames per second
clock = pygame.time.Clock()  # create an object to help track time

# --------------------------------------  load Sounds effects and music --------------------------------------
# Music level 1
pygame.mixer.music.load(path.join(snd_dir, 'Columns_III.mp3'))
pygame.mixer.music.set_volume(2)

# Razorcop sound
laser_shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'Laser_Shoot_6.wav '))
laser_beam_sound = pygame.mixer.Sound(path.join(snd_dir, 'Laser_Shoot_4.wav'))
damage_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_Enemy_6.wav'))
alert_sound = pygame.mixer.Sound(path.join(snd_dir, 'Alert_2.wav'))
# enemy sound
explosions_sounds = []
explosions_sounds_list = ['Explosion_Enemy_4.wav', 'Explosion_Enemy_5.wav', 'Explosion_Enemy_6.wav']
for explosion in explosions_sounds_list:
    explosions_sounds.append(pygame.mixer.Sound(path.join(snd_dir, explosion)))
#  explosion_enemy_1 = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_Enemy_4.wav'))

# --------------------------------------- load Scrolling Background ---------------------------------------
background = pygame.image.load("images\BGBig1600.png").convert()  # (convert) Pygame reading optimize
speed_background_y = 0  # background only has movement on Y axis

# -------------------------------------------- Sprite Groups  --------------------------------------------------
player = mod.Player()  # adds sprite player to the Sprite-Group on module.py
all_sprites = pygame.sprite.Group()  # Object with name Group for all the sprites like ship an enemies
all_sprites.add(player)

bullet_sprites = pygame.sprite.Group()

# enemies
enemies = pygame.sprite.Group()
for e in range(8):
    enemy = mod.Enemy()  # itinerant from Enemy class
    all_sprites.add(enemy)
    enemies.add(enemy)  # add instance enemy to pygame.sprite.group
score = 0
pygame.mixer.music.play(loops=-1)  # -1 infinite playback

# -------- Game Loop --------- Game Loop --------- Game Loop --------- Game Loop --------- Game Loop -------- Game Loop

running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)  # tells pygame to figure out how long the loop took.

    # ------------------------------------------ Process input (events) -----------------------------------------------
    for event in pygame.event.get():  # track for events inside the loop (keys events per example)
        if event.type == pygame.QUIT:  # check for closing window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_shoot_sound.play()
                bullet_sprites.add(player.create_bullet())
    laser_beam = pygame.key.get_pressed()
    if laser_beam[pygame.K_b]:
        laser_beam_sound.play()
        bullet_sprites.add(player.create_bullet())

    # ------------------------------------------------ Updates --------------------------------------------------
    all_sprites.update()  # updates sprites group
    bullet_sprites.update()
    rel_y = speed_background_y % background.get_rect().height
    '''dividing speed_background_y by the width and returning the remainder, Relative X now only references
    between 0 and the width of the display surface and overlaps the empty space by updating/drawing'''

    # check to see if a bullet hits a enemy / enemies sprite groups collisions
    collisions = pygame.sprite.groupcollide(enemies, bullet_sprites, True, True, pygame.sprite.collide_circle)
    for collision in collisions:
        score += 1234
        random.choice(explosions_sounds).play()
        enemy = mod.Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # to player simple Sprite collisions
    hits_to_player = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
    for hit in hits_to_player:
        damage_sound.play()
        player.life -= 100 / 3  # 3 shoots to DIE :'(
        if player.life < 35:
            alert_sound.play()
        if player.life <= 0:
            running = False
        enemy = mod.Enemy()  # enemy die too... i need him back to the action >:(
        all_sprites.add(enemy)
        enemies.add(enemy)

    # ----------------------------------------------- Draw / Render --------------------------------------------------
    # Scrolling Background
    screen.blit(background, (0, rel_y - background.get_rect().height))  # blit = render
    if rel_y < mod.Screensize.height:
        screen.blit(background, (0, rel_y))
    speed_background_y += 1  #

    # draws sprites group on the "screen" variable
    all_sprites.draw(screen)
    bullet_sprites.draw(screen)

    # Score table
    mod.score_text(screen, "Score: " + str(score), 24, mod.Screensize.width - 150, 30)  # Python ist schööön!!!
    # life bar
    mod.life_bar(screen, 50, 40, player.life)
    # Double Buffering refresh optimization (after drawing everything flips the display).
    pygame.display.flip()

pygame.quit()
