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
# screen = pygame.display.set_mode((mod.Screensize.width, mod.Screensize.height))  # define windows and window's size
screen = pygame.display.set_mode((mod.Screensize.width, mod.Screensize.height), pygame.FULLSCREEN, 32)
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
damage_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_enemy_6.wav'))
explosion_ship_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_Ship_3.wav'))
alert_sound = pygame.mixer.Sound(path.join(snd_dir, 'Alert_2.wav'))
# enemy sound
explosions_sounds = []
explosions_sounds_list = ['Explosion_Enemy_4.wav', 'Explosion_Enemy_5.wav']
for explosion in explosions_sounds_list:
    explosions_sounds.append(pygame.mixer.Sound(path.join(snd_dir, explosion)))
#  explosion_enemy_1 = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_Enemy_4.wav'))

# --------------------------------------- load Scrolling Background ---------------------------------------
background = pygame.image.load("images\Background_final.png").convert()  # (convert) Pygame reading optimize
speed_background_y = 0  # background only has movement on Y axis

# -------------------------------------------- Sprite Groups  --------------------------------------------------
'''pygame.sprite.Group() allows me to use update and move functions, 
    that normally are inherited from the instance(sprite) class'''

player = mod.Player()  # adds sprite player to the Sprite-Group on module.py
explosion_player_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()  # Object with name Group for all the sprites like ship an enemies
all_sprites.add(player)

bullet_sprites = pygame.sprite.Group()

# enemies
enemies = pygame.sprite.Group()  # create a enemies Sprite-Group
explosion_enemies_sprite = pygame.sprite.Group()  # create a explosion enemies Sprite-Group
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
            if event.key == pygame.K_SPACE and not player.hidden:
                laser_shoot_sound.play()
                bullet_sprites.add(player.create_bullet())
    laser_beam = pygame.key.get_pressed()
    if laser_beam[pygame.K_b] and not player.hidden:
        laser_beam_sound.play()
        bullet_sprites.add(player.create_bullet())

    # ------------------------------------------------ Updates --------------------------------------------------
    all_sprites.update()  # updates sprites group
    bullet_sprites.update()
    explosion_enemies_sprite.update()

    rel_y = speed_background_y % background.get_rect().height
    '''dividing speed_background_y by the width and returning the remainder, Relative X now only references
    between 0 and the width of the display surface and overlaps the empty space by updating/drawing'''

    # check to see if a bullet hits a enemy / enemies sprite groups collisions
    collisions = pygame.sprite.groupcollide(enemies, bullet_sprites, True, True, pygame.sprite.collide_circle)
    for collision in collisions:
        score += 1234
        random.choice(explosions_sounds).play()
        '''Madre de dios bendito, señor... Las explosiones deben ser llamadas usando la 
            coordenada de la collision, en vez del la coordenada del objeto impactado'''

        explosion = mod.ExplosionEnemies(collision.rect.centerx, collision.rect.centery)  # position from the collision
        all_sprites.add(explosion)
        #  create a new enemy by each collision
        enemy = mod.Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # to player simple Sprite collisions
    hits_to_player = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
    for hit in hits_to_player:
        player.life -= 100 / 3  # 3 shoots to DIE :'(
        if 100 > player.life > 1:
            damage_sound.play()
        if 35 > player.life > 5:
            alert_sound.play()
        if player.life <= 0:
            explosion_ship_sound.play()
            explosion_player = mod.ExplosionPlayer(player.rect.centerx, player.rect.centery)
            all_sprites.add(explosion_player)
            player.hide()
            player.lives -= 1
            player.life = 100

        # enemies explosion
        explosion = mod.ExplosionEnemies(hit.rect.centerx, hit.rect.centery)  # position from the collision
        all_sprites.add(explosion)
        # for more enemies incoming after the collision
        enemy = mod.Enemy()  # enemy die too... i need him back to the action >:(
        all_sprites.add(enemy)
        enemies.add(enemy)
        # if the player died and the explosion has finished playing
    if player.lives == 0 and not explosion_player.alive():
        running = False
    # ----------------------------------------------- Draw / Render --------------------------------------------------
    # Scrolling Background
    screen.blit(background, (0, rel_y - background.get_rect().height))  # blit = render
    if rel_y < mod.Screensize.height:
        screen.blit(background, (0, rel_y))
    speed_background_y += 1  # 1 pixel pro frame

    # draws sprites group on the "screen" variable
    all_sprites.draw(screen)
    bullet_sprites.draw(screen)
    explosion_player_sprite.draw(screen)
    explosion_enemies_sprite.draw(screen)
    # Score table
    mod.score_text(screen, "Score: " + str(score), 24, mod.Screensize.width - 150, 35)  # Python ist schööön!!!
    # life bar
    mod.life_bar(screen, 50, 40, player.life)
    # Hub lives
    mod.lives_hub(screen, 80, 70, player.lives)
    # Double Buffering refresh optimization (after drawing everything flips the display).
    pygame.display.flip()

pygame.quit()
