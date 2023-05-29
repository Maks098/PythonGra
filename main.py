import pygame
from Ogre import Ogre
from Player import Player
from BattleView import BattleView
import random
import threading


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

# data for player posioton, width and height
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
width = screen.get_width()
height = screen.get_height()

ogrepos = pygame.Vector2(width * 0.3, height * 0.7)
ogrepos1 = pygame.Vector2(width * 0.6, height * 0.5)
ogrepos2 = pygame.Vector2(width * 0.4, height * 0.6)

flag = False
# background setup
background = pygame.image.load("Graphics/maxresdefault.jpg")
background = pygame.transform.scale(background, (width, height))
pygame.display.flip()
updated = 0
# setup
i = 0
ogreHp = 15
isFighting = False
player = Player(player_pos, flag)
ogre = Ogre(ogrepos, dt, flag, ogreHp)
ogre1 = Ogre(ogrepos1, dt, flag, ogreHp)
ogre2 = Ogre(ogrepos2, dt, flag, ogreHp)
ogresList = [ogre, ogre1, ogre2]
pygame.display.flip()
menu = False
# starting loop
while running:
    click = False
    mousePos = pygame.mouse.get_pos()
    runSuccesful = False
    battleView = BattleView(flag, runSuccesful)
    attack = False
    defend = False
    runAttempt = False
    resume = False
    exitButton = False

    flag = battleView.flag
    screen.blit(background, (0, 0))
    # looking for events
    for event in pygame.event.get():
        # quitting game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (mousePos[0] > width * 0.1) & (mousePos[1] > height * 0.8) & (mousePos[0] < width * 0.25) & (
                    mousePos[1] < height * 0.9):
                attack = True
            elif (mousePos[0] > width * 0.4) & (mousePos[1] > height * 0.8) & (mousePos[0] < width * 0.55) & (
                    mousePos[1] < height * 0.9):
                defend = True
            elif (mousePos[0] > width * 0.75) & (mousePos[1] > height * 0.8) & (mousePos[0] < width * 0.90) & (
                    mousePos[1] < height * 0.9):
                runAttempt = True
            elif (mousePos[0] > width * 0.41) & (mousePos[1] > height * 0.48) & (mousePos[0] < width * 0.54) & (
                    mousePos[1] < height * 0.53):
                resume = True
            elif (mousePos[0] > width * 0.40) & (mousePos[1] > height * 0.56) & (mousePos[0] < width * 0.56) & (
                    mousePos[1] < height * 0.62):
                exitButton = True
            else:
                click = True

    ogresPos = [None] * len(ogresList)

    for q in range(len(ogresList)):
        ogresPos[q] = ogresList[q].pos

    for ogref in ogresList:
        if flag == False:
            isMoving = bool(random.getrandbits(1))
            if isMoving == True:
                posy = random.randint(-1, 1)
                posx = random.randint(-1, 1)
                if posy == -1:
                    ogref.pos.y -= 100 * dt
                elif posy == 1:
                    ogref.pos.y += 100 * dt
                if posx == -1:
                    ogref.pos.x += -100 * dt
                elif posx == 1:
                    ogref.pos.x += 100 * dt

    screen.blit(player.image, player_pos)
    for a in range(len(ogresList)):
        screen.blit(ogresList[a].image, ogresPos[a])
        ogresList[a].updateSOF()

    for ogre in ogresList:
        if (player.player_pos.x >= ogre.influenceSpherex.x) & (player.player_pos.x <= ogre.influenceSpherex.y) \
                & (player.player_pos.y >= ogre.influenceSpherey.x) & (player.player_pos.y <= ogre.influenceSpherey.y):
            background = pygame.image.load("Graphics/BattleView.png").convert()
            background = pygame.transform.scale(background, (width, height))
            hideAllCreatures(ogresList)
            flag = True
            battleView.startBattle(screen, player, ogre, attack, defend, runAttempt, runSuccesful, click)

    if player.hp <= 0:
        hideAllCreatures(ogresList)
        background = pygame.image.load("Graphics/śmierć.png").convert()
        background = pygame.transform.scale(background, (width, height))
        flag = True
    if battleView.runSuccesful:
        showAllCreatures(ogresList)
        background = pygame.image.load("Graphics/maxresdefault.jpg")
        background = pygame.transform.scale(background, (width, height))
        flag = False

    for check in ogresList:
        if check.hp <= 0:
            player.exp = player.exp + 3
            flag = False
            ogresList.sort(key=lambda x: x.hp)
            ogresPos.remove(check.pos)
            ogresList.remove(check)
            showAllCreatures(ogresList)
            background = pygame.image.load("Graphics/maxresdefault.jpg")
            background = pygame.transform.scale(background, (width, height))
    # if player.exp==3:
    # background = pygame.image.load("Graphics/lvlup.png")
    # background = pygame.transform.scale(background, (width, height))

    if flag == True:
        for ogref in ogresList:
            if flag == False:
                isMoving = bool(random.getrandbits(1))
                if isMoving == True:
                    posy = random.randint(-1, 1)
                    posx = random.randint(-1, 1)
                    if posy == -1:
                        ogref.pos.y -= 100 * dt
                    elif posy == 1:
                        ogref.pos.y += 100 * dt
                    if posx == -1:
                        ogref.pos.x += -100 * dt
                    elif posx == 1:
                        ogref.pos.x += 100 * dt

    keys = pygame.key.get_pressed()
    if flag == False:
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        if keys[pygame.K_ESCAPE]:
            flag = True
            menu = True
    if menu:
        pauseBackground = pygame.Surface((width, height))
        pauseBackground.set_alpha(150)
        pauseBackground.fill((0, 0, 0))
        screen.blit(pauseBackground, (0, 0))
        pause = pygame.image.load("Graphics/pause.png").convert()
        screen.blit(pause, (width * 0.33, height * 0.32))
        if resume:
            flag = False
            pause.fill((0, 0, 0, 0))
            pauseBackground.set_alpha(255)
            screen.blit(pauseBackground, (0, 0))
            menu = False
        elif exitButton:
            exit(0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    i = i + 1
pygame.quit()
# def showAllCreatures(list):
