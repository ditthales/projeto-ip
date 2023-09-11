import pygame
import sys

pygame.init()

class Player:
    # Make player and position
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.display_scroll = [0,0]
        self.current_x_position = x
        self.current_y_position = y
    
    # Draw player
    def main(self, display):
        self.current_x_position = self.x+self.display_scroll[0]
        self.current_y_position = self.y+self.display_scroll[1]
        pygame.draw.rect(display, (255, 0, 0), (self.current_x_position, self.current_y_position, self.width, self.height))

player = Player(400, 300, 32, 32)

screen_size = (800, 600)

display = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()


while True:
     # Display color
    display.fill((24, 164, 86))
    
     # Game EXIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    
    # Player
    player.main(display)
    
    # Move and Key press
    keys = pygame. key.get_pressed ()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player.current_x_position > 0:
            player.display_scroll[0] -= 5
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player.current_x_position < screen_size[0] - player.width:
            player.display_scroll[0] += 5
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if player.current_y_position > 0:
            player.display_scroll[1] -= 5
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if player.current_y_position < screen_size[1] - player.height:
            player.display_scroll[1] += 5
    
     # Display configurations
    clock.tick(60)
    pygame.display.update()