import pygame

pygame.display.init()  # initialize display
display_info = pygame.display.Info()  # get display info


WINDOW_SETTINGS = {
    # width, height
    'SCREEN_SIZE': (display_info.current_w, display_info.current_h),
    'CAPTION': "Arcade Game"
}


def init():
    global WINDOW_SETTINGS
    pygame.init()
    pygame.display.set_caption(WINDOW_SETTINGS['CAPTION'])
    screen = pygame.display.set_mode(
        WINDOW_SETTINGS['SCREEN_SIZE'], pygame.RESIZABLE)

    return screen
