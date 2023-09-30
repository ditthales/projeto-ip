import pygame

class Inimigo:
    
    def __init__(self, x, y, largura, altura, tipo):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.tipo = tipo
        self.offset = pygame.math.Vector2()
        self.image = pygame.image.load('bob.jpg')
        self.hp = 3
        self.cooldown = 90
        self.is_walking_right = False
        self.is_walking_left = False
        self.animation_count = 0
    
        if tipo == 'corvo':
            self.walk_images = [pygame.image.load("./birdassets/Bird1.png"),
                pygame.image.load("./birdassets/Bird2.png"),
                pygame.image.load("./birdassets/Bird3.png"),
                pygame.image.load("./birdassets/Bird4.png"),
                pygame.image.load("./birdassets/Bird5.png"),
                pygame.image.load("./birdassets/Bird6.png"),
                pygame.image.load("./birdassets/Bird7.png")]

        elif tipo == 'fantasma':
            self.walk_images = [pygame.image.load('./ghostassets/sprite_00.png'),
                                pygame.image.load('./ghostassets/sprite_00.png'),
                                pygame.image.load('./ghostassets/sprite_00.png'),
                                pygame.image.load('./ghostassets/sprite_00.png'),
                                pygame.image.load('./ghostassets/sprite_00.png'),
                                pygame.image.load('./ghostassets/sprite_00.png'),
                                pygame.image.load('./ghostassets/sprite_00.png')]

        elif tipo == 'esqueleto':
            self.walk_images= [pygame.image.load('./skeletonassets/skull.png'),
                                pygame.image.load('./skeletonassets/skull.png'),
                                pygame.image.load('./skeletonassets/skull.png'),
                                pygame.image.load('./skeletonassets/skull.png'),
                                pygame.image.load('./skeletonassets/skull.png'),
                                pygame.image.load('./skeletonassets/skull.png'),
                                pygame.image.load('./skeletonassets/skull.png')]

        else:
            self.walk_images= [pygame.image.load('bob.jpg'),
                                pygame.image.load('bob.jpg'),
                                pygame.image.load('bob.jpg'),
                                pygame.image.load('bob.jpg'),
                                pygame.image.load('bob.jpg'),
                                pygame.image.load('bob.jpg'),
                                pygame.image.load('bob.jpg')]


    def desenhar(self, tela, off_coords):
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        rect = self.rect_inicial()
        nova_pos = rect.center + self.offset
        
        self.animation_count = (self.animation_count + 1) % 84
        
        if self.is_walking_left:
            tela.blit(pygame.transform.scale(
                pygame.transform.flip(self.walk_images[self.animation_count // 12], True, False), (self.largura, self.altura)),
                (nova_pos))
        elif self.is_walking_right:
            tela.blit(pygame.transform.scale(self.walk_images[self.animation_count // 12], (self.altura, self.altura)),
                      (nova_pos))
        self.is_walking_right = False
        self.is_walking_left = False

    def comportamento(self, tupla_jogador):
        # tupla_jogador no formato (x, y)
        if tupla_jogador[1] > self.y:
            self.y += 1.5
        if tupla_jogador[1] < self.y:
            self.y -= 1.5
        if tupla_jogador[0] < self.x:
            self.x -= 1.5
            self.is_walking_right = True
        elif tupla_jogador[0] > self.x:
            self.x += 1.5
            self.is_walking_left = True

    def dano(self):
        self.hp -= 1
    
    def reposicionar(self, x, y):
        self.x = x
        self.y = y

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