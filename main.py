import pygame

from Blacksmith import Blacksmith
from Interface import Interface
from Menu import Menu
from Ogre import Ogre
from Skeleton import Skeleton
from Player import Player
from BattleView import BattleView
import random
from City import City
from Movement import Movement

def hideAllCreatures(list):
    for j in list:
        j.image = pygame.image.load("Graphics/blank.png").convert_alpha()
    player.image = pygame.image.load("Graphics/blank.png").convert_alpha()


def showAllCreaturesOgre(list,list2):
    for j in list:
        j.image = pygame.image.load("Graphics/Ogre.png").convert_alpha()

    for k in list2:
        k.image = pygame.image.load("Graphics/skeleton.png").convert_alpha()

    player.image = pygame.image.load("Graphics/PlayerTest.png").convert_alpha()

# def showAllCreaturesSkeleton(list):
#         for j in list:
#             j.image = pygame.image.load("Graphics/skeleton.png").convert_alpha()
#         player.image = pygame.image.load("Graphics/PlayerTest.png").convert_alpha()
def turnOnForSomeDt(forHowLong):
    start=pygame.time.get_ticks()
    if start+forHowLong>pygame.time.get_ticks():
        pygame.draw.rect(screen,"black",(300,300,30,30))

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

ogrepos = pygame.Vector2(width * 0.3, height * 0.65)
ogrepos1 = pygame.Vector2(width * 0.6, height * 0.65)
ogrepos2 = pygame.Vector2(width * 0.2, height * 0.2)
ogrepos3 = pygame.Vector2(width * 0.8, height * 0.5)
ogrepos4 = pygame.Vector2(width * 0.7, height * 0.1)

skeletonpos = pygame.Vector2(width * 0.1, height * 0.6)
skeletonpos2 = pygame.Vector2(width * 0.2, height * 0.4)
skeletonpos3 = pygame.Vector2(width * 0.9, height * 0.4)

occupied = False
# background setup
background = pygame.image.load("Graphics/PytongProjekt.jpg")
background = pygame.transform.scale(background, (width, height))
pygame.display.flip()
updated = 0
# setup
i = 0
ogreHp = 15
skeletonHp = 10
isFighting = False
player = Player(player_pos, occupied)

ogreIMG = "Graphics/Ogre.png"
skelIMG = "Graphics/skeleton.png"

ogre = Ogre(ogrepos, dt, occupied, ogreHp)
ogre1 = Ogre(ogrepos1, dt, occupied, ogreHp)
ogre2 = Ogre(ogrepos2, dt, occupied, ogreHp)
ogre3 = Ogre(ogrepos3, dt, occupied, ogreHp)
ogre4 = Ogre(ogrepos4, dt, occupied, ogreHp)

ogresList = [ogre, ogre1, ogre2, ogre3, ogre4]

skeleton = Skeleton(skeletonpos, dt, occupied, skeletonHp)
skeleton2 = Skeleton(skeletonpos2, dt, occupied, skeletonHp)
skeleton3 = Skeleton(skeletonpos3, dt, occupied, skeletonHp)

skeletonList = [skeleton, skeleton2, skeleton3]

