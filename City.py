import pygame
class City():
    def __init__(self,screen):
        self.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
        width=screen.get_width()
        height=screen.get_height()
