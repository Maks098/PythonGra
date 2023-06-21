import pygame


class City():
    def __init__(self, screen):
        self.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()

    def enterCity(self, screen, heal, upgrade, leave, player, background):
        width = screen.get_width()
        height = screen.get_height()
        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.45, height * 0.55))
        font = pygame.font.Font("Fonts/zx_spectrum-7_bold.ttf", 30)
        playerCurrentHp = font.render("[1] Zycie: " + str(player.hp) + "/" + str(player.maxhp), True, "black")
        screen.blit(playerCurrentHp, (width * 0.1, height * 0.75))
        playerCurrentArmour = font.render("[1] Pancerz: " + str(player.armor), True, "black")
        screen.blit(playerCurrentArmour, (width * 0.4, height * 0.75))
        playerCurrentGold = font.render("Zloto: " + str(player.gold), True, "black")
        screen.blit(playerCurrentGold, (width * 0.75, height * 0.75))
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

            elif player.hp < player.maxhp:
                player.hp += 1
                player.gold -= 1

        elif upgrade:
            if player.gold <= 0:
                player.gold = 0

            else:
                player.armor += 1
                player.gold -= 1
