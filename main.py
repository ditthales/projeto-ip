import pygame
from sys import exit
import random

# GAME CONFIGURATION
pygame.init()
icon = pygame.image.load('bob.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Prototipo')
relogio = pygame.time.Clock()

# SET SCREEN
screen_size = (800, 400)
tela = pygame.display.set_mode(screen_size)


# CREATE TEXT BASE
white_colected = 0
gray_colected = 0
black_colected = 0
fonte = pygame.font.Font('Minecraft.ttf', 20)

# RANDOM COODINATIOR GENARATOR FOR COLECTABLES
def genarate_random_x():
    return random.randint(0, 750)
def genarate_random_y():
    return random.randint(0, 350)




# PLAYER OBJECT
class Player:
    player_walk_images = [pygame.image.load("Player_Sprite1.png"),pygame.image.load("Player_Sprite2.png"),pygame.image.load("Player_Sprite3.png")]
    player_idle = pygame.image.load("Player_Sprite2.png")
    
    def __init__(self, x, y, altura, largura):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.animation_count = 0
        self.is_walking_right = False
        self.is_walking_left = False
    
    def posicionar(self, tela):
        self.animation_count = (self.animation_count + 1) % 36
        
        if self.is_walking_left:
            tela.blit(pygame.transform.scale(pygame.transform.flip(Player.player_walk_images[self.animation_count // 12], True, False),(32,42)),(self.x,self.y))
        elif self.is_walking_right:
            tela.blit(pygame.transform.scale(Player.player_walk_images[self.animation_count // 12],(32,42)),(self.x,self.y))
        else:
            tela.blit(pygame.transform.scale(Player.player_idle,(32,42)),(self.x,self.y))
        
        self.is_walking_right = False
        self.is_walking_left = False
        
    def get_posicao(self):
        return (self.x, self.y)

# COLECTABLE OBJECT
class Coletavel:
    def __init__(self, x, y, largura, altura, color):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.color = color
    
    def posicionar_c(self, tela):
        pygame.draw.rect(tela, self.color, (self.x, self.y, self.largura, self.altura))


    def get_pc(self):
        return(self.x, self.y)

# ENEMY OBJECT
class Inimigo:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
    
    def posicionar_in(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def comportamento(self, tupla_jogador):
        #tupla_jogador no formato (x, y)
        if(tupla_jogador[0] > self.x):
            self.x += 1.5
        if(tupla_jogador[1] > self.y):
            self.y += 1.5
        if(tupla_jogador[0] < self.x):
            self.x -= 1.5
        if(tupla_jogador[1] < self.y):
            self.y -= 1.5


# INICIALIZE OBJECTS
x = 400
y = 200
altura = 35
largura = 35
jogador = Player(x, y, altura, largura)
white = Coletavel(genarate_random_x(), genarate_random_y(), 15, 15,('White'))
gray = Coletavel(genarate_random_x(), genarate_random_y(), 15, 15,('Gray'))
black = Coletavel(genarate_random_x(), genarate_random_y(), 15, 15,('Black'))
inimigo = Inimigo(700, 350, 25, 25, 'Yellow')

# GAME RENDER
while True:
    # EXIT BUTTON
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            pygame.quit()
            exit()
    
    # DISPLAY BACKGROUND  
    tela.fill('Red')
    
    # SET OBJECTS
    surface_player = pygame.Surface((jogador.largura, jogador.altura))
    rectangle_player = surface_player.get_rect(center = (jogador.x, jogador.y))
    surface_white = pygame.Surface((white.largura, white.altura))
    rectangle_white = surface_player.get_rect(center = (white.x, white.y))
    surface_gray = pygame.Surface((gray.largura, gray.altura))
    rectangle_gray = surface_player.get_rect(center = (gray.x, gray.y))
    surface_black = pygame.Surface((black.largura, black.altura))
    rectangle_black = surface_player.get_rect(center = (black.x, black.y))
    surface_inimigo = pygame.Surface((inimigo.largura, inimigo.altura))
    rectangle_inimigo = surface_inimigo.get_rect(center = (inimigo.x, inimigo.y))


    # COLIDER MANAGER
    if rectangle_player.colliderect(rectangle_white):
        white_colected += 1
        white = Coletavel(genarate_random_x(), genarate_random_y(), 15, 15,('White'))    
    if rectangle_player.colliderect(rectangle_gray):
        gray_colected += 1
        gray = Coletavel(genarate_random_x(), genarate_random_y(), 15, 15,('Gray'))
    if rectangle_player.colliderect(rectangle_black):
        black_colected += 1
        black = Coletavel(genarate_random_x(), genarate_random_y(), 15, 15,('Black'))
    
    if rectangle_player.colliderect(rectangle_inimigo):
        white_colected = 0
        gray_colected = 0
        black_colected = 0
        x = 400
        y = 200
        inimigo = Inimigo(700, 350, 25, 25, 'Yellow')


    # CORE MOVEMENT
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_s] or keys[pygame.K_DOWN]):
        if y < screen_size[1] - altura:
            y += 3
            jogador.y = y
            jogador.is_walking_right = True
    elif(keys[pygame.K_w] or keys[pygame.K_UP]):
        if y > 0: 
            y -= 3
            jogador.y = y
            jogador.is_walking_right = True
    if(keys[pygame.K_d] or keys[pygame.K_RIGHT]):
        if x < screen_size[0] - largura:
            x += 3
            jogador.x = x
            jogador.is_walking_right = True
    elif(keys[pygame.K_a] or keys[pygame.K_LEFT]):
        if x > 0:
            x -= 3
            jogador.x = x
            jogador.is_walking_left = True

    # ENEMY MOVEMENT

    tupla_jogador = jogador.get_posicao()
    inimigo.comportamento(tupla_jogador)

    # SET TEXT
    texto = fonte.render(f'Coletou {white_colected} brancos, {gray_colected} cinzas e {black_colected} pretos', False, 'Green')

    # DISPLAY OBJECTS AND TEXT
    jogador.posicionar(tela)
    white.posicionar_c(tela)
    gray.posicionar_c(tela)
    black.posicionar_c(tela)
    inimigo.posicionar_in(tela)
    tela.blit(texto, (200, 200))

    # UPDATE RATIO / FPS
    pygame.display.update()
    relogio.tick(60)