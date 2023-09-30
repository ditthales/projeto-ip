import random
from sys import exit
from bullets import *
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
coletas = [0, 0, 0, 0]  # branco, agua, vida, kills
kills_imagem = pygame.image.load('caveira.png')
agua_imagem = pygame.image.load('water.png')
vida_imagem = pygame.image.load('heart.png')
moeda_imagem = pygame.image.load('moeda.png')
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
mapa = Mapa()
mapa.criar_mapa(mundo)
vida = Vida()
sede = Sede()
player_bullets = []  # store players bullets
enemy_bullets = []
continuar = False
flag = False
timer_dano_agua = 0
reset_timer_1 = 0
reset_timer_2 = 0
contador = 0
offset = [0,0]
lista_sede = []
lista_vida = []
cooldown = 60
score = 0
# GAME RENDER
while True:
    inimigos = [inimigo]
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

    rects_inm = []
    for i in inimigos:
        rectangle_inimigo = i.rect_inimigo(offset)
        rects_inm.append(rectangle_inimigo)

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
        score += 10

    elif index2 >= 0:
        coletas[2] += 1
        lista_vida.pop(index2)
        vida.curar()
        pygame.mixer.Sound.play(pegar_vida)
        score += 10

    elif index3 >= 0:
        coletas[0] += 1
        pygame.mixer.Sound.play(moeda)
        white = Coletavel(generate_random_x(), generate_random_y(), 15, 15, 'White')
        score += 50

    if sede.sede <= 0:
        fundo.set_volume(0)
        sem_agua.set_volume(0.7)
        player_bullets = []
        if timer_dano_agua % 360 == 0:
            vida.dano()
        timer_dano_agua += 1
    else:
        fundo.set_volume(0.8)
        sem_agua.set_volume(0)

    if jogador.morte_check(rectangle_player, rects_inm) != -1:
        index = jogador.morte_check(rectangle_player, rects_inm)
        inimigos[index].reposicionar(generate_random_x(), generate_random_y())
        vida.dano()
        score -= 10

    if vida.hp == 0:
        continuar = False
        while not continuar:
            continuar = menu(tela, fonte, 'Voce morreu :(! Aperte qualquer tecla pra continuar')
        coletas = [0, 0, 0, 0]
        offset =[0,0]
        score = 0
        jogador.morte()
        vida.reviver()
        sede.ressucitar()

    # player movement
    off_soma = jogador.move(screen_size, mapa.rect_colidiveis)
    offset[0] += off_soma[0]
    offset[1] += off_soma[1]

    # ENEMY MOVEMENT

    tupla_jogador = jogador.get_posicao()
    for i3 in inimigos:
        i3.comportamento(tupla_jogador)
    if i3.cooldown == 0:
        enemy_bullets.append(EnemyBullet(i3.x, i3.y, jogador.truepos[0], jogador.truepos[1], 7))
        i3.cooldown = 60
    else:
        i3.cooldown -= 1

    # SET TEXT
    texto_mortes = fonte2.render(f'{coletas[3]} kills', False, 'Black')
    texto_moedas = fonte.render(f'{coletas[0]}', False, 'Yellow')
    texto_agua = fonte.render(f'{coletas[1]}', False, 'Blue')
    texto_vida = fonte.render(f'{coletas[2]}', False, 'Red')
    texto_score = fonte2.render(f'{score}', False, 'White')

    # DISPLAY OBJECTS AND TEXT
    tela.fill(pygame.Color(92, 105, 159))
    mapa.desenhar(offset)
    jogador.desenhar(tela)

    white.desenhar(tela, offset)
    
    for g1 in lista_sede:
        g1.desenhar(tela, offset)
    
    for b1 in lista_vida:
        b1.desenhar(tela, offset)

    for i2 in inimigos:
        i2.desenhar(tela, offset)

    tela.blit(texto_mortes, (33, 0))
    tela.blit(kills_imagem, (0,0))
    tela.blit(texto_moedas, (10, 40))
    tela.blit(moeda_imagem, (40, 40))
    tela.blit(texto_agua, (10, 60))
    tela.blit(agua_imagem, (40, 60))
    tela.blit(texto_vida, (10, 80))
    tela.blit(vida_imagem, (40, 80))
    tela.blit(texto_score, (700, 0))
    
    vida.desenhar()
    sede.desenhar()

    if len(player_bullets) > 30:
        while len(player_bullets) > 10:
            player_bullets.pop(0)
    
    if len(enemy_bullets) > 30:
        while len(enemy_bullets) > 10:
            enemy_bullets.pop(0)

    for bala in enemy_bullets:
        bala.desenhar_offset(tela, offset)
        rect_bala = bala.rect()
        if bala.check_if_hit(rect_bala, rectangle_player):
            vida.dano()
            enemy_bullets.remove(bala)
            score -= 10

    if sede.sede > 0:
        for bullet in player_bullets:
            bullet.desenhar(tela)
            rect_bullet = bullet.rect()
            for ri2 in rects_inm:
                if bullet.check_if_hit(rect_bullet, rectangle_inimigo):
                    player_bullets.remove(bullet)
                    indx = rects_inm.index(ri2)
                    inm = inimigos[indx]
                    inm.dano()
                    if inm.hp <= 0:
                        score += 100
                        pygame.mixer.Sound.play(morte_inimigo)
                        cor_bloco = generate_drop()
                        if cor_bloco == 'aquamarine':
                            lista_sede.append(Coletavel(inm.x, inm.y, 15, 15, cor_bloco))
                        elif cor_bloco == 'Red':
                            lista_vida.append(Coletavel(inm.x, inm.y, 15, 15, cor_bloco))
                        coletas[3] += 1
                        inm.reposicionar(generate_random_x(), generate_random_y())
                        inm.hp = 10
    
    # UPDATE RATIO / FPS
    pygame.display.update()
    print(relogio)
    relogio.tick(60) 