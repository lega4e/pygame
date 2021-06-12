#!/usr/bin/python3

import math
import pygame
import copy

from nvxsct import sct
from random import randint, choice, uniform





# functions
def create_circle():
	return sct(
		pos = (randint(MAXRAD, WIDTH-MAXRAD), randint(MAXRAD, HEIGHT-MAXRAD)),
		r = MINRAD, state = 'grow'
	)

def distance(a, b = (0, 0)):
	return ( (a[0] - b[0])**2 + (a[1] - b[1])**2 ) ** 0.5





# constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED   = (255, 0,   0)
GREEN = (0,   255, 255)
BLUE  = (0,   0,   255)

WIDTH   = 600
HEIGHT  = 400
MINRAD  = 5
MAXRAD  = 30
CHSPEED = 10
FPS     = 30




# prepare
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

circles    = [] # sct(pos, color, r)
circlefreq = 0.5 # in seconds
circletime = 0





# main
running = True
while running:
	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pos = pygame.mouse.get_pos()
				for c in circles:
					if distance(pos, c.pos) < c.r:
						break
				else:
					c = None

				if c:
					circles.remove(c)



	# moving
	time = clock.get_time() / 1000
	newcircles = [ c for c in circles ]
	for c in circles:
		if c.state == 'grow':
			c.r += time * CHSPEED
			if c.r > MAXRAD:
				c.r = 2 * MAXRAD - c.r
				c.state = 'decay'
		else:
			c.r -= time * CHSPEED
			if c.r < MINRAD:
				newcircles.remove(c)
	circles = newcircles

	
	circletime -= time
	if circletime < 0:
		circles.append( create_circle() )
		circletime += circlefreq
	

	# draw
	screen.fill(WHITE)
	for c in circles:
		pygame.draw.circle(screen, BLUE, c.pos, c.r)
	pygame.display.update()

	clock.tick(FPS)


pygame.quit()





# END
