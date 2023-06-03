import pygame


class Player():
    def __init__(self, player_pos, flag):
        self.image = pygame.image.load('graphics/PlayerTest.png').convert_alpha()
        self.player_pos = player_pos
        self.hp = 10
        self.exp=0
        self.agility=5
        self.strength=5
        self.maxhp=10
        self.armor=2
        self.gold=0
        if flag == True:
            self.image = pygame.image.load("Graphics/blank.png").convert_alpha()
    def getDamage(self,damage):
        self.hp=self.hp-(damage-self.armor)