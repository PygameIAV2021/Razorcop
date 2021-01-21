# pygame Razorcop code all rights reserved.
# Art by Victor Rodriguez <https://twitter.com/pixelnacho>
# Juan Jose Rodriguez Luis - 2021.

import pygame
import module as mod
import sounds as snd
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'images')  # import images directory
snd_dir = path.join(path.dirname(__file__), 'sounds')  # import sounds directory


# ---------------------------------  initialize Pygame and create window ------------------------------------
pygame.init()  # start pygame library
screen = mod.Screen()
clock = pygame.time.Clock()  # set the game to the right speed

# --------------------------------------- load Scrolling Background ---------------------------------------
background = pygame.image.load("images\Background_final.png").convert()  # (convert) Pygame reading optimize
speed_background_y = 0  # background only has movement on Y axis

# -------------------------------------------- Sprite Groups  --------------------------------------------------
'''pygame.sprite.Group() allows me to use update and move functions, that normally are inherited from the 
   instance(sprite) class:
         instance_group --> instance_group.add(object) --> instance_group.update() --> instance_group.draw()'''

all_sprites = pygame.sprite.Group()  # Object to draw for all the sprites like ship and enemies

# player
player = mod.Player()  # adds sprite player to the Sprite-Group on module.py
explosion_player_sprite = pygame.sprite.Group()
all_sprites.add(player)

bullet_sprites = pygame.sprite.Group()

# enemies
enemies_sprites = pygame.sprite.Group()  # create a enemies Sprite-Group
explosion_enemies_sprite = pygame.sprite.Group()  # create a explosion enemies Sprite-Group
for e in range(8):
    enemy = mod.Enemy()  # itinerant from Enemy class
    all_sprites.add(enemy)  # init itinerant to update
    enemies_sprites.add(enemy)  # add instance enemy to pygame.sprite.group to use .draw

# -- data --
score = 0
# -------- Game Loop --------- Game Loop --------- Game Loop --------- Game Loop --------- Game Loop -------- Game Loop

running = True
start_game = True
game_over = False
pause = False
music = snd.Music()

while running:
    if pause:
        mod.pause_screen(screen.display)
        pause = False
    if game_over:
        mod.game_over_screen(screen.display, score)
        start_game = True
        game_over = False
        pause = False
    if start_game:
        mod.main_screen(screen.display)
        start_game = False
        player.lives = 3
        player.life = 100
        score = 0

    clock.tick(120)  # Keep loop running at the right speed
    # create object to help track time and tells pygame to figure out how long the loop took.
    # ------------------------------------------ Process input (events) -----------------------------------------------
    for event in pygame.event.get():  # track for events inside the loop (keys events per example)
        if event.type == pygame.QUIT:  # check for closing window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pause = True
            if event.key == pygame.K_SPACE and not player.hidden:
                snd.SoundFx.laser_shoot_sound.play()
                bullet_sprites.add(player.create_bullet())

    # ------------------------------------------------ Updates --------------------------------------------------
    all_sprites.update()  # updates sprites group
    bullet_sprites.update()
    explosion_enemies_sprite.update()  # to the collision function
    rel_y = speed_background_y % background.get_rect().height  # updates for the remainder from background
    '''dividing speed_background_y by the width and returning the remainder, Relative Y now only references
    between 0 and the width of the display surface and overlaps the empty space by updating/drawing'''

    # check to see if a bullet hits a enemy / enemies sprite groups collisions
    collisions = pygame.sprite.groupcollide(enemies_sprites, bullet_sprites, True, True, pygame.sprite.collide_circle)
    for collision in collisions:
        score += 1234
        random.choice(snd.SoundFx.enemy_explosions_sounds).play()
        '''Las explosiones deben ser llamadas usando la coordenada de la collision, no la del objeto impactado'''

        explosion = mod.ExplosionEnemies(collision.rect.centerx, collision.rect.centery)  # position from the collision
        all_sprites.add(explosion)
        #  create a new enemy by each collision
        enemy = mod.Enemy()  # enemy die too... i need him back to the action >:(
        all_sprites.add(enemy)  # to see them on the screen
        enemies_sprites.add(enemy)  # refresh to get properties from them

    # to player simple Sprite collisions
    hits_to_player = pygame.sprite.spritecollide(player, enemies_sprites, True, pygame.sprite.collide_circle)
    for hit in hits_to_player:
        player.life -= 100 / 3  # 3 shoots to DIE :'(
        if 100 > player.life > 1:
            snd.SoundFx.damage_sound.play()
        if 35 > player.life > 5:
            snd.SoundFx.alert_sound.play()
        if player.life <= 0:
            snd.SoundFx.explosion_ship_sound.play()
            explosion_player = mod.ExplosionPlayer(player.rect.centerx, player.rect.centery)
            all_sprites.add(explosion_player)
            player.hide()
            player.lives -= 1
            player.life = 100
            if player.lives == 0:
                player.life = 0

        # enemies explosion
        explosion = mod.ExplosionEnemies(hit.rect.centerx, hit.rect.centery)  # position from the collision
        all_sprites.add(explosion)
        # for more enemies incoming after the collision
        enemy = mod.Enemy()  # enemy die too... i need him back to the action >:(
        all_sprites.add(enemy)  # to see them on the screen
        enemies_sprites.add(enemy)  # refresh to get properties from them
        # if the player died and the explosion has finished playing
    if player.lives == 0 and not explosion_player.alive():
        game_over = True
    # ----------------------------------------------- Draw / Render --------------------------------------------------
    # Press start Menu
    # Scrolling Background
    screen.display.blit(background, (0, rel_y - background.get_rect().height))  # blit = render
    if rel_y < screen.height:
        screen.display.blit(background, (0, rel_y))
    speed_background_y += 1  # 1 pixel pro frame

    # draws sprites group on the "screen" variable
    all_sprites.draw(screen.display)
    bullet_sprites.draw(screen.display)
    explosion_player_sprite.draw(screen.display)
    explosion_enemies_sprite.draw(screen.display)
    # Score table
    mod.draw_text(screen.display, "Score: " + str(score), 40, screen.width - 150, 35)  # Python ist schööön!!!
    # life bar
    mod.life_bar(screen.display, 60, 40, player.life)
    # Hub lives
    mod.lives_hub(screen.display, 90, 70, player.lives)
    # Double Buffering refresh optimization (after drawing everything flips the display).
    pygame.display.flip()


pygame.quit()
