import pygame


class BattleView:
    def __init__(self, screen, player, enemy, flag):
        self.enemy = enemy
        self.player = player
        self.startBattle(screen, player, enemy, flag)

    def startBattle(self, screen, player, enemy, flag):
        i = 1
        while (player.hp <= 0) | (enemy.hp <= 0):
            flag = False

        # screen.blit(pygame.image.load("Graphics/Atakuj.png").convert(), (500, 400))

        #Insert Player character to BattleView
        player_pic = pygame.image.load("Graphics/PlayerTest.png").convert_alpha()
        width = player_pic.get_rect().width
        height = player_pic.get_rect().height
        player = pygame.transform.scale(player_pic, (width * 12, height * 12))
        screen.blit(player, (400, 500))

        if ((pygame.mouse.get_pressed()[0] == i) & (pygame.mouse.get_pos() < (600, 500)) & (
                pygame.mouse.get_pos() > (400, 300))):
            # enemy.hp=self.dealDamage(enemy,3)
            # i = i + 1
            enemy.getDamage(3)

    def dealDamage(self, enemy, damage):
        return enemy.hp - damage
