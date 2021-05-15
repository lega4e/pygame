#!/usr/bin/python3

import pygame

from random    import choice
from animation import Moving, sigmoid





# constants
WIDTH  = int(300*1.9)
HEIGHT = int(500*1.9)
FPS    = 60

WHITE      = '#ffffff'
LIGHT_GRAY = '#bbbbbb'
RED        = '#8B3F3F'
GREEN      = '#46802A'
BLACK      = '#000000'

ENEMY_FREQ_BEG   = 0.5
ENEMY_FREQ_END   = 0.25
ENEMY_FREQ_DELTA = 0.01

ENEMY_WIDTH  = None
ENEMY_HEIGHT = None

CAR_WIDTH  = None
CAR_HEIGHT = None





# init
pygame.init()
screen     = pygame.display.set_mode((WIDTH, HEIGHT))
clock      = pygame.time.Clock()
score_font = pygame.font.SysFont('Arial', 20)
end_font   = pygame.font.SysFont('Arial', 28)





# objects
moving = Moving(None, 0.2, sigmoid)

car_img    = pygame.image.load('./blue-car-forward.png').convert()
CAR_WIDTH  = car_img.get_size()[0]
CAR_HEIGHT = car_img.get_size()[1]

car_positions = [
	1/14*WIDTH  - CAR_WIDTH/2,
	4/14*WIDTH  - CAR_WIDTH/2,
	7/14*WIDTH  - CAR_WIDTH/2,
	10/14*WIDTH - CAR_WIDTH/2,
	13/14*WIDTH - CAR_WIDTH/2,
]
carpos = len(car_positions) // 2

car = pygame.Rect(
	car_positions[carpos],
	HEIGHT  - CAR_HEIGHT - 10,
	CAR_WIDTH,
	CAR_HEIGHT
)



enemies          = []
enemy_freq       = ENEMY_FREQ_BEG
enemy_timer      = 0
overtaken        = 0

enemy_img    = pygame.image.load('./pink-car-backward.png').convert()
ENEMY_WIDTH  = enemy_img.get_size()[0]
ENEMY_HEIGHT = enemy_img.get_size()[1]

enemy_positions = [
	1/14*WIDTH  - ENEMY_WIDTH/2,
	4/14*WIDTH  - ENEMY_WIDTH/2,
	7/14*WIDTH  - ENEMY_WIDTH/2,
	10/14*WIDTH - ENEMY_WIDTH/2,
	13/14*WIDTH - ENEMY_WIDTH/2,
]





# functions
def reset():
	global carpos,  car
	global enemies, enemy_freq, enemy_timer, overtaken

	carpos = 2
	car.left = car_positions[carpos]

	enemies          = []
	enemy_freq       = ENEMY_FREQ_BEG
	enemy_timer      = 0
	overtaken        = 0





# main
state   = 'stop'
carst   = 'stay'
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key in [ pygame.K_c, pygame.K_ESCAPE ]:
				running = False
			elif event.key == pygame.K_RIGHT:
				if (carst == 'stay' or moving.proc() > 0.7) and carpos < len(car_positions)-1:
					carpos += 1
					moving.reset()
					moving.rect = (car.left, car.top, car_positions[carpos], car.top)
					carst = 'right'
			elif event.key == pygame.K_LEFT:
				if (carst == 'stay' or moving.proc() > 0.7) and carpos > 0:
					carpos -= 1
					moving.reset()
					moving.rect = (car.left, car.top, car_positions[carpos], car.top)
					carst = 'left'
			elif event.key == pygame.K_SPACE:
				reset()
				if state in ['stop', 'game-over']:
					state = 'run'

	if state == 'run':
		time = clock.get_time() / 1000

		if carst in ['right', 'left']:
			x, y      = moving(time)
			car.left += x
			car.top  += y
			if not moving.isRun:
				carst = 'stay'

		for enemy in enemies:
			if enemy.colliderect(car):
				state = 'game-over'

			enemy.top += 10
			if enemy.top >= HEIGHT:
				enemies.remove(enemy)
				overtaken += 1

		enemy_timer += time
		while enemy_timer >= enemy_freq:
			enemy_timer -= enemy_freq
			enemies.append( pygame.Rect(
				choice(enemy_positions), -CAR_HEIGHT,
				CAR_WIDTH, CAR_HEIGHT
			) )

		enemy_freq = max(ENEMY_FREQ_END, enemy_freq - ENEMY_FREQ_DELTA*time)
		score_text = score_font.render('Score: %i' % overtaken, True, BLACK)
		freq_text  = score_font.render('Freq: %.2f' % enemy_freq, True, BLACK)

	# draw
	screen.fill(LIGHT_GRAY)

	if state == 'run':
		for enemy in enemies:
			screen.blit(enemy_img, (enemy.left, enemy.top))
			#  pygame.draw.rect(screen, RED, enemy)
		screen.blit(car_img, (car.left, car.top))
		#  pygame.draw.rect(screen, GREEN, car)
		screen.blit(score_text, (WIDTH-score_text.get_size()[0]-20, 30))
		screen.blit(freq_text, (20, 30))
	elif state == 'game-over':
		score_text = end_font.render('Game over! Score: %i' % overtaken, True, BLACK)
		start_text = end_font.render('SPACE to start', True, BLACK)
		h = score_text.get_size()[1] + start_text.get_size()[1] + 10
		screen.blit(
			score_text,
			(WIDTH/2 - score_text.get_size()[0]/2,
			 HEIGHT/2 - h/2)
		)
		screen.blit(
			start_text,
			(WIDTH/2 - start_text.get_size()[0]/2,
			 HEIGHT/2 - h/2 + score_text.get_size()[1] + 10)
		)
	elif state == 'stop':
		text = end_font.render('SPACE to start', True, BLACK)
		screen.blit(text, (WIDTH/2 - text.get_size()[0]/2, HEIGHT/2))
	else:
		raise Exception('Unknown state')

	pygame.display.update()
	clock.tick(FPS)

pygame.quit()





# END
