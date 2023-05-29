import pygame
from pynput import mouse


class BattleView:
    def __init__(self, flag, runSuccesful):
        self.flag = flag
        self.runSuccesful = runSuccesful

    def startBattle(self, screen, player, enemy, attack, defend, runAttempt, runSuccesful,click):
        playerRatio = player.hp / player.maxhp
        enemyRatio = enemy.hp / enemy.maxhp
        width = screen.get_width()
        height = screen.get_height()
        screen.blit(pygame.image.load("Graphics/attack.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/defend.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/runAttempt.png").convert(), (width * 0.75, height * 0.8))
        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.15, height * 0.5))
        screen.blit(pygame.image.load("Graphics/OgreInFight.png").convert_alpha(), (width * 0.7, height * 0.4))
        pygame.draw.rect(screen, "red", (width*0.13, height*0.23, width*0.15, height*0.04))
        pygame.draw.rect(screen, "green", (width*0.13, height*0.23, width*0.15*playerRatio, height*0.04))
        pygame.draw.rect(screen, "red", (width*0.78, height*0.23, width*0.15, height*0.04))
        pygame.draw.rect(screen, "green", (width*0.78, height*0.23, width*0.15 * enemyRatio, height*0.04))
        font = pygame.font.SysFont(None, 40)
        playerHpImg = font.render('Życie gracza', True, "black")
        enemyHpImg = font.render('Życie przeciwnika', True, "black")
        screen.blit(playerHpImg, (300, 250))
        screen.blit(enemyHpImg, (1525, 250))
        if attack:
            enemy.getDamage(player.strength)
            player.getDamage(enemy.strength)
        if defend:
            player.armor = player.armor + 1
            player.getDamage(enemy.strength)
            player.armor = player.armor -1
        if runAttempt:
            #self.flag = False
            player.player_pos.y = player.player_pos.y + 50
            self.runSuccesful = True
