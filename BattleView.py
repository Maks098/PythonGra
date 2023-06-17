import random

import pygame


class BattleView:
    def __init__(self, flag, runSuccesful, tic):
        self.flag = flag
        self.runSuccesful = runSuccesful
        self.i = 0

    def startBattle(self, screen, player, enemy, runSuccesful):
        attack = False
        defend = False
        runAttempt = False

        playerRatio = player.hp / player.maxhp
        enemyRatio = enemy.hp / enemy.maxhp
        width = screen.get_width()
        height = screen.get_height()

        attackImg = pygame.image.load("Graphics/attack.png").convert()
        attackRect = attackImg.get_rect()
        attackRect.center = (width * 0.2, height * 0.85)

        defendImg = pygame.image.load("Graphics/defend.png").convert()
        defendRect = defendImg.get_rect()
        defendRect.center = (width * 0.5, height * 0.85)

        runAttemptImg = pygame.image.load("Graphics/runAttempt.png").convert()
        runAttemptRect = runAttemptImg.get_rect()
        runAttemptRect.center = (width * 0.85, height * 0.85)

        screen.blit(attackImg, attackRect)
        screen.blit(defendImg, defendRect)
        screen.blit(runAttemptImg, runAttemptRect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if attackRect.collidepoint(event.pos):
                    attack = True
                if defendRect.collidepoint(event.pos):
                    defend = True
                if runAttemptRect.collidepoint(event.pos):
                    runAttempt = True

        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.15, height * 0.5))
        screen.blit(pygame.image.load("Graphics/OgreInFight.png").convert_alpha(), (width * 0.7, height * 0.4))
        pygame.draw.rect(screen, "red", (width * 0.13, height * 0.23, width * 0.15, height * 0.04))
        pygame.draw.rect(screen, "green", (width * 0.13, height * 0.23, width * 0.15 * playerRatio, height * 0.04))
        pygame.draw.rect(screen, "red", (width * 0.78, height * 0.23, width * 0.15, height * 0.04))
        pygame.draw.rect(screen, "green", (width * 0.78, height * 0.23, width * 0.15 * enemyRatio, height * 0.04))
        font = pygame.font.Font("Fonts/zx_spectrum-7.ttf", int(height * 0.02))
        playerHpImg = font.render('Zycie gracza', True, "black")
        enemyHpImg = font.render('Zycie przeciwnika', True, "black")
        screen.blit(playerHpImg, (width * 0.15, height * 0.23))
        screen.blit(enemyHpImg, (width * 0.785, height * 0.23))
        if attack:
            tic = pygame.time.get_ticks()
            playerChanceToStrike = random.randint(0, player.agility)
            enemyChanceToDodge = random.randint(0, enemy.agility)
            if playerChanceToStrike > enemyChanceToDodge:
                enemy.getDamage(player.strength)
                playerCommunication = font.render('Gracz zadał ' + str(player.strength - enemy.armor) + " obrażeń",
                                                  True, "black")
                screen.blit(playerCommunication, (width / 2, height * 0.1))

            else:
                playerCommunication = font.render('Gracz chybil', True, "black")
                screen.blit(playerCommunication, (width / 2, height * 0.1))

            playerChanceToDodge = random.randint(0, player.agility)
            enemyChanceToStrike = random.randint(0, enemy.agility)
            if enemyChanceToStrike > playerChanceToDodge:
                player.getDamage(enemy.strength)
            self.i = self.i + 1
        if defend:
            player.armor = player.armor + 1
            player.getDamage(enemy.strength)
            player.armor = player.armor - 1
            self.i = self.i + 1
        if runAttempt:
            player.player_pos.y = player.player_pos.y + 50
            self.runSuccesful = True

