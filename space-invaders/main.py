#!/usr/bin/python3

import math
import pygame
import copy

from nvxsct import sct
from random import randint, choice, uniform





# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED   = (255, 0,   0)
GREEN = (0,   255, 255)
BLUE  = (0,   0,   255)

WIDTH   = 800
HEIGHT  = 600
FPS     = 60

SHIP_SPEED   = 200
BULLET_SPEED = 400
ENEMY_INTER  = (0.5, 1.5)
ENEMEY_SPEED = 130





# prepare
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# common
last_time = 0 # in secs


# ship
w, h     = 60, 50
x, y     = WIDTH/2 - w/2, HEIGHT/2 + 100
ship     = pygame.Rect(x, y, 60, 50)
ship_img = pygame.image.load('./res/razorinv.png')


# bullet
bullet_img = pygame.image.load('./res/bullet.png')
bulw, bulh = 2, 5
bullets = []


# enemies
enemy_img  = pygame.image.load('./res/invaderinv.png')
enw, enh   = enemy_img.get_size()
enemies    = []
next_enemy = uniform(*ENEMY_INTER)





# main
running = True
while running:
	time       = clock.get_time() / 1000 # in secs
	last_time += time

	# events
	is_shot = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				running = False
			elif event.key == pygame.K_SPACE:
				bullets.append(pygame.Rect(
					ship.left + ship.width / 2 + 3,
					y + bulh + BULLET_SPEED * time,
					bulw, bulh
				))


	# ship move
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_LEFT]:
		x -= SHIP_SPEED * time
	if pressed[pygame.K_RIGHT]:
		x += SHIP_SPEED * time
	if pressed[pygame.K_DOWN]:
		y += SHIP_SPEED * time
	if pressed[pygame.K_UP]:
		y -= SHIP_SPEED * time

	ship.left, ship.top = x, y


	# enemies
	for enemy in enemies:
		enemy.top += ENEMEY_SPEED * time
		if enemy.top > HEIGHT:
			enemies.remove(enemy)
	
	next_enemy -= time
	if next_enemy <= 0:
		next_enemy += uniform(*ENEMY_INTER)
		enemies.append(pygame.Rect(
			randint(0, WIDTH-enw), -enh,
			enw, enh
		))


	# bullets
	for bul in bullets:
		bul.top -= BULLET_SPEED * time
		if bul.top - bul.height < 0:
			bullets.remove(bul)


	# draw
	screen.fill(BLACK)
	for enemy in enemies:
		screen.blit(enemy_img, (enemy.left, enemy.top))
	for bul in bullets:
		screen.blit(bullet_img, (bul.left, bul.top))
	screen.blit(ship_img, (ship.left, ship.top))
	pygame.display.update()

	clock.tick(FPS)


pygame.quit()





# END
