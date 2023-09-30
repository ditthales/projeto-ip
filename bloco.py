import pygame


class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y, group, argumento) -> None:

        super().__init__(group)
        self.argumento = argumento
        self.x = x
        self.y = y

        if argumento == 'pedra':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/pedra.png'),(32,32))
            
        elif argumento == 'borda_cd':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_cd.png'),(32,32))
            
        elif argumento == 'borda_ce':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_ce.png'),(32,32))
            
        elif argumento == 'borda_cm':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_cm.png'),(32,32))
            
        elif argumento == 'borda_id':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_id.png'),(32,32))
            
        elif argumento == 'borda_ie':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_ie.png'),(32,32))
            
        elif argumento == 'borda_im':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_im.png'),(32,32))
            
        elif argumento == 'borda_md':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_md.png'),(32,32))
            
        elif argumento == 'borda_me':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/quina_me.png'),(32,32))

        elif argumento == 'areia':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/areia.png'),(32,32))
            
        elif argumento == 'areia2':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/areia2.png'),(32,32))

        self.rect = self.image.get_rect(topleft=(x,y))
        self.rect_inicial = self.image.get_rect(topleft=(x,y))