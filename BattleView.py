import random
import time
import pygame


class BattleView:
    def __init__(self, flag, runSuccesful):
        self.flag = flag
        self.runSuccesful = runSuccesful
        self.i=0


    def print_message(self,screen, font, communicate, comm_center):
        display_duration = 1
        message = font.render(communicate, True, 'black')
        comm_rect = message.get_rect()
        comm_rect_center = (comm_center)

        start_time = time.time()
        elapsed_time = time.time() - start_time

        while elapsed_time < display_duration:
            screen.blit(message, comm_rect_center)
            pygame.display.flip()
            elapsed_time = time.time() - start_time

    def startBattle(self, screen, player, enemy, attack, defend, runAttempt, runSuccesful):

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

                player_comm = "Gracz zadal " + str(player.strength - enemy.armor) + " pkt. obrazen"
                comm_rect_center = (width / 2 * 0.85, height * 0.2)

                self.print_message(screen, font, player_comm, comm_rect_center)
                self.i=self.i+1

            else:
                player_comm_miss = "Gracz chybil"
                comm_rect_center_miss = (width / 2 * 0.85, height * 0.2)

                self.print_message(screen, font, player_comm_miss, comm_rect_center_miss)
                self.i=self.i+1

            playerChanceToDodge = random.randint(0, player.agility)
            enemyChanceToStrike = random.randint(0, enemy.agility)

            if enemyChanceToStrike > playerChanceToDodge:
                player.getDamage(enemy.strength)

                enemy_comm = "Ogr atakuje"
                e_comm_rect_center = (width / 2 * 0.85, height * 0.25)

                self.print_message(screen, font, enemy_comm, e_comm_rect_center)
                self.i=self.i+1
            else:
                enemy_comm = "Ogr nie trafia atakiem"
                e_comm_rect_center = (width / 2 * 0.85, height * 0.25)

                self.print_message(screen, font, enemy_comm, e_comm_rect_center)
                self.i = self.i + 1

        if defend:
            player.armor = player.armor + 1
            player.getDamage(enemy.strength)
            player.armor = player.armor - 1

            comm = "Gracz uzywa obrony"
            comm_rect_center = (width / 2 * 0.85, height * 0.2)

            self.print_message(screen, font, comm, comm_rect_center)
            self.i=self.i+1

        if runAttempt:

            player.player_pos.y = player.player_pos.y + 50
            self.runSuccesful = True
