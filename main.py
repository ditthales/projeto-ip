import pygame
from sys import exit
import random
from player import Player
from coletavel import Coletavel
from inimigo import Inimigo
from PlayersBullets import PlayerBullet

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
def generate_random_x():
    return random.randint(0, 750)
def generate_random_y():
    return random.randint(0, 350)


def menu(tela, fonte):
    tela.fill('Magenta')
    texto_menu = fonte.render('Aperte qualquer tecla para continuar', False, 'Green')
    tela.blit(texto_menu, (200, 200))
    pygame.display.update()
    for evento in pygame.event.get():
        if(evento.type == pygame.KEYDOWN):
            return True
        elif (evento.type == pygame.QUIT):
            pygame.quit()
            exit()
    return False

# INICIALIZE OBJECTS
x = 400
y = 200
altura = 45
largura = 35
jogador = Player(x, y, altura, largura)
white = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('White'))
gray = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('Gray'))
black = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('Black'))
inimigo = Inimigo(700, 350, 25, 25, 'Yellow')
player_bullets = []  # store players bullets

continuar = False

# GAME RENDER
while True:
    # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # EXIT BUTTON
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            pygame.quit()
            exit()

        # store PlayerBullet objects on a list for each click
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                player_bullets.append(PlayerBullet(jogador.x, jogador.y, mouse_x, mouse_y))

    while continuar == False:
        continuar = menu(tela, fonte)

    # DISPLAY BACKGROUND  
    tela.fill('Red')
    
    # SET OBJECTS
    rectangle_player = jogador.rect()

    rectangle_white = white.rect_coleta()
    rectangle_gray = gray.rect_coleta()
    rectangle_black = black.rect_coleta()
    
    rectangle_inimigo = inimigo.rect_inimigo()

    # COLIDER MANAGER
    if rectangle_player.colliderect(rectangle_white):
        white_colected += 1
        white = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('White'))    
    if rectangle_player.colliderect(rectangle_gray):
        gray_colected += 1
        gray = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('Gray'))
    if rectangle_player.colliderect(rectangle_black):
        black_colected += 1
        black = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('Black'))
    
    if rectangle_player.colliderect(rectangle_inimigo):
        white_colected = 0
        gray_colected = 0
        black_colected = 0
        x = 400
        y = 200
        jogador.x = x
        jogador.y = y
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

    for bullet in player_bullets:
        bullet.draw_circle(tela)

    # UPDATE RATIO / FPS
    pygame.display.update()
    relogio.tick(60)