city = City(screen)
blacksmith = Blacksmith(screen)
pygame.display.flip()
menu = False
inCity = False
inBlacksmith = False
inLevelUp=False
isDead = False
movement=Movement()
menuClass=Menu()
# starting loop
while running:

    interface=Interface()
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
    enteringBlacksmith = False

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
            elif (mousePos[0] >= width * 0.42) & (mousePos[1] >= height * 0.56) & (mousePos[0] <= width * 0.58) & (
                    mousePos[1] <= height * 0.62):
                exitButton = True
            elif (mousePos[0] >= width * 0.40) & (mousePos[1] >= height * 0.25) & (mousePos[0] <= width * 0.56) & (
                    mousePos[1] <= height * 0.34):
                enteringCity = True
            elif (mousePos[0] >= width * 0.72) & (mousePos[1] >= height * 0.3) & (mousePos[0] <= width * 0.88) & (
                    mousePos[1] <= height * 0.4):
                enteringBlacksmith = True
            else:
                click = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                occupied = not occupied
                menu=not menu

       # pygame.draw.rect(screen,"black",(300,300,20,20))

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
                        ogref.pos.y -= 200 * dt
                    elif posy == 1:
                        ogref.pos.y += 200 * dt
                else:
                    posx = random.randint(-1, 1)
                    if posx == -1:
                        ogref.pos.x += -200 * dt
                    elif posx == 1:
                        ogref.pos.x += 200 * dt

                movement.ogre_movement(ogref.pos, width, height)


    skeletonPos = [None] * len(skeletonList)

    for a in range(len(skeletonList)):
        skeletonPos[a] = skeletonList[a].pos

    for skelm in skeletonList:
        if occupied == False:
            isMoving = bool(random.getrandbits(1))
            if isMoving == True:
                whichDirection = bool(random.getrandbits(1))
                if whichDirection == True:
                    # vertical
                    posy = random.randint(-1, 1)
                    if posy == -1:
                        skelm.pos.y -= 200 * dt
                    elif posy == 1:
                        skelm.pos.y += 200 * dt
                else:
                    posx = random.randint(-1, 1)
                    if posx == -1:
                        skelm.pos.x += -200 * dt
                    elif posx == 1:
                        skelm.pos.x += 200 * dt

                movement.skel_movement(skelm.pos, width, height)

    #if player.exp==3:
        # inLevelUp=True
        # background = pygame.image.load("Graphics/lvlup.png")
        # background = pygame.transform.scale(background, (width, height))
        # occupied=True
        # hideAllCreatures(ogresList)
        # city.image = pygame.image.load("Graphics/blank.png").convert_alpha()


    if ((not inCity) and (not inLevelUp) and (not inBlacksmith) and (not isDead)):
        interface.showInterface(screen,player)

    cityOnMapRect=city.image.get_rect()
    cityOnMapRect.center = (width * 0.48, height *0.18)
    screen.blit(city.image,cityOnMapRect)
    screen.blit(player.image, player_pos)

    if not inCity:
        if (player.player_pos.x >= width * 0.45) & (player.player_pos.y >= height * 0.16) & (
                player.player_pos.x <= width * 0.49) & (player.player_pos.y <= height * 0.21):
            enter = pygame.image.load("Graphics/enter.png").convert()
            enterRect = enter.get_rect()
            enterRect.center = (width * 0.48, height *0.3)
            screen.blit(enter,enterRect)
            if enteringCity:
                inCity = True
    if inCity:
        hideAllCreatures(ogresList)
        hideAllCreatures(skeletonList)
        blacksmith.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        city.enterCity(screen,attackOrHeal,defendOrUpgrade,runAttemptOrLeave,player,background)
        occupied=True
        background = pygame.image.load("Graphics/city.png").convert()
        background = pygame.transform.scale(background, (width, height))
        if runAttemptOrLeave:
            showAllCreaturesOgre(ogresList,skeletonList)
            occupied = False
            blacksmith.image = pygame.image.load("Graphics/blacksmith_logo.png").convert_alpha()
            city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
            background = pygame.image.load("Graphics/PytongProjekt.jpg").convert()
            background = pygame.transform.scale(background, (width, height))
            inCity = False

    blacksmithOnMapRect = blacksmith.image.get_rect()
    blacksmithOnMapRect.center = (width * 0.8, height * 0.25)
    screen.blit(blacksmith.image, blacksmithOnMapRect)
    screen.blit(player.image, player_pos)

    if not inBlacksmith:
        if (player.player_pos.x >= width * 0.77) & (player.player_pos.y >= height * 0.20) & (
                player.player_pos.x <= width * 0.81) & (player.player_pos.y <= height * 0.28):
            enter = pygame.image.load("Graphics/enter.png").convert()
            enterRect = enter.get_rect()
            enterRect.center = (width * 0.8, height *0.35)
            screen.blit(enter,enterRect)
            if enteringBlacksmith:
                inBlacksmith = True
    if inBlacksmith:
        hideAllCreatures(ogresList)
        hideAllCreatures(skeletonList)
        city.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        blacksmith.enter_blacksmith(screen, defendOrUpgrade, runAttemptOrLeave, player, background)
        occupied = True
        background = pygame.image.load("Graphics/blacksmith.png").convert()
        background = pygame.transform.scale(background, (width, height))

        if runAttemptOrLeave:
            showAllCreaturesOgre(ogresList, skeletonList)

            occupied = False
            city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
            blacksmith.image = pygame.image.load("Graphics/blacksmith_logo.png").convert_alpha()
            background = pygame.image.load("Graphics/PytongProjekt.jpg").convert()
            background = pygame.transform.scale(background, (width, height))
            inBlacksmith = False

    for a in range(len(ogresList)):
        screen.blit(ogresList[a].image, ogresPos[a])
        ogresList[a].updateSOF()

    for ogre in ogresList:
        if (player.player_pos.x >= ogre.influenceSpherex.x) & (player.player_pos.x <= ogre.influenceSpherex.y) \
                & (player.player_pos.y >= ogre.influenceSpherey.x) & (player.player_pos.y <= ogre.influenceSpherey.y):
            background = pygame.image.load("Graphics/BattleView.png").convert()
            background = pygame.transform.scale(background, (width, height))
            hideAllCreatures(ogresList)
            hideAllCreatures(skeletonList)
            city.image = pygame.image.load("Graphics/blank.png").convert_alpha()
            blacksmith.image = pygame.image.load("Graphics/blank.png").convert_alpha()
            occupied = True
            battleView.startBattle(screen, player, ogre, ogreIMG, attackOrHeal, defendOrUpgrade, runAttemptOrLeave, runSuccesful)

    for b in range(len(skeletonList)):
        screen.blit(skeletonList[b].image, skeletonPos[b])
        skeletonList[b].updateSOF()

    for skel in skeletonList:
        if (player.player_pos.x >= skel.influenceSpherex.x) & (player.player_pos.x <= skel.influenceSpherex.y) \
                & (player.player_pos.y >= skel.influenceSpherey.x) & (player.player_pos.y <= skel.influenceSpherey.y):
            background = pygame.image.load("Graphics/BattleView.png").convert()
            background = pygame.transform.scale(background, (width, height))
            hideAllCreatures(skeletonList)
            hideAllCreatures(ogresList)
            city.image = pygame.image.load("Graphics/blank.png").convert_alpha()
            blacksmith.image = pygame.image.load("Graphics/blank.png").convert_alpha()
            occupied = True
            battleView.startBattle(screen, player, skel, skelIMG, attackOrHeal, defendOrUpgrade, runAttemptOrLeave, runSuccesful)


    if battleView.runSuccesful:
        showAllCreaturesOgre(ogresList, skeletonList)

        blacksmith.image = pygame.image.load("Graphics/blacksmith_logo.png").convert_alpha()
        city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
        background = pygame.image.load("Graphics/PytongProjekt.jpg")
        background = pygame.transform.scale(background, (width, height))
        occupied = False

    for check in ogresList:
        if check.hp <= 0:
            player.exp = player.exp + 3
            occupied = False
            ogresList.sort(key=lambda x: x.hp)
            ogresPos.remove(check.pos)
            ogresList.remove(check)
            showAllCreaturesOgre(ogresList,skeletonList)
            blacksmith.image = pygame.image.load("Graphics/blacksmith_logo.png").convert_alpha()
            city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
            background = pygame.image.load("Graphics/PytongProjekt.jpg")
            background = pygame.transform.scale(background, (width, height))
            player.gold=player.gold+random.randint(2,6)

    for check in skeletonList:
        if check.hp <= 0:
            player.exp = player.exp + 3
            occupied = False
            skeletonList.sort(key=lambda x: x.hp)
            skeletonPos.remove(check.pos)
            skeletonList.remove(check)
            showAllCreaturesOgre(ogresList,skeletonList)
            blacksmith.image = pygame.image.load("Graphics/blacksmith_logo.png").convert_alpha()
            city.image = pygame.image.load("Graphics/cityImage.png").convert_alpha()
            background = pygame.image.load("Graphics/PytongProjekt.jpg")
            background = pygame.transform.scale(background, (width, height))
            player.gold=player.gold+random.randint(2,6)

    movement.startMovement(occupied,player_pos,dt,width,height)

    if menu:
        pauseBackground = pygame.Surface((width, height))
        pauseBackground.set_alpha(150)
        pauseBackground.fill((0, 0, 0))
        screen.blit(pauseBackground, (0, 0))

        pause = pygame.image.load("Graphics/pause.png").convert()
        pauseRect = pause.get_rect()
        pauseRect.center = (width / 2, height / 2)

        resumeImg = pygame.image.load("Graphics/resume.png").convert()
        resumeImg_rect = resumeImg.get_rect()
        resumeImg_rect.center = (width / 2, height / 2)

        exitImg = pygame.image.load("Graphics/exit.png").convert()
        exitImg_rect = exitImg.get_rect()
        exitImg_rect.center = (width / 2, height * 0.59)

        screen.blit(pause, pauseRect)
        screen.blit(resumeImg, resumeImg_rect)
        screen.blit(exitImg, exitImg_rect)
        if resume:
            occupied = False
            menu = False
        elif exitButton:
            exit(0)

    if player.hp <= 0:
        hideAllCreatures(ogresList)
        hideAllCreatures(skeletonList)
        blacksmith.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        city.image = pygame.image.load("Graphics/blank.png").convert_alpha()
        background = pygame.image.load("Graphics/deathscreen.png")
        background = pygame.transform.scale(background, (width, height))
        isDead = True
        occupied = False

        exitImg = pygame.image.load("Graphics/exit.png").convert()
        exitImg_rect = exitImg.get_rect()
        exitImg_rect.center = (width / 2, height * 0.59)
        screen.blit(exitImg, exitImg_rect)
        if exitButton:
            exit(0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    i = i + 1

pygame.quit()
