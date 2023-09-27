import pygame


class Coletavel:
    def __init__(self, x, y, largura, altura, color):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.color = color
        self.offset = pygame.math.Vector2()
        if color == 'Red':
            self.image = pygame.image.load('heart.png')
        elif color == 'aquamarine':
            self.image = pygame.image.load('water.png')
        else:
            self.image = pygame.image.load('white.png')


    def desenhar(self, tela, off_coords):
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        rect = self.rect_inicial()
        nova_pos = rect.center + self.offset
        tela.blit(self.image, nova_pos)

    def rect_inicial(self):
        surface_coletavel = pygame.Surface((self.largura, self.altura))
        rectangle_coletavel = surface_coletavel.get_rect(center=(self.x, self.y))
        return rectangle_coletavel

    def rect_coleta(self, off_coords):
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        surface_coletavel = pygame.Surface((self.largura, self.altura))
        rectangle_coletavel = surface_coletavel.get_rect(center=(self.x + self.offset.x, self.y + self.offset.y))
        return rectangle_coletavel

    def get_pc(self):
        return self.x, self.y