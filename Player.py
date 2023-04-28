import pygame


class Player():
    def __init__(self,player_pos):
        self.image = pygame.image.load('graphics/PlayerTest.png').convert_alpha()
        self.player_pos=player_pos




