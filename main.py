import pygame
from CameraGroup import CameraGroup
from Player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
width = screen.get_width()
height = screen.get_height()

bg = pygame.image.load("Graphics/maxresdefault.jpg")
bg = pygame.transform.scale(bg, (width, height))

camera_group = CameraGroup
player = Player((300,200), camera_group)
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player = pygame.image.load("Graphics/PlayerTest.png").convert_alpha()

    # screen.fill("white")
    screen.blit(player, (player_pos))
    pygame.display.flip()
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     if player_pos.y >= 0:
    #         player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     if player_pos.y <= 1050:
    #         player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     if player_pos.x >= 0:
    #         player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     if player_pos.x <= 1850:
    #         player_pos.x += 300 * dt

    # camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
