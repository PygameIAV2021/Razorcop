# pygame Razorcop code all rights reserved.
# Juan Jose Rodriguez Luis - 2021.

import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'images')  # import images directory
ani_dir = path.join(path.dirname(__file__), 'sprite_animations')  # import sounds directory
fnt_dir = path.join(path.dirname(__file__), 'fonts')  # import fonts
hsc_dir = path.join(path.dirname(__file__), 'highscore')  # import highscore folder

# for randoms enemies
enemies_images = []
enemies_list = ['Cangrejo.png', 'Pulga.png']
for i in enemies_list:
    enemies_images.append(pygame.image.load(path.join(img_dir, i)))

# -------------------------  hubs ------------------------------------------
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(path.join(fnt_dir, "VerminVibes1989Regular.ttf"), size)
    text_surface = font.render(text, True, Colors.white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def life_bar(surface, x, y, life):
    # if life < 0:
    # life = 0 --> debugging --> bar will not negative, because of negative length on display
    bar_length = 200
    bar_height = 10
    fill = (life / 100) * bar_length
    # border_line_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, Colors.green, fill_rect)
    if life <= 70:
        pygame.draw.rect(surface, Colors.yellow, fill_rect)
    if life <= 35:
        pygame.draw.rect(surface, Colors.red, fill_rect)
    # pygame.draw.rect(surface, Colors.white, border_line_rect, 1)  # 4 = border line height

def lives_hub(surface, x, y, lives):
    player_live = pygame.image.load(path.join(img_dir, "Icon_Ship.png"))
    for num in range(lives):
        img_rect = player_live.get_rect()
        img_rect.x = x + 50 * num
        img_rect.y = y
        surface.blit(player_live, img_rect)

# ----------------------- Main Screen ---------------------------------------
def main_screen(surface):
    background = pygame.image.load(path.join(img_dir, 'BGBig1600.png'))
    background_rect = background.get_rect()
    surface.blit(background, background_rect)
    draw_text(surface, "RAZORCOP", 220, Screen.width / 2, Screen.height / 4)
    draw_text(surface, "Press enter to begin", 70, Screen.width / 2, Screen.height / 2 + 200)
    draw_text(surface, "Arrow keys to move, Space to fire", 30, Screen.width / 2, Screen.height - 100)
    pygame.display.flip()
    waiting = True
    clock = pygame.time.Clock()

    while waiting:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
# ----------------------------------- pause screen ---------------------------------------
def pause_screen(surface):
    draw_text(surface, "PAUSE", 150, Screen.width / 2, (Screen.height / 2) - 70)
    pygame.display.flip()
    waiting = True
    clock = pygame.time.Clock()

    while waiting:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
# ----------------------------------- Game over screen ------------------------------------
def game_over_screen(surface, score):
    background = pygame.image.load(path.join(img_dir, 'BGBig1600.png'))
    background_rect = background.get_rect()
    surface.blit(background, background_rect)
    if score < 20000:
        draw_text(surface, "GAME OVER", 200, Screen.width / 2, Screen.height / 4)
        draw_text(surface, "YOU ARE DEAD", 120, Screen.width / 2, Screen.height / 2)
        draw_text(surface, "Your score: " + str(score), 50, Screen.width / 2, Screen.height - Screen.height / 4)
        draw_text(surface, "Press ENTER to continue", 50, Screen.width / 2, Screen.height - Screen.height / 5)
    if 20000 < score < 50000:
        draw_text(surface, "GAME OVER", 200, Screen.width / 2, Screen.height / 4)
        draw_text(surface, "Come on, you can do it better!", 100, Screen.width / 2, Screen.height / 2)
        draw_text(surface, "Your score: " + str(score), 50, Screen.width / 2, Screen.height - Screen.height / 4)
        draw_text(surface, "Press ENTER to continue", 50, Screen.width / 2, Screen.height - Screen.height / 5)
    if 50000 < score < 100000:
        draw_text(surface, "GAME OVER", 200, Screen.width / 2, Screen.height / 4)
        draw_text(surface, "NICE HIGHSCORE!!!", 130, Screen.width / 2, Screen.height / 2)
        draw_text(surface, "Your score: " + str(score), 50, Screen.width / 2, Screen.height - Screen.height / 4)
        draw_text(surface, "Press ENTER to continue", 50, Screen.width / 2, Screen.height - Screen.height / 5)
    if 100000 < score < 150000:
        draw_text(surface, "GAME OVER", 200, Screen.width / 2, Screen.height / 4)
        draw_text(surface, "THAT WAS AMAZING!!!", 130, Screen.width / 2, Screen.height / 2)
        draw_text(surface, "Your score: " + str(score), 50, Screen.width / 2, Screen.height - Screen.height / 4)
        draw_text(surface, "Press ENTER to continue", 50, Screen.width / 2, Screen.height - Screen.height / 5)
    if 150000 < score < 200000:
        draw_text(surface, "GAME OVER", 200, Screen.width / 2, Screen.height / 4)
        draw_text(surface, "YOU ARE UNBELIEVABLE!!!", 140, Screen.width / 2, Screen.height / 2)
        draw_text(surface, "Your score: " + str(score), 50, Screen.width / 2, Screen.height - Screen.height / 4)
        draw_text(surface, "Press ENTER to continue", 50, Screen.width / 2, Screen.height - Screen.height / 5)
    pygame.display.flip()
    waiting = True
    clock = pygame.time.Clock()

    while waiting:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
# ----------------------- classes -------------------------------------------------

class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    pink = (255, 111, 255)

class Screen:
    width = 1600
    height = 900
    # display = pygame.display.set_mode((width, height))  # define windows and window's size (attribute blit)
    display = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)
    icon = pygame.image.load(path.join(img_dir, "Icon_Ship.png"))  # load icon image
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Razorcop")

