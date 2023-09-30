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
pygame.display.set_caption('Desert Gun')
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
menu_imagem = pygame.image.load('./menuassets/menu.png')
morte_imagem = pygame.image.load('./menuassets/gameover.png')
jogar = pygame.image.load('./menuassets/botaojogar.png')
restart = pygame.image.load('./menuassets/pelanza.png')
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
    return random.randint(10, 1200)

def generate_random_y():
    return random.randint(10, 750)

def generate_drop():
    num_cor = random.randint(1, 3)

    if num_cor == 1:
        return 'Red'
    else:
        return 'aquamarine'

def raid_generation(lista_inimigos):
    posicao_x = generate_random_x()
    posicao_y = generate_random_y()
    num = random.randint(1, 3)
    if num == 1:
        tipo = 'fantasma'
    else:
        tipo = 'corvo'
    inimigo = Inimigo(posicao_x, posicao_y, 32, 32, tipo)
    lista_inimigos.append(inimigo)

def menu(tela, imagem, botao, pos, dimensoes):
    tela.blit(imagem, (0,0))
    tela.blit(botao, pos)
    surf_botao = pygame.surface.Surface(dimensoes)
    rect_botao = surf_botao.get_rect(topleft=pos)
    mouse_status = pygame.mouse.get_pressed()
    if mouse_status[0]:
        tupla_mouse = pygame.mouse.get_pos()
        surf_mouse = pygame.surface.Surface((25, 25))
        rect_mouse = surf_mouse.get_rect(topleft=tupla_mouse)
        if rect_mouse.colliderect(rect_botao):
            return True 
    pygame.display.update()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    return False


# INICIALIZE OBJECTS
jogador = Player(400, 200, 45, 35)
white = Coletavel(generate_random_x(), generate_random_y(), 16, 16, 'White')
gray = Coletavel(generate_random_x(), generate_random_y(), 16, 16, 'aquamarine')
black = Coletavel(generate_random_x(), generate_random_y(), 16, 16, 'Red')
mapa = Mapa()
mapa.criar_mapa(mundo)
vida = Vida()
sede = Sede()
player_bullets = []  # store players bullets
enemy_bullets = []
spray_bullets = []
ray_bullets = []
continuar = False
flag = False
timer_dano_agua = 0
reset_timer_1 = 0
reset_timer_2 = 0
contador = 0
offset = [0,0]
lista_sede = []
lista_vida = []
score = 0
onda = 0
raid_start = True
# GAME RENDER
while True:
    while not continuar:
        continuar = menu(tela, menu_imagem, jogar, (305, 250), (180, 77))

    if raid_start:
        onda += 1
        inimigos = []
        numero_inimigos = random.randint(1, 10)
        raid_start = False
        for n in range(0, numero_inimigos):
            raid_generation(inimigos)
    
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
        score += 100

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
            continuar = menu(tela, morte_imagem, restart, (350, 150), (100, 87))
        coletas = [0, 0, 0, 0]
        offset =[0,0]
        score = 0
        onda = 0
        raid_start = True
        inimigos = []
        enemy_bullets = []
        spray_bullets = []
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
            if i3.tipo == 'corvo':
                enemy_bullets.append(EnemyBullet(i3.x, i3.y, jogador.truepos[0], jogador.truepos[1], 4))
                i3.cooldown = 60
            elif i3.tipo == 'fantasma':
                spray_bullets.append(EnemyBullet(i3.x, i3.y, generate_random_x(), generate_random_y(), 3))
                if len(spray_bullets) >= 10:
                    i3.cooldown = 480
        else:
            i3.cooldown -= 1
            if i3.tipo == 'fantasma':
                if i3.cooldown == 1:
                    spray_bullets = []

    # SET TEXT
    texto_mortes = fonte2.render(f'{coletas[3]} kills', False, 'Black')
    texto_onda = fonte2.render(f'ONDA {onda}', False, 'Black')
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
    tela.blit(texto_onda, (350, 0))

    
    vida.desenhar()
    sede.desenhar()

    if len(player_bullets) > 30:
        while len(player_bullets) > 10:
            player_bullets.pop(0)
    
    if len(enemy_bullets) > 30:
        while len(enemy_bullets) > 10:
            enemy_bullets.pop(0)

    if len(spray_bullets) > 40:
        while len(enemy_bullets) > 20:
            spray_bullets.pop(0)

    for bala in enemy_bullets:
        bala.desenhar_offset(tela, offset)
        rect_bala = bala.rect()
        if bala.check_if_hit(rect_bala, rectangle_player):
            vida.dano()
            enemy_bullets.remove(bala)
            score -= 10

    for bala2 in spray_bullets:
        bala2.desenhar_offset(tela, offset)
        rect_bala = bala2.rect()
        if bala.check_if_hit(rect_bala, rectangle_player):
            vida.dano()
            spray_bullets.remove(bala2)
            score -= 10

    if sede.sede > 0:
        for bullet in player_bullets:
            bullet.desenhar(tela)
            rect_bullet = bullet.rect()
            for ri2 in rects_inm:
                if bullet.check_if_hit(rect_bullet, ri2):
                    try:
                        player_bullets.remove(bullet)
                        indx = rects_inm.index(ri2)
                        inm = inimigos[indx]
                        inm.dano()
                        if inm.hp <= 0:
                            numero_inimigos -= 1
                            score += 100
                            pygame.mixer.Sound.play(morte_inimigo)
                            inimigos.remove(inm)
                            cor_bloco = generate_drop()
                            if cor_bloco == 'aquamarine':
                                lista_sede.append(Coletavel(inm.x, inm.y, 15, 15, cor_bloco))
                            elif cor_bloco == 'Red':
                                lista_vida.append(Coletavel(inm.x, inm.y, 15, 15, cor_bloco))
                            coletas[3] += 1
                            if numero_inimigos == 0:
                                raid_start = True
                    except:
                        None
    
    # UPDATE RATIO / FPS
    pygame.display.update()
    relogio.tick(60) 