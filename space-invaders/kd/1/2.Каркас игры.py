import pygame

from random import randint, uniform



# CONSTANTS
WIDTH  = 500
HEIGHT = 500
FPS    = 60

BLACK = (0, 0, 0)



# INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



# MAIN LOOP
motion  = 'stop'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # drawing
    screen.fill(BLACK)
    pygame.display.update()
    clock.tick(FPS)



pygame.quit()