class Player(pygame.sprite.Sprite, Screen):   # class child of pygame.sprite.Sprite
    def __init__(self):  # initializer can accept any number of Group instances that the Sprite will become a member of.
        pygame.sprite.Sprite.__init__(self)
        # class Sprite: simple base class for visible game objects.
        # we need to call the init from the superclass, because i created a child class for player
        self.image = pygame.image.load(path.join(img_dir, "Player_Ship.png"))
        self.rect = self.image.get_rect()  # it takes image and draws a rect around, useful to Coordinates-values-
        self.radius = int(self.rect.width * .80 / 2)  # for pygame.sprite.collide_circle
        # pygame.draw.circle(self.image, Colors.red, self.rect.center, self.radius)
        self.rect.center = [Screen.width / 2, Screen.height - 100]
        self.speed = 10
        self.speedx = 0
        self.speedy = 0
        self.life = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()  # time checkpoint on screen

    def update(self):  # Movement speedx,y and centerx,y are from Base-class
        # to unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:  # time while hiding
            self.hidden = False
            self.rect.center = [Screen.width / 2, Screen.height - 100]

        if not self.hidden:  # if the ship ist not on Screen, will not able to move
            self.speedx = 0
            self.speedy = 0
            key_state = pygame.key.get_pressed()
            if key_state[pygame.K_LEFT] and (self.rect.left > 0):
                self.speedx -= self.speed
            if key_state[pygame.K_RIGHT] and (self.rect.right < Screen.width):
                self.speedx = self.speed
            if key_state[pygame.K_LEFT] and key_state[pygame.K_RIGHT]:
                self.speedx = 0
            self.rect.x += self.speedx

            if key_state[pygame.K_UP] and (self.rect.top > 0):
                self.speedy -= self.speed
            if key_state[pygame.K_DOWN] and (self.rect.bottom < Screen.height):
                self.speedy = self.speed
            if key_state[pygame.K_UP] and key_state[pygame.K_DOWN]:
                self.speedy = 0
            self.rect.y += self.speedy

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()  # time checkpoint out from screen
        self.rect.center = (Screen.width / 2, Screen.height + 300)  # set the ship out from game screen

    def create_bullet(self):  # player.create_bullet calls this function
        return Bullet(self.rect.centerx, self.rect.top)

class ExplosionPlayer(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []  # amazing, pycharm really take care about your grammar by programming image/images
        for number in range(7):
            img = pygame.image.load(path.join(ani_dir, f'ExploRazor{number}.png'))
            self.images.append(img)  # appends to the images list
        self.index = 0  # to get always the first picture every time a instance ist created
        self.image = self.images[self.index]  # accessing to the image from the list
        self.rect = self.image.get_rect()  # it takes image and draws a rect around, useful to Coordinates-values-
        self.rect = self.image.get_rect(center=(pos_x, pos_y))  # position for the rectangle with the image on it
        self.counter = 0  # takes the 0 from index to counter

    def update(self):
        explosion_speed = 10  # setting the rate which images update
        '''Counter will reaches explosion_speed by each rate, if 
                        explosion ist higher, Counter needs more time to reach it'''
        # update explosion animation
        self.counter += 1  # to increase at each iteration
        '''if the counter reach the end of the list, reset the counter'''
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        '''if the animation ist complete, reset the animation index'''
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()  # once it comes to the end of the list, kill the animation instance

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):  # parameter from Player rect position
        pygame.sprite.Sprite.__init__(self)  # class Sprite: simple base class for visible game objects.
        self.image = pygame.image.load(path.join(img_dir, "Bullet.png"))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.radius = int(self.rect.width * .30 / 2)
        #  pygame.draw.circle(self.image, Colors.red, self.rect.center, self.radius)

    def update(self):
        self.rect.y -= 16
        if self.rect.bottom < 0:
            self.kill()  # if the bullet is beyond from the screen limits, will be delete

class Enemy(pygame.sprite.Sprite, Screen):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(enemies_images)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .70 / 2)  # for pygame.sprite.collide_circle
        # pygame.draw.circle(self.image, Colors.green, self.rect.center, self.radius)
        self.rect.x = random.randrange(200, Screen.width - 200)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(2, 4)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > Screen.height + 50:
            self.rect.x = random.randrange(200, Screen.width - 200)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-2, 2)
            self.speedy = random.randrange(2, 4)

class ExplosionEnemies(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []  # amazing, pycharm really take care about your grammar by programming image/images
        for number in range(7):
            img = pygame.image.load(path.join(ani_dir, f'Explosiones{number}.png'))
            self.images.append(img)  # appends to the images list
        self.index = 0  # to get always the first picture every time a instance ist created
        self.image = self.images[self.index]  # accessing to the first image from the list
        self.rect = self.image.get_rect()  # it takes image and draws a rect around, useful to Coordinates-values-
        self.rect = self.image.get_rect(center=(pos_x, pos_y))  # position for the rectangle with the image on it
        self.counter = 0  # takes the 0 from index to counter

    def update(self):
        explosion_speed = 4  # setting the rate which images update,  1 faster than 2 and then. Images repeats 5 times
        # update explosion animation
        self.counter += 1  # to increase at each iteration to select images from the list
        '''if the counter reach the end of the list, update + 1 > len -1'''
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1  # for the access to the next image from the list
            self.image = self.images[self.index]  #
        '''if the animation ist complete, reset the animation index'''
        if self.index >= len(self.images) - 1:
            self.kill()  # once it comes to the end of the list, deletes the animation instance
