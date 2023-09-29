import pygame
import math


# a class to represent the players bullet on the game where a bullet is shot on the angle between the player position
# and mouse position
class PlayerBullet:

    def __init__(self, x_bullet, y_bullet, x_mouse, y_mouse, speed):
        self.x = x_bullet
        self.y = y_bullet
        self.xm = x_mouse
        self.ym = y_mouse
        self.speed = speed
        self.angulo = math.atan2(self.y - self.ym, self.x - self.xm)
        self.x_pos = math.cos(self.angulo) * self.speed
        self.y_pos = math.sin(self.angulo) * self.speed
        self.offset = pygame.math.Vector2()

    def desenhar(self, where_display, off_coords):
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        self.x -= self.x_pos
        self.y -= self.y_pos
        nova_pos = (self.x, self.y) + self.offset
        where_display.blit(pygame.transform.scale(pygame.image.load('cuspe.png'),(10,10)), nova_pos)

    def rect(self):
        surface_bullet = pygame.Surface((10,10))
        rectangle_bullet = surface_bullet.get_rect(center = (self.x, self.y))
        return rectangle_bullet
        
    def check_if_hit(self, rect_bullet, rect_enemy):
        if rect_bullet.colliderect(rect_enemy):
            return True
        else:
            return False
