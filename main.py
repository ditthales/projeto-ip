import pygame
from sys import exit
import random


pygame.init()

teste = pygame.image.load('bob.jpg')

tela = pygame.display.set_mode((800, 400))
tela.fill('Red')

pygame.display.set_caption('Prototipo')
pygame.display.set_icon(teste)

relogio = pygame.time.Clock()

var = 0
var2 = 0
var3 = 0

fonte = pygame.font.Font('Minecraft.ttf', 20)
texto = fonte.render(f'Coletou {var} brancos, {var2} cinzas e {var3} pretos', False, 'Green')

class Player:
    def __init__(self, x, y, altura, largura):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
    
    def posicionar(self, tela):
        pygame.draw.rect(tela, ('Blue'), (self.x, self.y, self.largura, self.altura))
    
    def get_posicao(self):
        return (self.x, self.y)

class Coletavel:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
    
    def posicionar_c(self, tela):
        pygame.draw.rect(tela, ('White'), (self.x, self.y, self.largura, self.altura))


    def get_pc(self):
        return(self.x, self.y)
    
class Coletavel2:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
    
    def posicionar_c(self, tela):
        pygame.draw.rect(tela, ('Gray'), (self.x, self.y, self.largura, self.altura))


    def get_pc(self):
        return(self.x, self.y)
    
class Coletavel3:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
    
    def posicionar_c(self, tela):
        pygame.draw.rect(tela, ('Black'), (self.x, self.y, self.largura, self.altura))


    def get_pc(self):
        return(self.x, self.y)


x_c = random.randint(0, 800)
y_c = random.randint(0, 400)

coletar = Coletavel(x_c, y_c, 15, 15)

x_c2 = random.randint(0, 800)
y_c2 = random.randint(0, 400)

coletar2 = Coletavel2(x_c2, y_c2, 15, 15)

x_c3 = random.randint(0, 800)
y_c3 = random.randint(0, 400)

coletar3 = Coletavel3(x_c3, y_c3, 15, 15)

x = 400
y = 200
altura = 20
largura = 20
jogador = Player(x, y, altura, largura)

while True:
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            pygame.quit()
            exit()

    texto = fonte.render(f'Coletou {var} brancos, {var2} cinzas e {var3} pretos', False, 'Green')

    tela.blit(texto, (200, 200))

    surf = pygame.Surface((jogador.largura, jogador.altura))
    rect = surf.get_rect(center = (jogador.x, jogador.y))

    surf2 = pygame.Surface((coletar.largura, coletar.altura))
    rect2 = surf.get_rect(center = (coletar.x, coletar.y))

    surf3 = pygame.Surface((coletar2.largura, coletar2.altura))
    rect3 = surf.get_rect(center = (coletar2.x, coletar2.y))

    surf4 = pygame.Surface((coletar3.largura, coletar3.altura))
    rect4 = surf.get_rect(center = (coletar3.x, coletar3.y))

    tela.blit(surf, rect)
    tela.blit(surf2, rect2)
    tela.blit(surf3, rect3)
    tela.blit(surf4, rect4)

    if rect.colliderect(rect2):
        var += 1
        x_c = random.randint(0, 800)
        y_c = random.randint(0, 400)

        coletar = Coletavel(x_c, y_c, 15, 15)
        coletar.posicionar_c(tela)
    elif rect.colliderect(rect3):
        var2 += 1
        x_c2 = random.randint(0, 800)
        y_c2 = random.randint(0, 400)

        coletar2 = Coletavel2(x_c2, y_c2, 15, 15)
        coletar2.posicionar_c(tela)
    elif rect.colliderect(rect4):
        var3 += 1
        x_c3 = random.randint(0, 800)
        y_c3 = random.randint(0, 400)

        coletar3 = Coletavel3(x_c3, y_c3, 15, 15)
        coletar3.posicionar_c(tela)


    keys = pygame.key.get_pressed()

    if(keys[pygame.K_d]):
        x += 3
    if(keys[pygame.K_s]):
        y += 3
    if(keys[pygame.K_w]):
        y -= 3
    if(keys[pygame.K_a]):
        x -= 3


    tela.fill('Red')
    tela.blit(texto, (200, 200))

    jogador = Player(x, y, altura, largura)
    jogador.posicionar(tela)

    coletar.posicionar_c(tela)
    coletar2.posicionar_c(tela)
    coletar3.posicionar_c(tela)

    pygame.display.update()
    relogio.tick(60)