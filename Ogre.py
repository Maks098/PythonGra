import pygame
import random
import threading


class Ogre():
    def __init__(self, pos, dt,flag,hp):
        self.image = pygame.image.load("Graphics/Ogre.png").convert_alpha()
        self.pos = pygame.Vector2(pos)
        self.influenceSpherex = pygame.Vector2(self.pos.x - 20, self.pos.x + 20)
        self.influenceSpherey = pygame.Vector2(self.pos.y - 20, self.pos.y + 20)
        self.dt = dt
        self.hp=hp
        self.flag=flag
        self.strength=4
        self.agility=2
        self.maxhp=hp
        self.armor=1
        if flag==True:
            self.image=pygame.image.load("Graphics/blank.png").convert_alpha()

    def getDamage(self,damage):
        self.hp=self.hp-(damage-self.armor)

    def updateSOF(self):
        self.influenceSpherex = pygame.Vector2(self.pos.x - 20, self.pos.x + 20)
        self.influenceSpherey = pygame.Vector2(self.pos.y - 20, self.pos.y + 30)
