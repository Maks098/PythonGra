import pygame
from Ogre import Ogre
from Player import Player
from BattleView import BattleView
import random
from City import City


def hideAllCreatures(list):
    for j in ogresList:
        j.image = pygame.image.load("Graphics/blank.png").convert_alpha()
    player.image = pygame.image.load("Graphics/blank.png").convert_alpha()


def showAllCreatures(list):
    for j in list:
        j.image = pygame.image.load("Graphics/Ogre.png").convert_alpha()
    player.image = pygame.image.load("Graphics/PlayerTest.png").convert_alpha()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

# data for player position, width and height of screen
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
width = screen.get_width()
height = screen.get_height()

ogrepos = pygame.Vector2(width * 0.3, height * 0.7)
ogrepos1 = pygame.Vector2(width * 0.6, height * 0.5)
ogrepos2 = pygame.Vector2(width * 0.4, height * 0.6)

occupied = False
# background setup
background = pygame.image.load("Graphics/maxresdefault.jpg")
background = pygame.transform.scale(background, (width, height))
pygame.display.flip()
updated = 0
# setup
i = 0
ogreHp = 15
isFighting = False
player = Player(player_pos, occupied)
ogre = Ogre(ogrepos, dt, occupied, ogreHp)
ogre1 = Ogre(ogrepos1, dt, occupied, ogreHp)
ogre2 = Ogre(ogrepos2, dt, occupied, ogreHp)
ogresList = [ogre, ogre1, ogre2]
city = City(screen)
pygame.display.flip()
menu = False
inCity = False

