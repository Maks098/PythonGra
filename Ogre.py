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
        self.strength=3
        self.agility=2
        self.maxhp=hp
        self.armor=1
        if flag==True:
            self.image=pygame.image.load("Graphics/blank.png").convert_alpha()




    def randomWalk(self):
        if self.flag==False:
            isMoving = bool(random.getrandbits(1))
            if isMoving == True:
                posy = random.randint(-1, 10)
                posx = random.randint(-1, 10)
                if posy == -1:
                    self.pos.y -= 100 * self.dt
                elif posy == 1:
                    self.pos.y += 100 * self.dt
                if posx == -1:
                    self.pos.x += -100 * self.dt
                elif posx == 1:
                    self.pos.x += 100 * self.dt

    def getDamage(self,damage):
        self.hp=self.hp-(damage-self.armor)

    def updateSOF(self):
        self.influenceSpherex = pygame.Vector2(self.pos.x - 20, self.pos.x + 20)
        self.influenceSpherey = pygame.Vector2(self.pos.y - 20, self.pos.y + 30)