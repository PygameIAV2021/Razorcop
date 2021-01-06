# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2020.

import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'images')  # import images directory
snd_dir = path.join(path.dirname(__file__), 'sounds')  # import sounds directory

# for randoms enemies
enemies_images = []
enemies_list = ['Cangrejo.png', 'Pulga.png']
for i in enemies_list:
    enemies_images.append(pygame.image.load(path.join(img_dir, i)))

font_name = pygame.font.match_font('verdana')
def score_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, Colors.white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def life_bar(surface, x, y, life):
    # if life < 0:
    # life = 0 --> debugging --> bar will not negative, because of negative length on display
    bar_length = 200
    bar_height = 15
    fill = (life / 100) * bar_length
    border_line_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, Colors.green, fill_rect)
    if life <= 70:
        pygame.draw.rect(surface, Colors.yellow, fill_rect)
    if life <= 35:
        pygame.draw.rect(surface, Colors.red, fill_rect)
    pygame.draw.rect(surface, Colors.white, border_line_rect, 2)  # 4 = border line height

class Screensize:
    width = 1600
    height = 900


class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):  # initializer can accept any number of Group instances that the Sprite will become a member of.
        pygame.sprite.Sprite.__init__(self)  # class Sprite: simple base class for visible game objects.
        self.image = pygame.image.load(path.join(img_dir, "Player_Ship.png"))
        self.rect = self.image.get_rect()  # it takes image and draws a rect around, useful to Coordinates-values-
        self.radius = int(self.rect.width * .80 / 2)  # for pygame.sprite.collide_circle
        #  pygame.draw.circle(self.image, Colors.red, self.rect.center, self.radius)
        self.rect.center = [Screensize.width / 2, Screensize.height - (Screensize.height / 4)]
        self.speed = 6
        self.speedx = 0
        self.speedy = 0
        self.life = 100

    def update(self):  # Movement speedx,y and centerx,y are from Base-class
        self.speedx = 0
        self.speedy = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT] and (self.rect.left > 0):
            self.speedx -= self.speed
        if key_state[pygame.K_RIGHT] and (self.rect.right < Screensize.width):
            self.speedx = self.speed
        if key_state[pygame.K_LEFT] and key_state[pygame.K_RIGHT]:
            self.speedx = 0
        self.rect.x += self.speedx

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_UP] and (self.rect.top > 0):
            self.speedy -= self.speed
        if key_state[pygame.K_DOWN] and (self.rect.bottom < Screensize.height):
            self.speedy = self.speed
        if key_state[pygame.K_UP] and key_state[pygame.K_DOWN]:
            self.speedy = 0
        self.rect.y += self.speedy

    def create_bullet(self):  # player.create_bullet calls this function
        return Bullet(self.rect.centerx, self.rect.top)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):  # parameter from Player rect position
        pygame.sprite.Sprite.__init__(self)  # class Sprite: simple base class for visible game objects.
        self.image = pygame.image.load(path.join(img_dir, "Bullet.png"))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.radius = int(self.rect.width * .30 / 2)
        #  pygame.draw.circle(self.image, Colors.red, self.rect.center, self.radius)

    def update(self):  # for movements
        self.rect.y -= 12
        if self.rect.bottom < 0:  # if the bullet is beyond from the screen limits, will be delete
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(enemies_images)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .70 / 2)  # for pygame.sprite.collide_circle
        #  pygame.draw.circle(self.image, Colors.green, self.rect.center, self.radius)
        self.rect.x = Screensize.width / 2
        self.rect.y = random.randrange(-100, -40)
        self.speedx = 0
        self.speedy = random.randrange(2, 8)

    '''def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        follow_vector = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        follow_vector.normalize()
        # Move along this normalized vector towards the player at current speed.
        follow_vector.scale_to_length(self.speed)
        self.rect.move_ip(follow_vector)'''

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > Screensize.height + 50:
            self.rect.x = random.randrange(200, Screensize.width - 200)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-2, 2)
            self.speedy = random.randrange(2, 8)
            if self.rect.centery <= 200:
                self.speedy = random.randrange(2, 8)
            if self.rect.centery > Screensize.width + 200:
                self.speedy = random.randrange(-8, -6)
