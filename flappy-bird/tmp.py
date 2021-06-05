#!/usr/bin/python3

import math
import pygame

from random import randint





# constants
WIDTH  = 500
HEIGHT = 500
FPS    = 60

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GREEN  = (46,  204, 113)
YELLOW = (255, 255, 0)
SKY    = (133, 193, 233)

GRAVITY    = 0.02
JUMP_DUR   = 5.0
JUMP_POWER = 7.0
BIRD_SPEED = 10.0





# prepare
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.time.Clock()

total_score = 0



# font
font_go   = pygame.font.SysFont("comic sans ms", 40)
font_sc   = pygame.font.SysFont("comic sans ms", 16)

text_go   = font_go.render("Game Over", True, BLACK)
text_go_x = WIDTH/2  - text_go.get_size()[0]/2
text_go_y = HEIGHT/2 - text_go.get_size()[1]/2



# bird
bird_imgs = [
	pygame.image.load('bird1.png'),
	pygame.image.load('bird2.png'),
	pygame.image.load('bird3.png'),
	None
]
bird_imgs[3] = bird_imgs[1]
bird_counter = 0

bird        = bird_imgs[0].get_rect()
bird.left   = 100
bird.top    = HEIGHT // 2
bird_yspeed = 0.0
jump_time   = 0.0





# main
state = 'running'
last_time = pygame.time.get_ticks() / 1000
while state != 'stop':
	time = pygame.time.get_ticks() / 1000 - last_time
	last_time += time
	print(time)
	
	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			state = 'stop'
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_yspeed = bird_yspeed * 0.4 - JUMP_POWER

	# update
	if state == 'running':
		bird_yspeed  += GRAVITY * time
		bird.top     += bird_yspeed
		bird_counter += 1
		rbird_img  = pygame.transform.rotate(
			bird_imgs[bird_counter % len(bird_imgs)], 
			math.atan( - bird_yspeed / BIRD_SPEED ) *
				180 / math.pi / 2.0 + 7.5
		)

		if bird.top > HEIGHT or bird.bottom < 0:
			state = 'game over'

	# draw
	screen.fill(SKY)

	if state == 'running':
		screen.blit(rbird_img, (bird.left, bird.top))
	elif state == 'game over':
		screen.blit(text_go, (text_go_x, text_go_y))
	elif state != 'stop':
		raise Exception('Unknown state')

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()





# END

