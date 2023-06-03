import random

import pygame


class BattleView:
    def __init__(self, flag, runSuccesful):
        self.flag = flag
        self.runSuccesful = runSuccesful
        self.i=0
        self.playerLog=False

    def startBattle(self, screen, player, enemy, attack, defend, runAttempt, runSuccesful, click):

        playerRatio = player.hp / player.maxhp
        enemyRatio = enemy.hp / enemy.maxhp
        width = screen.get_width()
        height = screen.get_height()

        screen.blit(pygame.image.load("Graphics/attack.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/defend.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/runAttempt.png").convert(), (width * 0.75, height * 0.8))
        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.15, height * 0.5))
        screen.blit(pygame.image.load("Graphics/OgreInFight.png").convert_alpha(), (width * 0.7, height * 0.4))
        pygame.draw.rect(screen, "red", (width * 0.13, height * 0.23, width * 0.15, height * 0.04))
        pygame.draw.rect(screen, "green", (width * 0.13, height * 0.23, width * 0.15 * playerRatio, height * 0.04))
        pygame.draw.rect(screen, "red", (width * 0.78, height * 0.23, width * 0.15, height * 0.04))
        pygame.draw.rect(screen, "green", (width * 0.78, height * 0.23, width * 0.15 * enemyRatio, height * 0.04))
        font = pygame.font.Font("Fonts/zx_spectrum-7.ttf", 20)
        playerHpImg = font.render('Zycie gracza', True, "black")
        enemyHpImg = font.render('Zycie przeciwnika', True, "black")
        screen.blit(playerHpImg, (width * 0.15, height * 0.23))
        screen.blit(enemyHpImg, (width * 0.785, height * 0.23))
        if attack:
            playerChanceToStrike = random.randint(0, player.agility)
            enemyChanceToDodge = random.randint(0, enemy.agility)
            if playerChanceToStrike > enemyChanceToDodge:
                enemy.getDamage(player.strength)
                #playerCommunication = font.render('Gracz zadał ' + str(player.strength - enemy.armor) + " obrażeń", True, "black")
               # screen.blit(playerCommunication, (width / 2, height * 0.1))
            else:
                playerCommunication = font.render('Gracz chybił', True, "black")
                screen.blit(playerCommunication, (width / 2, height * 0.1))

            playerChanceToDodge = random.randint(0, player.agility)
            enemyChanceToStrike = random.randint(0, enemy.agility)
            if enemyChanceToStrike > playerChanceToDodge:
                player.getDamage(enemy.strength)
            self.i=self.i+1
        if defend:
            player.armor = player.armor + 1
            player.getDamage(enemy.strength)
            player.armor = player.armor - 1
            self.i=self.i+1
        if runAttempt:
            player.player_pos.y = player.player_pos.y + 50
            self.runSuccesful = True
        #if enemy.hp!=enemyStartingHp:

