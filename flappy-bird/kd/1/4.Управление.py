import pygame
import random



#Настройки окна
WIDTH  = 500
HEIGHT = 500
FPS    = 60

GRAVITY    = 20.0
JUMP_POWER = 6.0

# Цвета
YELLOW = (255, 255, 0)
SKY = (133, 193, 233)
GREEN = (46, 204, 113)
WHITE = (255, 255, 255)

#Инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# Настройки персонажа
total_score = 0
bird_img    = pygame.image.load('fpbs1.png')
bird        = bird_img.get_rect()
bird.left   = 30
bird.top    = HEIGHT/2
bird_yspeed = 0

# Шрифты
sc_font = pygame.font.SysFont('comic sans ms', 30)
go_font = pygame.font.SysFont('comic sans ms', 50)
go_text = go_font.render('GAME OVER', 1, WHITE)



last_time = pygame.time.get_ticks() / 1000
running = True
while running:
    time = pygame.time.get_ticks() / 1000 - last_time
    last_time += time

    screen.fill(SKY)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                bird_yspeed = bird_yspeed * 0.4 - JUMP_POWER

    bird_yspeed += GRAVITY * time
    bird.top += bird_yspeed

    screen.blit(bird_img, (bird.left, bird.top))
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
