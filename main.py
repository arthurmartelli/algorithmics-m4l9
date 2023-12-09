from typing import Any
import pygame
from pygame.sprite import Group


width,height = 800,600
screen = pygame.display.set_mode((width,height))
backround_color = (0,255,255)

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y) :
        super(Player,self).__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((0,126,255))
        self.rect = self.image.get_rect
        self.rect.center = (x,y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5 
        if keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.y += 5

player = Player(width//2 , height//2)


# Game state variable
GAME_STATE = {
    'running': True
}

while GAME_STATE['running']:

    # Stop the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATE['running'] = False

        screen.fill(backround_color)
        player.update()
        
        
