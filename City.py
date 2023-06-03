import pygame
class City():
    def __init__(self,screen):
        self.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
    def enterCity(self,screen,heal,upgrade,leave,player,background):
        width=screen.get_width()
        height=screen.get_height()
        background = pygame.image.load("Graphics/city.png").convert_alpha()
        self.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        background = pygame.transform.scale(background, (width, height))
        occupied = True
        screen.blit(pygame.image.load("Graphics/heal.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/upgrade.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/leave.png").convert(), (width * 0.75, height * 0.8))
        if heal:
            player.hp = player.maxhp
        elif upgrade:
            print("Do zaimplementowania")



