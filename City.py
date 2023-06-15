import pygame

import Interface


class City():
    def __init__(self, screen):
        self.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()

    def enterCity(self, screen, leave, player, background):
        heal=False
        upgrade=False
        leaveFromCityPerspective=False
        print(leave)
        width = screen.get_width()
        height = screen.get_height()

        healImg = pygame.image.load("Graphics/heal.png").convert()
        healRect = healImg.get_rect()
        healRect.center = (width * 0.2, height * 0.85)

        upgradeImg = pygame.image.load("Graphics/upgrade.png").convert()
        upgradeRect = upgradeImg.get_rect()
        upgradeRect.center = (width * 0.5, height * 0.85)

        leaveImg = pygame.image.load("Graphics/leave.png").convert()
        leaveRect = leaveImg.get_rect()
        leaveRect.center = (width * 0.85, height * 0.85)

        screen.blit(healImg,healRect)
        screen.blit(upgradeImg,upgradeRect)
        screen.blit(leaveImg,leaveRect)

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if healRect.collidepoint(event.pos):
                    heal=True
                if upgradeRect.collidepoint(event.pos):
                    upgrade=True
                if leaveRect.collidepoint(event.pos):
                    leaveFromCityPerspective=True


        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.45, height * 0.55))
        font = pygame.font.Font("Fonts/zx_spectrum-7_bold.ttf", 30)
        player_current_hp = font.render("Zycie: " + str(player.hp) + "/" + str(player.maxhp), True, "black")
        screen.blit(player_current_hp, (width * 0.1, height * 0.75))
        player_current_armour = font.render("Pancerz: " + str(player.armor), True, "black")
        screen.blit(player_current_armour, (width * 0.4, height * 0.75))
        player_current_gold = font.render("Zloto: " + str(player.gold), True, "black")
        screen.blit(player_current_gold, (width * 0.75, height * 0.75))
        background = pygame.image.load("Graphics/city.png").convert_alpha()
        self.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        background = pygame.transform.scale(background, (width, height))
        occupied = True
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
        elif leaveFromCityPerspective:
            return True
