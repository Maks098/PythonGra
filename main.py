import pygame
from Ogre import Ogre
from Player import Player
import threading

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
i=0

# data for player posioton, width and height
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
width = screen.get_width()
height = screen.get_height()
ogrepos = pygame.Vector2(700, 500)
# background setup
background = pygame.image.load("Graphics/maxresdefault.jpg")
background = pygame.transform.scale(background, (width, height))
pygame.display.flip()
# setup


pygame.display.flip()
# starting loop
while running:

    screen.blit(background, (0, 0))
    # looking for events
    for event in pygame.event.get():
        # quitting game
        if event.type == pygame.QUIT:
            running = False
    player = Player(player_pos)
    screen.blit(player.image, player_pos)
    if i==0:
        ogre = Ogre(ogrepos, dt)
    else:
        ogre=Ogre(updated,dt)
    thread = threading.Thread(target=ogre.randomWalk())
    thread.start()
    updated=ogre.pos
    screen.blit(ogre.image, ogre.pos)
    if (player.player_pos.x >= ogre.influenceSpherex.x) & (player.player_pos.x <= ogre.influenceSpherex.y) \
            & (player.player_pos.y >= ogre.influenceSpherey.x) & (player.player_pos.y <= ogre.influenceSpherey.y):
        running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()
    print(ogre.pos)

    dt = clock.tick(60) / 1000
    i=i+1
pygame.quit()
