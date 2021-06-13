import pygame

from random import randint, uniform



# CONSTANTS
WIDTH  = 500
HEIGHT = 500
FPS    = 60

SHIP_SPEED = 5

BLACK = (0, 0, 0)



# INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ship
ship_img = pygame.image.load('razorinv.png')
w, h     = 60, 50
x, y     = WIDTH/2 - w/2, HEIGHT/2 + 80
ship     = pygame.Rect(x, y, w, h)



# MAIN LOOP
motion  = 'stop'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motion = 'left'
            elif event.key == pygame.K_RIGHT:
                motion = 'right'
            elif event.key == pygame.K_UP:
                motion = 'up'
            elif event.key == pygame.K_DOWN:
                motion = 'down'
        elif event.type == pygame.KEYUP:
            if event.key in [
                pygame.K_LEFT, pygame.K_RIGHT,
                pygame.K_UP, pygame.K_DOWN
            ]:
                motion = 'stop'


    # ship motion
    if motion == 'left' and x - SHIP_SPEED > 0:
        x -= SHIP_SPEED
    elif(
        motion == 'right' and
        ship.right + SHIP_SPEED < WIDTH
    ):
        x += SHIP_SPEED
    elif motion == 'up' and y - SHIP_SPEED > 0:
        y -= SHIP_SPEED
    elif(
        motion == 'down' and
        ship.bottom + SHIP_SPEED < HEIGHT
    ):
        y += SHIP_SPEED
    ship.left = x
    ship.top  = y

    
    # drawing
    screen.fill(BLACK)
    screen.blit(ship_img, (x, y))
    pygame.display.update()
    clock.tick(FPS)



pygame.quit()
