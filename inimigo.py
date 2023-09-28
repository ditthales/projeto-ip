import pygame


class Inimigo:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.offset = pygame.math.Vector2()
        self.image = pygame.image.load('bob.jpg')
        self.hp = 10

    def desenhar(self, tela, off_coords):
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        rect = self.rect_inicial()
        nova_pos = rect.center + self.offset
        tela.blit(self.image, nova_pos)

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

    def dano(self):
        self.hp -= 1

    def rect_inicial(self):
        surface_inimigo = pygame.Surface((self.largura, self.altura))
        rectangle_inimigo = surface_inimigo.get_rect(center=(self.x, self.y))
        return rectangle_inimigo

    def rect_inimigo(self, off_coords):
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        surface_coletavel = pygame.Surface((self.largura, self.altura))
        rectangle_coletavel = surface_coletavel.get_rect(center=(self.x + self.offset.x, self.y + self.offset.y))
        return rectangle_coletavel