import pygame


class Coletavel:
    def __init__(self, x, y, largura, altura, color):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.color = color
    
    def desenhar(self, tela, lista = []):
        for i in lista:
            pygame.draw.rect(tela, i.color, (i.x, i.y, i.largura, i.altura))

    def rect_coleta(self):
        surface_coletavel = pygame.Surface((self.largura, self.altura))
        rectangle_coletavel = surface_coletavel.get_rect(center=(self.x, self.y))
        return rectangle_coletavel

    def get_pc(self):
        return self.x, self.y
