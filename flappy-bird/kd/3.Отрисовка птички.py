import pygame
import random



#Настройки окна
WIDTH = 500
HEIGHT = 500
FPS = 60

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
bird_img  = pygame.image.load('fpbs1.png')
bird      = bird_img.get_rect()
bird.left = 30
bird.top  = HEIGHT/2

# Шрифты
sc_font = pygame.font.SysFont('comic sans ms', 30)
go_font = pygame.font.SysFont('comic sans ms', 50)
go_text = go_font.render('GAME OVER', 1, WHITE)



running = True
while running:
    screen.fill(SKY)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    screen.blit(bird_img, (bird.left, bird.top))
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
