import random
import time
import pygame


class BattleView:
    def __init__(self, flag, runSuccesful, ):
        self.flag = flag
        self.runSuccesful = runSuccesful
        self.i = 0

    def printMessage(self, screen, font, communicate, commCenter):
        displayDuration = 0.5
        message = font.render(communicate, True, 'black')
        commRect = message.get_rect()
        commRectCenter = (commCenter)

        startTime = time.time()
        elapsedTime = time.time() - startTime

        while elapsedTime < displayDuration:
            screen.blit(message, commRectCenter)
            pygame.display.flip()
            elapsedTime = time.time() - startTime

    def startBattle(self, screen, player, enemy, enemyImg, attack, defend, runAttempt, runSuccesful):

        playerRatio = player.hp / player.maxhp
        enemyRatio = enemy.hp / enemy.maxhp
        width = screen.get_width()
        height = screen.get_height()

        enemyImage = pygame.image.load(enemyImg)
        enemyWidth = enemyImage.get_width()
        enemyHeight = enemyImage.get_height()
        enemyImgScaled = pygame.transform.scale(enemyImage, (enemyWidth * 10, enemyHeight * 10))

        screen.blit(pygame.image.load("Graphics/attack.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/defend.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/runAttempt.png").convert(), (width * 0.75, height * 0.8))
        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.15, height * 0.5))
        screen.blit(enemyImgScaled, (width * 0.7, height * 0.4))

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

                playerComm = "Gracz zadal " + str(player.strength - enemy.armor) + " pkt. obrazen"
                commRectCenter = (width / 2 * 0.85, height * 0.2)

                self.printMessage(screen, font, playerComm, commRectCenter)

            else:
                playerCommMiss = "Gracz chybil"
                commRectCenterMiss = (width / 2 * 0.85, height * 0.2)

                self.printMessage(screen, font, playerCommMiss, commRectCenterMiss)

            playerChanceToDodge = random.randint(0, player.agility)
            enemyChanceToStrike = random.randint(0, enemy.agility)

            if enemyChanceToStrike > playerChanceToDodge:
                player.getDamage(enemy.strength - player.armor)

                enemyComm = "Przeciwnik atakuje"
                eCommRectCenter = (width / 2 * 0.85, height * 0.25)

                self.printMessage(screen, font, enemyComm, eCommRectCenter)
                self.i = self.i + 1
            else:
                enemyComm = "Przeciwnik nie trafia atakiem"
                eCommRectCenter = (width / 2 * 0.85, height * 0.25)

                self.printMessage(screen, font, enemyComm, eCommRectCenter)
                self.i = self.i + 1

        if defend:
            player.getDamage(enemy.strength - 1)
            comm = "Gracz uzywa obrony"
            commRectCenter = (width / 2 * 0.85, height * 0.2)

            self.printMessage(screen, font, comm, commRectCenter)
            self.i = self.i + 1

        if runAttempt:
            player.player_pos.y = player.player_pos.y + 50
            self.runSuccesful = True
