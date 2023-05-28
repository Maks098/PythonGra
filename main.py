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

ogrepos = pygame.Vector2(width*0.3,height*0.7)
ogrepos1 = pygame.Vector2(width*0.6, height*0.5)
ogrepos2 = pygame.Vector2(width*0.4,height*0.6)

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
attack = False
defend = False
ogresList = [ogre, ogre1, ogre2]
pygame.display.flip()

# starting loop
while running:
    mousePos = pygame.mouse.get_pos()
    battleView = BattleView(flag)
    attack = False
    defend = False
    runAttempt=False
    flag = battleView.flag
    screen.blit(background, (0, 0))
    # looking for events
    pygame.draw.rect(screen,"red",(width*0.7,height*0.8,20,20))
    pygame.draw.rect(screen, "red", (width * 0.9, height * 0.8, 20, 20))
    for event in pygame.event.get():
        # quitting game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (mousePos[0] > width * 0.1) & (mousePos[1] > height * 0.8) & (mousePos[0] < width * 0.2) & (mousePos[1] < height * 0.85):
                attack = True
            elif (mousePos[0] > width * 0.4) & (mousePos[1] > height * 0.8) & (mousePos[0] < width * 0.5) & (mousePos[1] < height * 0.85):
                defend = True
            elif (mousePos[0] > width * 0.7) & (mousePos[1] > height * 0.8) & (mousePos[0] < width * 0.9) & (mousePos[1] < height * 0.85):
                runAttempt = True

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

    for aoi in ogresList:
        if (player.player_pos.x >= aoi.influenceSpherex.x) & (player.player_pos.x <= aoi.influenceSpherex.y) \
                & (player.player_pos.y >= aoi.influenceSpherey.x) & (player.player_pos.y <= aoi.influenceSpherey.y):
            background = pygame.image.load("Graphics/BattleView.png").convert()
            background = pygame.transform.scale(background, (width, height))
            hideAllCreatures(ogresList)
            flag = True
            battleView.startBattle(screen, player, aoi, attack)

    if player.hp <= 0:
        hideAllCreatures(ogresList)
        background = pygame.image.load("Graphics/śmierć.png").convert()
        background = pygame.transform.scale(background, (width, height))
        flag = True

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

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    i = i + 1
pygame.quit()
# def showAllCreatures(list):
