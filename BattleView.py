import pygame


class BattleView:
    def __init__(self, screen, enemy, player, flag):
        self.enemy = enemy
        self.player = player
        self.startBattle(screen, player, enemy, flag)

    def startBattle(self, screen, playerhp, enemyhp, flag):
        if (playerhp <= 0) | (enemyhp <= 0):
            flag = False

        screen.blit(pygame.image.load("Graphics/Atakuj.png").convert(), (500, 400))
        click = pygame.mouse.get_pressed()
        if ((pygame.mouse.get_pressed()[0]==1)&(pygame.mouse.get_pos() < (600, 500)) & (
                pygame.mouse.get_pos() > (400, 300))):
            exit(0)
