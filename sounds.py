# pygame Razorcop code all rights reserved.
# all the sounds effects were created with Bfxr VST <https://www.bfxr.net/> please support developer's patreon
# Sound effects by Juan Jose Rodriguez Luis - 2021.

import pygame
from os import path

pygame.mixer.init()  # start sounds library
snd_dir = path.join(path.dirname(__file__), 'sounds')  # import sounds directory


# Razorcop sound
class Music:
    def __init__(self):
        pygame.mixer.music.load(path.join(snd_dir, 'Columns_III.mp3'))
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(loops=-1)  # -1 infinite playback
        self.pause = False
        if self.pause:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()


class SoundFx:
    # Player's sound
    laser_shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'Laser_Shoot_6.wav'))
    pygame.mixer.Sound.set_volume(laser_shoot_sound, 0.7)
    laser_beam_sound = pygame.mixer.Sound(path.join(snd_dir, 'Laser_Shoot_4.wav'))
    pygame.mixer.Sound.set_volume(laser_beam_sound, 0.2)
    damage_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_enemy_6.wav'))
    pygame.mixer.Sound.set_volume(damage_sound, 0.7)
    explosion_ship_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion_Ship_3.wav'))
    pygame.mixer.Sound.set_volume(explosion_ship_sound, 0.7)
    alert_sound = pygame.mixer.Sound(path.join(snd_dir, 'Alert_2.wav'))
    pygame.mixer.Sound.set_volume(alert_sound, 0.4)

    # Enemy's sound
    enemy_explosions_sounds = []  # to save the file / has the attribute .play
    enemy_explosions_sounds_list = ['Explosion_Enemy_4.wav', 'Explosion_Enemy_5.wav']
    for explosion in enemy_explosions_sounds_list:
        kaboom = pygame.mixer.Sound(path.join(snd_dir, explosion))
        pygame.mixer.Sound.set_volume(kaboom, 0.6)
        enemy_explosions_sounds.append(kaboom)
