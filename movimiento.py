import pygame
from pygame import sprite, transform, key
from pygame.locals import *

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
screen_fill = (255,255,0)

class GameSprite(sprite.Sprite):
    def __init__(self, img: str, speed: int, position: (int, int)):
        sprite.Sprite.__init__(self)


        self.image = transform.scale(pygame.image.load(img), (80, 80))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]


    def reset(self):
        screen.blit(
            self.image,
            (self.rect.x, self.rect.y)
        )

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


player = Player("m1.png", 5, (80, 80))



run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        