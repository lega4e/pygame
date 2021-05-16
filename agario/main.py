#!/usr/bin/python3

import math
import pygame
import copy

from nvxsct import sct
from random import randint, choice, uniform





# functions
def create_food():
	return sct(
		pos = (randint(0, WIDTH), randint(0, HEIGHT)),
		color = choice(list(pygame.color.THECOLORS.values())),
		r = uniform(6, 12)
	)

def distance(a, b = (0, 0)):
	return ( (a[0] - b[0])**2 + (a[1] - b[1])**2 ) ** 0.5





# constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED   = (255, 0,   0)
GREEN = (0,   255, 255)
BLUE  = (0,   0,   255)

WIDTH  = 600
HEIGHT = 400
FPS    = 60




# prepare
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

speed = 200
x = WIDTH / 2
y = HEIGHT / 2
r = 30

food = [] # sct(pos, color, r)
foodfreq = 0.3 # in seconds
foodtime = 0





# main
running = True
while running:
	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key in [ pygame.K_c, pygame.K_ESCAPE ]:
				running = False


	# moving
	time = clock.get_time() / 1000

	mpos = pygame.mouse.get_pos()
	norm = (mpos[0] - x, mpos[1] - y)
	d = distance(norm)
	norm = norm[0] / d, norm[1] / d

	x += norm[0] * speed * time
	y += norm[1] * speed * time


	# intersects
	newfood = [ f for f in food ]
	for f in food:
		d = distance((x, y), f.pos)
		if d < r + f.r / 2:
			r = ( r**2 + f.r**2 ) ** 0.5
			newfood.remove(f)

	food = newfood

	
	foodtime -= time
	if foodtime < 0:
		food.append( create_food() )
		foodtime += foodfreq
	

	# draw
	screen.fill(WHITE)
	for f in food:
		pygame.draw.circle(screen, f.color, f.pos, f.r)
	pygame.draw.circle(screen, RED, (x, y), r)
	pygame.display.update()

	clock.tick(FPS)


pygame.quit()





# END
