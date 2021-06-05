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

GRAVITY         = 20.0
JUMP_POWER      = 5.0
BIRD_SPEED      = 40.0
BIRD_ACC        = 1.0
PIPE_DIS        = 130
PIPE_MIN_HEIGHT = 50
PIPE_WIDTH      = 50
PIPE_SPAN       = 100






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
bird_xspeed = BIRD_SPEED
jump_time   = 0.0



# pipes
class Pipe:
	def __init__(self):
		h1          = randint(
			PIPE_SPAN + PIPE_MIN_HEIGHT,
			HEIGHT - PIPE_MIN_HEIGHT - PIPE_SPAN
		)
		self.x      = float(WIDTH)
		self.up     = pygame.Rect(self.x, 0,            PIPE_WIDTH, h1)
		self.mid    = pygame.Rect(self.x, h1,           10,         PIPE_SPAN)
		self.down   = pygame.Rect(self.x, h1+PIPE_SPAN, PIPE_WIDTH, HEIGHT-h1-PIPE_SPAN)
		self.passed = False
		return

	def update(self, time, bird_xspeed):
		delta = bird_xspeed * time
		self.x          -= delta
		self.up.right   -= delta
		self.mid.right  -= delta
		self.down.right -= delta
		return

pipes    = []
pipe_dis = 0






# main
state = 'running'
while state != 'stop':
	time = clock.get_time() / 1000

	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			state = 'stop'
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_yspeed = bird_yspeed * 0.4 - JUMP_POWER

	# generate pipes
	pipe_dis -= bird_xspeed * time
	if pipe_dis <= 0:
		pipe_dis += PIPE_DIS
		pipes.append(Pipe())

	# update
	if state == 'running':
		bird_xspeed  += BIRD_ACC * time
		bird_yspeed  += GRAVITY  * time
		bird.top     += bird_yspeed
		bird_counter += 1
		rbird_img  = pygame.transform.rotate(
			bird_imgs[bird_counter % len(bird_imgs)], 
			math.atan( -bird_yspeed / bird_xspeed ) *
				180 / math.pi * 1.2 + 7.5
		)

		if bird.top > HEIGHT or bird.bottom < 0:
			state = 'game over'

		for pipe in pipes:
			pipe.update(time, bird_xspeed)
			if pipe.x < 0:
				pipes.remove(pipe)
			elif bird.colliderect(pipe.up) or bird.colliderect(pipe.down):
				state = 'game over'
			elif not pipe.passed and bird.colliderect(pipe.mid):
				pipe.passed  = True
				total_score += 1


	# draw
	screen.fill(SKY)

	if state == 'running':
		for pipe in pipes:
			pygame.draw.rect(screen, GREEN, pipe.up)
			pygame.draw.rect(screen, GREEN, pipe.down)
		screen.blit(rbird_img, (bird.left, bird.top))
		screen.blit(font_sc.render('Score: %i' % total_score, True, BLACK), (10, 10))
	elif state == 'game over':
		screen.blit(text_go, (text_go_x, text_go_y))
	elif state != 'stop':
		raise Exception('Unknown state')

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()





# END
