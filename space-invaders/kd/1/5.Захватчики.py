import pygame

from random import randint, uniform



# CONSTANTS
WIDTH  = 500
HEIGHT = 500
FPS    = 60

SHIP_SPEED   = 5
BULLET_SPEED = 10
ENEMY_SPEED  = 2

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

# bullets
bullet_img = pygame.image.load('bullet.png')
wb, hb     = 2, 5
bullets    = []

# enemies
enemy_img  = pygame.image.load('invaderinv.png')
we, he     = 100, 50
enemies    = []
next_enemy = randint(60, 90)



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
            elif event.key == pygame.K_SPACE:
                bullets.append(
                    pygame.Rect(x + w/2 + 3, y, wb, hb)
                )
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


    # bullets
    for bul in bullets:
        bul.top -= BULLET_SPEED
        if bul.bottom < 0:
            bullets.remove(bul)


    # enemies
    next_enemy -= 1
    if next_enemy <= 0:
        next_enemy += randint(60, 90)
        enemies.append(pygame.Rect(
            randint(0, WIDTH-we), -he,
            we, he
        ))
        
    for enemy in enemies:
        enemy.top += ENEMY_SPEED
        if enemy.top > HEIGHT:
            enemies.remove(enemy)


    # drawing
    screen.fill(BLACK)

    for enemy in enemies:
        screen.blit(enemy_img, (enemy.left, enemy.top))
    for bul in bullets:
        screen.blit(bullet_img, (bul.left, bul.top))
    screen.blit(ship_img, (x, y))

    pygame.display.update()
    clock.tick(FPS)



pygame.quit()
