import pygame


#todo poprawić napisy w blacksmithie

class Blacksmith():
    def __init__(self, screen):
        self.image = pygame.image.load("Graphics/blacksmith_logo.png").convert_alpha()

    def enter_blacksmith(self,screen, upgrade, leave, player, background):
        width = screen.get_width()
        height = screen.get_height()

        screen.blit(pygame.image.load("Graphics/PlayerInFight.png").convert_alpha(), (width * 0.2, height * 0.55))
        font = pygame.font.Font("Fonts/zx_spectrum-7_bold.ttf", 30)

        player_current_strength = font.render("[3] Sila: " + str(player.strength), True, "black")
        screen.blit(player_current_strength, (width * 0.4, height * 0.75))

        player_current_gold = font.render("Zloto: " + str(player.gold), True, "black")
        screen.blit(player_current_gold, (width * 0.75, height * 0.75))

        background = pygame.image.load("Graphics/blacksmith.png").convert_alpha()
        self.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        background = pygame.transform.scale(background, (width, height))
        occupied = True

        screen.blit(pygame.image.load("Graphics/upgrade.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/leave.png").convert(), (width * 0.75, height * 0.8))

        if upgrade:
            if player.gold <= 0:
                player.gold = 0
                print("not")
            elif player.gold < 3:
                print("not enough")
            else:
                player.strength += 1
                player.gold -= 3
