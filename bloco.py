import pygame


class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y, group, argumento) -> None:

        super().__init__(group)
        self.argumento = argumento
        self.x = x
        self.y = y

        if argumento == 'pedra':

            self.image = pygame.image.load('pedra2.png')

        elif argumento == 'areia':

            self.image = pygame.image.load('areia.png')

        self.rect = self.image.get_rect(center=(x,y))
        self.rect_inicial = self.image.get_rect(center=(x,y))

    #def rect(self, pos):
     #   rect_novo = self.image.get_rect(center=pos)
      #  return rect_novo