# 
# author:  nvx
# created: 2021.06.05 13:27:35
# 

import glob
import pygame

from ship    import Ship
from invader import Invader, InvaderHive





class Game:
	def __init__(self, surface):
		# ship
		self.surface = surface
		self.ship_img = pygame.image.load('./res/razorinv.png')
		w, h = self.ship_img.get_size()
		self.ship = Ship(
			pygame.Rect(glob.WIDTH/2 - w/2, glob.HEIGHT/2 + 100, w, h),
			self.ship_img
		)

		# invaders
		self.invhive  = InvaderHive()
		self.invaders = []

		return


	def run(self):
		clock = pygame.time.Clock()
		state = 'running' # 'running', 'game over'
		while True:
			time = clock.get_time() / 1000 # in secs

			# events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return
					elif event.key in glob.HANDLED_KEYS:
						glob.pressed[event.key] = True
				elif event.type == pygame.KEYUP:
					if event.key in glob.HANDLED_KEYS:
						glob.pressed[event.key] = False

			if state == 'running':
				self.game_iteration(time)
			elif state == 'game over':
				self.go_iteartion(time)
			else:
				raise Exception("Unknown state of game")

			clock.tick(glob.FPS)

		return


	def game_iteration(self, time):

		# updates
		self.ship.update(time)
		for invader in self.invaders:
			invader.update(time)

		# enemy
		inv = self.invhive.spawn(time)
		if inv is not None:
			self.invaders.append(inv)

		# draw
		self.surface.fill(glob.BLACK)
		self.ship.draw(self.surface)
		for invader in self.invaders[::-1]:
			invader.draw(self.surface)
			if invader.rect.top > glob.HEIGHT:
				self.invaders.remove(invader)
		pygame.display.update()

		return


	def go_iteration(self, time):
		return





# END
