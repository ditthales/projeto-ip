import pygame


class Vida:

    def __init__(self):
        self.hp = 10
        self.tela = pygame.display.get_surface()
    
    def desenhar(self):
        pygame.draw.rect(self.tela, 'Red', (10, 330, (10 * self.hp), 20))

    def curar(self):
        if self.hp < 10:
            self.hp += 1

    def dano(self):
        if self.hp > 0:
            self.hp -= 1

    def reviver(self):
        self.hp = 10


class Sede:

    def __init__(self):
        self.sede = 6000
        self.tela = pygame.display.get_surface()
    
    def desenhar(self):
        pygame.draw.rect(self.tela, 'aquamarine', (10, 350, (self.sede/50), 20))       

    def sede_passiva(self):
        if(self.sede > 0):
            self.sede -= 3

    def sede_ativa(self):
        if(self.sede > 59):
            self.sede -= 60

    def refrescar(self):
        self.sede += 600

    def ressucitar(self):
        self.sede = 6000
