import pygame


class Menu():
    def menu(self, screen, resume, exitButton, occupied, menu):
        width = screen.get_width()
        height = screen.get_height()
        pauseBackground = pygame.Surface((width, height))
        pauseBackground.set_alpha(150)
        pauseBackground.fill((0, 0, 0))

        screen.blit(pauseBackground, (0, 0))
        pause = pygame.image.load("Graphics/pause.png").convert()
        pauseRect = pause.get_rect()
        pauseRect.center = (width / 2, height / 2)
        screen.blit(pause, pauseRect)
        if resume:
            occupied = False
            menu = False
        elif exitButton:
            exit(0)
