import pygame
from sys import exit
import random
from player import Player
from coletavel import Coletavel
from inimigo import Inimigo
from PlayersBullets import PlayerBullet
from mapa import *
from barras import *

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
coletas = [0, 0, 0] #branco, cinza, preto
fonte = pygame.font.Font('Minecraft.ttf', 20)

# RANDOM COODINATIOR GENARATOR FOR COLECTABLES
def generate_random_x():
    return random.randint(0, 750)
def generate_random_y():
    return random.randint(0, 350)


def menu(tela, fonte, texto):
    tela.fill('Magenta')
    texto_menu = fonte.render(texto, False, 'Green')
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
gray = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('aquamarine'))
black = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('Red'))
inimigo = Inimigo(700, 350, 25, 25, 'Yellow')
mapa = Mapa()
mapa.criar_mapa(mundo)
vida = Vida()
sede = Sede()
player_bullets = []  # store players bullets

continuar = False

timer_dano_agua = 0
reset_timer = 0
contador = 0
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
    mouse_status = pygame.mouse.get_pressed()
    if(mouse_status[0] == True):
        if(contador % 10 == 0) and sede.sede > 0:
            sede.sede_ativa()
            player_bullets.append(PlayerBullet(jogador.x, jogador.y, mouse_x, mouse_y))
        contador += 1
    else:
        contador = 0

    while continuar == False:
        continuar = menu(tela, fonte, 'Aperte qualquer tecla para continuar')

    # DISPLAY BACKGROUND  
    mapa.desenhar()

    # SET OBJECTS
    rectangle_player = jogador.rect()

    rectangle_white = white.rect_coleta()
    rectangle_gray = gray.rect_coleta()
    rectangle_black = black.rect_coleta()
    
    lista_colet = [rectangle_white, rectangle_gray, rectangle_black]

    rectangle_inimigo = inimigo.rect_inimigo()

    # COLIDER MANAGER

    sede.sede_passiva()

    index = jogador.coleta(rectangle_player, lista_colet)
    if index >= 0:
        coletas[index] += 1
    
    if index == 0:
        white = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('White'))    
    if index == 1:
        gray = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('aquamarine'))
        sede.refrescar()
    if index == 2:
        black = Coletavel(generate_random_x(), generate_random_y(), 15, 15,('Red'))
        vida.curar()


    if sede.sede <= 0:
        player_bullets = []
        if timer_dano_agua % 360 == 0:
            vida.dano()
        timer_dano_agua += 1

    if jogador.morte_check(rectangle_player, rectangle_inimigo):
        inimigo = Inimigo(700, 350, 25, 25, 'Yellow')
        vida.dano()
    
    if(vida.hp == 0):
        continuar = False
        while continuar == False:
            continuar = menu(tela, fonte, 'Voce morreu :(! Aperte qualquer tecla pra continuar')
        coletas = [0, 0, 0]
        x = 400
        y = 200
        jogador.x = x
        jogador.y = y
        vida.reviver()
        sede.ressucitar()

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
    texto = fonte.render(f'Coletou {coletas[0]} brancos, {coletas[1]} aguas e {coletas[2]} vidas', False, 'Green')

    # DISPLAY OBJECTS AND TEXT
    mapa.desenhar()
    jogador.posicionar(tela)
    white.posicionar_c(tela)
    gray.posicionar_c(tela)
    black.posicionar_c(tela)
    inimigo.posicionar_in(tela)
    tela.blit(texto, (jogador.x - 160, jogador.y - 20))
    vida.desenhar_vida()
    sede.desenhar_sede()

    #if len(player_bullets) > 10:

    if sede.sede > 0:
        for bullet in player_bullets:
            bullet.draw_circle(tela)
            rect_bullet = bullet.rect()
            if bullet.check_if_hit(rect_bullet,rectangle_inimigo):
                player_bullets.remove(bullet)
                inimigo = Inimigo(700, 350, 25, 25, 'Yellow')

    # UPDATE RATIO / FPS
    pygame.display.update()
    relogio.tick(60)