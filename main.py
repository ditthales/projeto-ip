import random
from sys import exit

from PlayersBullets import PlayerBullet
from barras import *
from coletavel import Coletavel
from inimigo import Inimigo
from mapa import *
from player import *

# GAME CONFIGURATION
pygame.init()
pygame.mixer.init()
icon = pygame.image.load('bob.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Prototipo')
relogio = pygame.time.Clock()

# SET SCREEN
screen_size = (800, 400)
tela = pygame.display.set_mode(screen_size)

# CREATE TEXT BASE
coletas = [0, 0, 0]  # branco, cinza, preto
kills = 0
kills_imagem = pygame.image.load('caveira.png')
fonte = pygame.font.Font('Minecraft.ttf', 20)
fonte2 = pygame.font.Font('Minecraft.ttf', 40)

# SOUND
tiro = pygame.mixer.Sound('./sons/shoot.wav')
pegar_vida = pygame.mixer.Sound('./sons/life.wav')
pegar_agua = pygame.mixer.Sound('./sons/drink.flac')
morte_inimigo = pygame.mixer.Sound('./sons/morte_inimigo.wav')
fundo = pygame.mixer.Sound('./sons/background.mp3')
sem_agua = pygame.mixer.Sound('./sons/sede.mp3')
moeda = pygame.mixer.Sound('./sons/moeda.wav')

# RANDOM COODINATIOR GENARATOR FOR COLECTABLES
def generate_random_x():
    return random.randint(0, 750)

def generate_random_y():
    return random.randint(0, 350)

def generate_drop():
    num_cor = random.randint(1, 2)

    if num_cor == 1:
        return 'aquamarine'
    else:
        return 'Red'

def menu(tela, fonte, texto):
    tela.fill('Magenta')
    texto_menu = fonte.render(texto, False, 'Green')
    tela.blit(texto_menu, (200, 200))
    pygame.display.update()

    for evento in pygame.event.get():

        if evento.type == pygame.KEYDOWN:
            return True

        elif evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    return False


