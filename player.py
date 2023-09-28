import pygame


class Player:
    player_walk_images = [pygame.image.load("./playerassets/Player_Sprite1.png"),
                          pygame.image.load("./playerassets/Player_Sprite2.png"),
                          pygame.image.load("./playerassets/Player_Sprite3.png")]
    player_idle = pygame.image.load("./playerassets/Player_Sprite2.png")

    def __init__(self, x, y, altura, largura):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.animation_count = 0
        self.is_walking_right = False
        self.is_walking_left = False
        self.previous_location = [x,y]
        self.direcao = pygame.math.Vector2()
        self.stored = [0, 0]
        self.flag = False

    def move(self, screen_size,rect_colidiveis):

        keys = pygame.key.get_pressed()

        off_soma = [0, 0]

        index = self.coleta(self.rect(), rect_colidiveis)

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            if self.y < screen_size[1] - self.altura:
                if self.stored[1] >= 0:
                    self.direcao.y += 3
                    self.is_walking_right = True
                    off_soma[1] -= 3
                    

        elif (keys[pygame.K_w] or keys[pygame.K_UP]):
            if self.y > 0:
                if self.stored[1] <= 0:
                    self.direcao.y -= 3
                    self.is_walking_right = True
                    off_soma[1] += 3


        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            if self.x < screen_size[0] - self.largura:
                if self.stored[0] >= 0:
                    self.direcao.x += 3
                    self.is_walking_right = True
                    off_soma[0] -= 3


        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            if self.x > 0:
                if self.stored[0] <= 0:
                    self.direcao.x -= 3
                    self.is_walking_left = True
                    off_soma[0] += 3


        if index != -1 and not self.flag:
            self.stored = off_soma
            self.flag = True
        
        if index == -1:
            self.previous_location = self.get_posicao_list()
            self.flag = False
            self.stored = [0,0]

        return off_soma

    def desenhar(self, tela):
        self.animation_count = (self.animation_count + 1) % 36

        if self.is_walking_left:
            tela.blit(pygame.transform.scale(
                pygame.transform.flip(Player.player_walk_images[self.animation_count // 12], True, False), (32, 42)),
                (self.x, self.y))
        elif self.is_walking_right:
            tela.blit(pygame.transform.scale(Player.player_walk_images[self.animation_count // 12], (32, 42)),
                      (self.x, self.y))
        else:
            tela.blit(pygame.transform.scale(Player.player_idle, (32, 42)), (self.x, self.y))

        self.is_walking_right = False
        self.is_walking_left = False

    def get_posicao(self):
        pos = (self.x, self.y)
        nova_p = pos + self.direcao
        return nova_p
    
    def get_posicao_list(self):
        pos = (self.x, self.y)
        nova_p = pos + self.direcao
        return [nova_p[0], nova_p[1]]

    def rect(self):
        surface_player = pygame.Surface((self.largura, self.altura))
        rectangle_player = surface_player.get_rect(center = (self.x + 15, self.y + 25))
        return rectangle_player

    @staticmethod
    def morte_check(rectangle_player, rectangle_inimigo):
        if rectangle_player.colliderect(rectangle_inimigo):
            return True
        else:
            return False

    def morte(self):
        self.direcao.x = 0
        self.direcao.y = 0
        self.x = 400
        self.y = 200

    @staticmethod
    def coleta(rect_player, rect_list_coleta):
        index = rect_player.collidelist(rect_list_coleta)
        return index