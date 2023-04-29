import pygame
import random
import threading


class Ogre():
    def __init__(self, pos, dt,flag):
        self.image = pygame.image.load("Graphics/Ogre.png").convert_alpha()
        self.pos = pygame.Vector2(pos)
        self.influenceSpherex = pygame.Vector2(pos.x - 20, pos.x + 20)
        self.influenceSpherey = pygame.Vector2(pos.y - 20, pos.y + 30)
        self.dt = dt
        self.hp=15
        self.flag=flag
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

