import pygame

import Interface


class City():
    def __init__(self, screen):
        self.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()

    def enterCity(self, screen, heal, upgrade, leave, player, background):
        width = screen.get_width()
        height = screen.get_height()
        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.45, height * 0.55))
        font = pygame.font.Font("Fonts/zx_spectrum-7_bold.ttf", 30)
        player_current_hp = font.render("[1] Zycie: " + str(player.hp) + "/" + str(player.maxhp), True, "black")
        screen.blit(player_current_hp, (width * 0.1, height * 0.75))
        player_current_armour = font.render("[1] Pancerz: " + str(player.armor), True, "black")
        screen.blit(player_current_armour, (width * 0.4, height * 0.75))
        player_current_gold = font.render("Zloto: " + str(player.gold), True, "black")
        screen.blit(player_current_gold, (width * 0.75, height * 0.75))
        background = pygame.image.load("Graphics/city.png").convert_alpha()
        self.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        background = pygame.transform.scale(background, (width, height))
        occupied = True
        screen.blit(pygame.image.load("Graphics/heal.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/upgrade.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/leave.png").convert(), (width * 0.75, height * 0.8))
        if heal:
            if player.gold <= 0:
                player.gold = 0
                print("do zaimplementoowania")
            elif player.hp < player.maxhp:
                player.hp += 1
                player.gold -= 1

        elif upgrade:
            if player.gold <= 0:
                player.gold = 0
                print("do zaimplementoowania")
            else:
                player.armor += 1
                player.gold -= 1
