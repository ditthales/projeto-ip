import pygame
from bloco import Bloco

mundo = [
    ['CE', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM',
     'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM', 'CM',
     'CM', 'CM', 'CM', 'CM', 'CD'],
    ['ME', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'L', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', '2', 'O',
     'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'X', 'MD'],
    ['ME', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'C', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', '2', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'C', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'X', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O',
     'O', 'O', 'O', '2', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     '2', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', '2', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', '2',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2',
     'O', 'X', '2', 'O', 'MD'],
    ['ME', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', '2', 'O', 'O',
     'O', 'O', '2', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', '2',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O',
     'O', 'O', '2', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', '2',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', '2', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', '2', 'O', 'O', 'O', 'O',
     'O', 'X', '2', 'O', 'MD'],
    ['ME', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'L', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', '2', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'X', 'O', 'O', 'L', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O',
     'O', 'X', 'O', 'O', 'MD'],
    ['ME', '2', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'L', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O',
     'O', 'O', '2', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', '2', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', '2', 'O', 'O', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', '2', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O',
     'O', '2', 'O', '2', 'MD'],
    ['ME', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
     'O', 'O', 'O', 'O', 'MD'],
    ['ME', 'X', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O',
     'O', '2', 'O', '2', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '2', 'O', 'O', 'O', 'O', 'O', '2', 'O',
     '2', 'O', 'O', 'X', 'MD'],
    ['IE', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM',
     'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM', 'IM',
     'IM', 'IM', 'IM', 'IM', 'ID']]


# LEGENDA:
# 'O' - espaço vazio (fundo)
# 'X' - pedra
#

class Mapa:
    def __init__(self):
        self.tela = pygame.display.get_surface()

        self.sprites_visiveis = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.rect_colidiveis = []
        self.offset = pygame.math.Vector2()

    def criar_mapa(self, mundo):
        for t_linha in enumerate(mundo):
            l_index = t_linha[0]
            for t_bloco in enumerate(t_linha[1]):
                c_index = t_bloco[0]
                x = c_index * 32
                y = l_index * 32
                if t_bloco[1] == 'X':
                    Bloco(x, y, [self.obstaculos], 'pedra')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'CD':
                    Bloco(x, y, [self.obstaculos], 'borda_cd')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'CE':
                    Bloco(x, y, [self.obstaculos], 'borda_ce')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'CM':
                    Bloco(x, y, [self.obstaculos], 'borda_cm')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'ID':
                    Bloco(x, y, [self.obstaculos], 'borda_id')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'IE':
                    Bloco(x, y, [self.obstaculos], 'borda_ie')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'IM':
                    Bloco(x, y, [self.obstaculos], 'borda_im')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'MD':
                    Bloco(x, y, [self.obstaculos], 'borda_md')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'ME':
                    Bloco(x, y, [self.obstaculos], 'borda_me')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == '2':
                    Bloco(x, y, [self.sprites_visiveis], 'areia2')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                elif t_bloco[1] == 'O':
                    Bloco(x, y, [self.sprites_visiveis], 'areia')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                elif t_bloco[1] == 'C':
                    Bloco(x, y, [self.obstaculos], 'cacto')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                elif t_bloco[1] == 'L':
                    Bloco(x, y, [self.obstaculos], 'lapide')
                    surface_block = pygame.Surface((32,32))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
    def desenhar(self, off_coords):
        self.rect_colidiveis = []
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        for sprite in self.sprites_visiveis:
            nova_pos = sprite.rect.topleft + self.offset
            self.tela.blit(sprite.image, nova_pos)
        for sprite in self.obstaculos:
            nova_pos = sprite.rect_inicial.topleft + self.offset
            sprite.rect.topleft = nova_pos
            self.rect_colidiveis.append(sprite.rect)
            self.tela.blit(sprite.image, nova_pos)