import pygame
from pynput import mouse


class BattleView:
    def __init__(self, screen, player, flag,background):
        #self.enemy = enemy
        self.flag=flag
        self.player = player
        #self.startBattle(screen, player, enemy, flag,background)

#a
    def startBattle(self, screen, player, enemy, flag,background):
        playerRatio=player.hp/player.maxhp
        enemyRatio=enemy.hp/enemy.maxhp
        if (player.hp <= 0) | (enemy.hp <= 0):
            self.flag = False
        font = pygame.font.Font('freesansbold.ttf', 32)
        screen.blit(pygame.image.load("Graphics/Atakuj.png").convert(), (500, 400))
        screen.blit(pygame.image.load("Graphics/PlayerTest.png").convert_alpha(), (800, 400))
        pygame.draw.rect(screen,"red",(250,250,300,40))
        pygame.draw.rect(screen, "green", (250, 250, 300*playerRatio, 40))
        pygame.draw.rect(screen, "red", (1500, 250, 300, 40))
        pygame.draw.rect(screen, "green", (1500, 250, 300 * enemyRatio, 40))
        font = pygame.font.SysFont(None, 40)
        playerHpImg = font.render('Życie gracza', True, "black")
        enemyHpImg = font.render('Życie przeciwnika', True, "black")
        screen.blit(playerHpImg, (300,250))
        screen.blit(enemyHpImg, (1525, 250))
        if ((pygame.mouse.get_pressed()[0] == 1) & (pygame.mouse.get_pos() < (600, 500)) & (
                pygame.mouse.get_pos() > (400, 300))):


            enemy.getDamage(player.strength)
            player.getDamage(enemy.strength)
            print("HP GRACZA: "+str(player.hp))







    def dealDamage(self,enemy,damage):
        return enemy.hp-damage


