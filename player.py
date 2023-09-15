import pygame

class Player:
    player_walk_images = [pygame.image.load(".\playerassets\Player_Sprite1.png"), pygame.image.load(".\playerassets\Player_Sprite2.png"), pygame.image.load(".\playerassets\Player_Sprite3.png")]
    player_idle = pygame.image.load(".\playerassets\Player_Sprite2.png")
    
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

    def rect(self):
        surface_player = pygame.Surface((self.largura, self.altura))
        rectangle_player = surface_player.get_rect(center = (self.x, self.y))
        return rectangle_player

    def morte_check(self, rectangle_player, rectangle_inimigo):
        if rectangle_player.colliderect(rectangle_inimigo):
            return True
        else:
            return False
    
    def coleta(self, rect_player, rect_list_coleta):
        index = rect_player.collidelist(rect_list_coleta)
        return index