import pygame
class Movement():
    #def __init__(self):

    def startMovement(self,occupied,player_pos,dt,width,height):
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

        if player_pos.x > width:
            player_pos.x = -20
        if player_pos.x < -20:
            player_pos.x = width

        if player_pos.y > height * 0.72:
            player_pos.y = -20
        if player_pos.y < -20:
            player_pos.y = height * 0.72

    def ogre_movement(self, o_pos, width, height):
        if o_pos.x > width:
            o_pos.x = -20
        if o_pos.x < -20:
            o_pos.x = width

        if o_pos.y > height * 0.72:
            o_pos.y = -20
        if o_pos.y < -20:
            o_pos.y = height * 0.72
