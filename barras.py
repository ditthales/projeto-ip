import pygame

class Vida:

    def __init__(self):
        self.hp = 10
        self.tela = pygame.display.get_surface()
    
    def desenhar_vida(self):
        pygame.draw.rect(self.tela, 'Red', (10, 350, (10 * self.hp), 20))
    
    def curar(self):
        if(self.hp < 10):
            self.hp += 1
    
    def dano(self):
        if(self.hp > 0):
            self.hp -= 1
    
    def reviver(self):
        self.hp = 10