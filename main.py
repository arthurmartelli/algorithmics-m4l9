import pygame
import window

screen = window.init()
backround_color = (255,255,255)

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
