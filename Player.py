import pygame


class Player():
    def __init__(self, player_pos, flag):
        self.image = pygame.image.load('graphics/PlayerTest.png').convert_alpha()
        self.player_pos = player_pos
        self.hp = 10
        if flag == True:
            self.image = pygame.image.load("Graphics/blank.png").convert_alpha()
