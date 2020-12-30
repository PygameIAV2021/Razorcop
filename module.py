# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2020.

import pygame


class Screensize:
    width = 1280
    height = 720


class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):  # initializer can accept any number of Group instances that the Sprite will become a member of.
        pygame.sprite.Sprite.__init__(self)  # class Sprite: simple base class for visible game objects.
        self.image = pygame.image.load("Player_Ship.png")
        self.rect = self.image.get_rect()  # Coordinates for instance player
        self.rect.centerx = Screensize.width / 2
        self.rect.centery = Screensize.height - (Screensize.height / 4)
        self.speed = 6
        self.speedx = 0
        self.speedy = 0

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

    def create_bullet(self):  # player.create_bullet calls this funktion
        return Bullet(self.rect.centerx, self.rect.top)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):  # parameter from Player rect position
        pygame.sprite.Sprite.__init__(self)  # class Sprite: simple base class for visible game objects.
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):  # for movements
        self.rect.y -= 12
        if self.rect.bottom < 0:  # if the bullet is beyond from the screen limits, will be delete
            self.kill()
