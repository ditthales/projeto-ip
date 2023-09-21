import pygame


class Inimigo:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def comportamento(self, tupla_jogador):
        # tupla_jogador no formato (x, y)
        if tupla_jogador[0] > self.x:
            self.x += 1.5
        if tupla_jogador[1] > self.y:
            self.y += 1.5
        if tupla_jogador[0] < self.x:
            self.x -= 1.5
        if tupla_jogador[1] < self.y:
            self.y -= 1.5

    def rect_inimigo(self):
        surface_inimigo = pygame.Surface((self.largura, self.altura))
        rectangle_inimigo = surface_inimigo.get_rect(center=(self.x, self.y))
        return rectangle_inimigo
