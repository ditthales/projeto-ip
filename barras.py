import pygame
pygame.mixer.init()


class Vida:

    hit = pygame.mixer.Sound('./sons/dano.wav')
    hit.set_volume(0.7)

    def __init__(self):
        self.hp = 20
        self.tela = pygame.display.get_surface()
    
    def desenhar(self):
        pygame.draw.rect(self.tela, 'Red', (10, 330, (10 * self.hp), 20))

    def curar(self):
        if self.hp < 10:
            self.hp += 5

    def dano(self):
        pygame.mixer.Sound.play(self.hit)
        if self.hp > 0:
            self.hp -= 1

    def reviver(self):
        self.hp = 20


class Sede:

    def __init__(self):
        self.sede = 6000
        self.tela = pygame.display.get_surface()
    
    def desenhar(self):
        pygame.draw.rect(self.tela, 'aquamarine', (10, 350, (self.sede/50), 20))       

    def sede_passiva(self):
        if(self.sede > 0):
            self.sede -= 2

    def sede_ativa(self):
        if(self.sede > 59):
            self.sede -= 60

    def refrescar(self):
        self.sede += 1500

    def ressucitar(self):
        self.sede = 6000
