import pygame
class City():
    def __init__(self,screen):
        self.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
        width=screen.get_width()
        height=screen.get_height()
        screen.blit(pygame.image.load("Graphics/heal.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/upgrade.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/leave.png").convert(), (width * 0.75, height * 0.8))