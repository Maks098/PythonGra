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

ogrepos = pygame.Vector2(700, 500)
ogrepos1 = pygame.Vector2(1000, 500)
ogrepos2 = pygame.Vector2(500, 300)

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
attack=False
ogresList = [ogre, ogre1, ogre2]
pygame.display.flip()
# starting loop
while running:
    battleView = BattleView(screen, player, flag)
    attack = False
    flag = battleView.flag
    screen.blit(background, (0, 0))
    # looking for events
    for event in pygame.event.get():
        # quitting game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos() < (600, 500)) & (
                    pygame.mouse.get_pos() > (400, 300)):
                attack = True
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
            battleView.startBattle(screen, battleView.player, aoi, attack)

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
