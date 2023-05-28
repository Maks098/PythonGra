import pygame
from pynput import mouse


class BattleView:
    def __init__(self, flag):
        self.flag=flag

    def startBattle(self, screen, player, enemy, attack):
        playerRatio=player.hp/player.maxhp
        enemyRatio=enemy.hp/enemy.maxhp
        width=screen.get_width()
        height=screen.get_height()
        if (player.hp <= 0) | (enemy.hp <= 0):
            self.flag = False
        font = pygame.font.Font('freesansbold.ttf', 32)
        screen.blit(pygame.image.load("Graphics/Atakuj.png").convert(), (width*0.11, height*0.80))
        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width*0.15, height*0.5))
        screen.blit(pygame.image.load("Graphics/OgreInFight.png").convert_alpha(), (width * 0.7, height * 0.4))
        pygame.draw.rect(screen,"red",(250,250,300,40))
        pygame.draw.rect(screen, "green", (250, 250, 300*playerRatio, 40))
        pygame.draw.rect(screen, "red", (1500, 250, 300, 40))
        pygame.draw.rect(screen, "green", (1500, 250, 300 * enemyRatio, 40))
        font = pygame.font.SysFont(None, 40)
        playerHpImg = font.render('Życie gracza', True, "black")
        enemyHpImg = font.render('Życie przeciwnika', True, "black")
        screen.blit(playerHpImg, (300,250))
        screen.blit(enemyHpImg, (1525, 250))
        if (attack==True):
            enemy.getDamage(player.strength)
            player.getDamage(enemy.strength)
            print("HP GRACZA: "+str(player.hp))







    def dealDamage(self,enemy,damage):
        return enemy.hp-damage

