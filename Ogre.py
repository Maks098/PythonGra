import pygame
import random
import threading


class Ogre():
    def __init__(self, pos, dt):
        self.image = pygame.image.load("Graphics/Ogre.png").convert_alpha()
        self.pos = pygame.Vector2(pos)
        self.influenceSpherex = pygame.Vector2(pos.x - 20, pos.x + 20)
        self.influenceSpherey = pygame.Vector2(pos.y - 20, pos.y + 30)
        self.dt = dt

    def randomWalk(self):
        isMoving = bool(random.getrandbits(1))
        if isMoving == True:
            posy = random.randint(-1, 1)
            posx = random.randint(-1, 1)
            if posy == -1:
                self.pos.y -= 100 * self.dt
            elif posy == 1:
                self.pos.y += 100 * self.dt
            if posx == -1:
                self.pos.x += -100 * self.dt
            elif posx == 1:
                self.pos.x += 100 * self.dt
