import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, pos, group, argumento) -> None:
        super().__init__(group)
        self.argumento = argumento
        if(argumento == 'pedra'):
            self.image = pygame.image.load('pedra2.png')
        elif(argumento == 'areia'):
            self.image = pygame.image.load('areia.png')
        self.rect = self.image.get_rect(center = pos)