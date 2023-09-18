import pygame
import math


# a class to represent the players bullet on the game where a bullet is shot on the angle between the player position
# and mouse position
class PlayerBullet:

    def __init__(self, x_bullet, y_bullet, x_mouse, y_mouse):
        self.x = x_bullet
        self.y = y_bullet
        self.xm = x_mouse
        self.ym = y_mouse
        self.speed = 15
        self.angulo = math.atan2(self.y - self.ym, self.x - self.xm)
        self.x_pos = math.cos(self.angulo) * self.speed
        self.y_pos = math.sin(self.angulo) * self.speed

    def draw_circle(self, where_display):
        self.x -= self.x_pos
        self.y -= self.y_pos
        pygame.draw.rect(where_display, (255, 255, 255), (self.x, self.y,10,10))
        
    def rect(self):
        surface_bullet = pygame.Surface((10,10))
        rectangle_bullet = surface_bullet.get_rect(center = (self.x, self.y))
        return rectangle_bullet
        
    def check_if_hit(self, rect_bullet, rect_enemy):
        if rect_bullet.colliderect(rect_enemy):
            return True
        else:
            return False
