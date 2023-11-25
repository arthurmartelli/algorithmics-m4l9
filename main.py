import pygame
import window

screen = window.init()

GAME_STATE = {
    'running': True
}

while GAME_STATE['running']:

    # Stop the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATE['running'] = False
