import pygame

class Interface():
    def showInterface(self,screen,player):
        width=screen.get_width()
        height=screen.get_height()
        font = pygame.font.Font("Fonts/zx_spectrum-7_bold.ttf", 30)
        playerCurrentHpImg = font.render("Zycie: " + str(player.hp) + "/" + str(player.maxhp), True, "black")
        screen.blit(playerCurrentHpImg, (width * 0.03, height * 0.8))
        playerStrength = font.render("Sila: " + str(player.strength), True, "black")
        screen.blit(playerStrength, (width * 0.03, height * 0.9))
        playerCurrentHpImg = font.render("Zwinnosc: " + str(player.agility), True, "black")
        screen.blit(playerCurrentHpImg, (width * 0.25, height * 0.8))
        playerCurrentHpImg = font.render("Pancerz: " + str(player.armor), True, "black")
        screen.blit(playerCurrentHpImg, (width * 0.17, height * 0.9))
        playerCurrentHpImg = font.render("Punkty doswiadczenia: " + str(player.exp), True, "black")
        screen.blit(playerCurrentHpImg, (width * 0.35, height * 0.9))
        playerCurrentHpImg = font.render("Zloto: " + str(player.gold), True, "black")
        screen.blit(playerCurrentHpImg, (width * 0.45, height * 0.8))
