import pygame
from Ogre import Ogre
from Player import Player
from BattleView import BattleView
import threading

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
i = 0

# data for player posioton, width and height
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
width = screen.get_width()
height = screen.get_height()
ogrepos = pygame.Vector2(700, 500)
ogrepos1 = pygame.Vector2(1000, 500)

flag = False
# background setup
background = pygame.image.load("Graphics/maxresdefault.jpg")
background = pygame.transform.scale(background, (width, height))
pygame.display.flip()
# setup
lockedPosOgre = 0, 0
lockedPosOgre1 = 0, 0

# listForOgres=(ogre,ogre1)
listForPositionsOfOgres = ()
pygame.display.flip()
# starting loop
while running:

    screen.blit(background, (0, 0))
    # looking for events
    for event in pygame.event.get():
        # quitting game
        if event.type == pygame.QUIT:
            running = False
    player = Player(player_pos, flag)
    screen.blit(player.image, player_pos)
    if i == 0:
        ogre = Ogre(ogrepos, dt, flag, )
        ogre1 = Ogre(ogrepos1, dt, flag, )
    else:
        ogre = Ogre(updated, dt, flag, )
        ogre1 = Ogre(updated1, dt, flag, )
    lockedPosOgre = ogre.pos
    lockedPosOgre1 = ogre1.pos

    thread = threading.Thread(target=ogre.randomWalk())
    thread.start()
    thread1 = threading.Thread(target=ogre1.randomWalk())
    thread1.start()

    updated = ogre.pos
    updated1 = ogre1.pos

    screen.blit(ogre.image, ogre.pos)
    screen.blit(ogre1.image, ogre1.pos)
    if (player.player_pos.x >= ogre.influenceSpherex.x) & (player.player_pos.x <= ogre.influenceSpherex.y) \
            & (player.player_pos.y >= ogre.influenceSpherey.x) & (player.player_pos.y <= ogre.influenceSpherey.y):
        battleView = BattleView(screen, int(ogre.hp), int(player.hp), flag)
        background = pygame.image.load("Graphics/BattleView.png").convert()
        background = pygame.transform.scale(background, (width, height))
        flag = True

    if (player.player_pos.x >= ogre1.influenceSpherex.x) & (player.player_pos.x <= ogre1.influenceSpherex.y) \
            & (player.player_pos.y >= ogre1.influenceSpherey.x) & (player.player_pos.y <= ogre1.influenceSpherey.y):
        running = False

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