# INICIALIZE OBJECTS
jogador = Player(400, 200, 45, 35)
white = Coletavel(generate_random_x(), generate_random_y(), 16, 16, 'White')
gray = Coletavel(generate_random_x(), generate_random_y(), 16, 16, 'aquamarine')
black = Coletavel(generate_random_x(), generate_random_y(), 16, 16, 'Red')
inimigo = Inimigo(generate_random_x(), generate_random_y(), 25, 25, 'Yellow')
inimigos = []
mapa = Mapa()
mapa.criar_mapa(mundo)
vida = Vida()
sede = Sede()
player_bullets = []  # store players bullets
t = 0
continuar = False
flag = False
timer_dano_agua = 0
reset_timer_1 = 0
reset_timer_2 = 0
contador = 0
offset = [0,0]
lista_sede = []
lista_vida = []
# GAME RENDER
while True:
    if reset_timer_1 <= 0:
        pygame.mixer.Sound.play(fundo)
        reset_timer_1 = 12780
    else:
        reset_timer_1 -= 1
    
    if reset_timer_2 <= 0:
        pygame.mixer.Sound.play(sem_agua)
        reset_timer_2 = 2460
    else:
        reset_timer_2 -= 1    

    lista_white = [white]
    # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # EXIT BUTTON
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # store PlayerBullet objects on a list for each click
    mouse_status = pygame.mouse.get_pressed()
    if mouse_status[0]:
        if (contador % 10 == 0) and sede.sede > 0:
            sede.sede_ativa()
            pygame.mixer.Sound.play(tiro)
            player_bullets.append(PlayerBullet(jogador.x, jogador.y, mouse_x, mouse_y))
        contador += 1
    else:
        contador = 0

    while not continuar:
        continuar = menu(tela, fonte, 'Aperte qualquer tecla para continuar')

    # DISPLAY BACKGROUND  
    mapa.desenhar(offset)

    # SET OBJECTS
    rectangle_player = jogador.rect()

    rects_branco = []
    for w in lista_white:
        rrr = w.rect_coleta(offset)
        rects_branco.append(rrr)

    rects_sede = []
    for g in lista_sede:
        r = g.rect_coleta(offset)
        rects_sede.append(r)
    
    rects_vida = []
    for b in lista_vida:
        rr = rectangle_black = b.rect_coleta(offset)
        rects_vida.append(rr)

    lista_colet = [rects_branco, rects_sede, rects_vida]

    rectangle_inimigo = inimigo.rect_inimigo(offset)

    # COLIDER MANAGER

    sede.sede_passiva()

    index1 = jogador.coleta(rectangle_player, rects_sede)
    index2 = jogador.coleta(rectangle_player, rects_vida)
    index3 = jogador.coleta(rectangle_player, rects_branco)
    
    if index1 >= 0:
        coletas[1] += 1
        lista_sede.pop(index1)
        sede.refrescar()
        pygame.mixer.Sound.play(pegar_agua)

    elif index2 >= 0:
        coletas[2] += 1
        lista_vida.pop(index2)
        vida.curar()
        pygame.mixer.Sound.play(pegar_vida)

    elif index3 >= 0:
        coletas[0] += 1
        pygame.mixer.Sound.play(moeda)
        white = Coletavel(generate_random_x(), generate_random_y(), 15, 15, 'White')

    if sede.sede <= 0:
        fundo.set_volume(0)
        sem_agua.set_volume(1)
        player_bullets = []
        if timer_dano_agua % 360 == 0:
            vida.dano()
        timer_dano_agua += 1
    else:
        fundo.set_volume(1)
        sem_agua.set_volume(0)

    if jogador.morte_check(rectangle_player, rectangle_inimigo):
        inimigo = Inimigo(generate_random_x(), generate_random_y(), 25, 25, 'Yellow')
        vida.dano()

    if vida.hp == 0:
        continuar = False
        while not continuar:
            continuar = menu(tela, fonte, 'Voce morreu :(! Aperte qualquer tecla pra continuar')
        coletas = [0, 0, 0]
        x = 400
        y = 200
        offset =[0,0]
        jogador.direcao.x = 0
        jogador.direcao.y = 0
        jogador.x = x
        jogador.y = y
        vida.reviver()
        sede.ressucitar()

    # player movement
    off_soma = jogador.move(screen_size, mapa.rect_colidiveis)
    if type(off_soma) == tuple:
        t = 60
    else:
        offset[0] += off_soma[0]
        offset[1] += off_soma[1]


    t -= 1
    if t <= 0:
        jogador.stored = [0, 0]


    # ENEMY MOVEMENT

    tupla_jogador = jogador.get_posicao()
    inimigo.comportamento(tupla_jogador)

    # SET TEXT
    texto = fonte.render(f'Coletou {coletas[0]} brancos, {coletas[1]} aguas e {coletas[2]} vidas', False, 'Green')
    texto_mortes = fonte2.render(f'{kills} kills', False, 'Black')

    # DISPLAY OBJECTS AND TEXT
    tela.fill(pygame.Color(92, 105, 159))
    mapa.desenhar(offset)
    jogador.desenhar(tela)

    #white.desenhar(tela, offset)
    
    for g1 in lista_sede:
        g1.desenhar(tela, offset)
    
    for b1 in lista_vida:
        b1.desenhar(tela, offset)

    inimigo.desenhar(tela, offset)

    #tela.blit(texto, (jogador.x - 160, jogador.y - 20))
    tela.blit(texto_mortes, (33, 0))
    tela.blit(kills_imagem, (0,0))
    
    vida.desenhar()
    sede.desenhar()

    if len(player_bullets) > 50:
        while len(player_bullets) > 30:
            player_bullets.pop(0)

    if sede.sede > 0:
        for bullet in player_bullets:
            bullet.desenhar(tela)
            rect_bullet = bullet.rect()
            if bullet.check_if_hit(rect_bullet, rectangle_inimigo):
                pygame.mixer.Sound.play(morte_inimigo)
                player_bullets.remove(bullet)
                cor_bloco = generate_drop()
                if cor_bloco == 'aquamarine':
                    lista_sede.append(Coletavel(inimigo.x, inimigo.y, 15, 15, cor_bloco))
                elif cor_bloco == 'Red':
                    lista_vida.append(Coletavel(inimigo.x, inimigo.y, 15, 15, cor_bloco))
                kills += 1
                inimigo = Inimigo(generate_random_x(), generate_random_y(), 25, 25, 'Yellow')
    
    # UPDATE RATIO / FPS
    pygame.display.update()
    relogio.tick(60)