# starting loop
while running:
    runSuccesful = False
    battleView = BattleView(occupied, runSuccesful)
    click = False
    mousePos = pygame.mouse.get_pos()
    attackOrHeal = False
    defendOrUpgrade = False
    runAttemptOrLeave = False
    resume = False
    exitButton = False
    enteringCity = False

    screen.blit(background, (0, 0))
    # looking for events
    for event in pygame.event.get():
        # quitting game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (mousePos[0] >= width * 0.1) & (mousePos[1] >= height * 0.8) & (mousePos[0] <= width * 0.25) & (
                    mousePos[1] <= height * 0.9):
                attackOrHeal = True
            elif (mousePos[0] >= width * 0.4) & (mousePos[1] >= height * 0.8) & (mousePos[0] <= width * 0.55) & (
                    mousePos[1] <= height * 0.9):
                defendOrUpgrade = True
            elif (mousePos[0] >= width * 0.75) & (mousePos[1] >= height * 0.8) & (mousePos[0] <= width * 0.90) & (
                    mousePos[1] <= height * 0.9):
                runAttemptOrLeave = True
            elif (mousePos[0] >= width * 0.44) & (mousePos[1] >= height * 0.47) & (mousePos[0] <= width * 0.56) & (
                    mousePos[1] <= height * 0.53):
                resume = True
            elif (mousePos[0] >= width * 0.40) & (mousePos[1] >= height * 0.56) & (mousePos[0] <= width * 0.58) & (
                    mousePos[1] <= height * 0.62):
                exitButton = True
            elif (mousePos[0] >= width * 0.44) & (mousePos[1] >= height * 0.3) & (mousePos[0] <= width * 0.59) & (
                    mousePos[1] <= height * 0.38):
                enteringCity = True
            else:
                click = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                occupied = not occupied
                menu = not menu

    ogresPos = [None] * len(ogresList)

    for q in range(len(ogresList)):
        ogresPos[q] = ogresList[q].pos

    for ogref in ogresList:
        if occupied == False:
            isMoving = bool(random.getrandbits(1))
            if isMoving == True:
                whichDirection = bool(random.getrandbits(1))
                if whichDirection == True:
                    # vertical
                    posy = random.randint(-1, 1)
                    if posy == -1:
                        ogref.pos.y -= 100 * dt
                    elif posy == 1:
                        ogref.pos.y += 100 * dt
                else:
                    posx = random.randint(-1, 1)
                    if posx == -1:
                        ogref.pos.x += -100 * dt
                    elif posx == 1:
                        ogref.pos.x += 100 * dt
    print(clock.tick())
    screen.blit(city.image, (width * 0.5, height * 0.4))
    screen.blit(player.image, player_pos)
    if not inCity:
        if (player.player_pos.x >= width * 0.49) & (player.player_pos.y >= height * 0.39) & (
                player.player_pos.x <= width * 0.52) & (player.player_pos.y <= height * 0.46):
            screen.blit(pygame.image.load("Graphics/enter.png").convert(), (width * 0.44, height * 0.3))
            if enteringCity:
                inCity = True
    if inCity:
        background = pygame.image.load("Graphics/city.png").convert_alpha()
        city.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        background = pygame.transform.scale(background, (width, height))
        occupied = True
        hideAllCreatures(ogresList)
        screen.blit(pygame.image.load("Graphics/heal.png").convert(), (width * 0.1, height * 0.8))
        screen.blit(pygame.image.load("Graphics/upgrade.png").convert(), (width * 0.4, height * 0.8))
        screen.blit(pygame.image.load("Graphics/leave.png").convert(), (width * 0.75, height * 0.8))
        if attackOrHeal:
            player.hp = player.maxhp
        elif defendOrUpgrade:
            print("Do zaimplementowania")
        elif runAttemptOrLeave:
            occupied = False
            showAllCreatures(ogresList)
            inCity = False
            city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
            background = pygame.image.load("Graphics/maxresdefault.jpg").convert()
            background = pygame.transform.scale(background, (width, height))

    for a in range(len(ogresList)):
        screen.blit(ogresList[a].image, ogresPos[a])
        ogresList[a].updateSOF()

    for ogre in ogresList:
        if (player.player_pos.x >= ogre.influenceSpherex.x) & (player.player_pos.x <= ogre.influenceSpherex.y) \
                & (player.player_pos.y >= ogre.influenceSpherey.x) & (player.player_pos.y <= ogre.influenceSpherey.y):
            background = pygame.image.load("Graphics/BattleView.png").convert()
            background = pygame.transform.scale(background, (width, height))
            hideAllCreatures(ogresList)
            city.image = pygame.image.load("Graphics/blank.png").convert_alpha()
            occupied = True
            battleView.startBattle(screen, player, ogre, attackOrHeal, defendOrUpgrade, runAttemptOrLeave, runSuccesful,
                                   click)
    if player.hp <= 0:
        hideAllCreatures(ogresList)
        background = pygame.image.load("Graphics/śmierć.png").convert()
        background = pygame.transform.scale(background, (width, height))
        occupied = True
    if battleView.runSuccesful:
        showAllCreatures(ogresList)
        city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
        background = pygame.image.load("Graphics/maxresdefault.jpg")
        background = pygame.transform.scale(background, (width, height))
        occupied = False

    for check in ogresList:
        if check.hp <= 0:
            player.exp = player.exp + 3
            occupied = False
            ogresList.sort(key=lambda x: x.hp)
            ogresPos.remove(check.pos)
            ogresList.remove(check)
            showAllCreatures(ogresList)
            city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
            background = pygame.image.load("Graphics/maxresdefault.jpg")
            background = pygame.transform.scale(background, (width, height))
    # if player.exp==3:
    # background = pygame.image.load("Graphics/lvlup.png")
    # background = pygame.transform.scale(background, (width, height))

    keys = pygame.key.get_pressed()
    if occupied == False:
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

    if menu:
        pauseBackground = pygame.Surface((width, height))
        pauseBackground.set_alpha(150)
        pauseBackground.fill((0, 0, 0))

        screen.blit(pauseBackground, (0, 0))
        pause = pygame.image.load("Graphics/pause.png").convert()
        rect = pause.get_rect()
        rect.center = (width / 2, height / 2)
        screen.blit(pause, rect)
        if resume:
            occupied = False
            menu = False
        elif exitButton:
            exit(0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    i = i + 1
pygame.quit()
