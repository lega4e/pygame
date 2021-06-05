# 
# author:  nvx
# created: 2021.06.05 13:28:40
# 

import glob
import pygame

from random import randint, uniform





class InvaderSets:
	speed = 300.0



class Invader:
	x    = 0.0
	y    = 0.0
	img  = None
	rect = pygame.Rect(0, 0, 0, 0)
	sets = InvaderSets()

	def __init__(self, rect, img):
		self.x    = float(rect.left)
		self.y    = float(rect.top)
		self.rect = rect
		self.img  = img

	def update(self, time):
		self.y += self.sets.speed * time
		return
	
	def draw(self, surface):
		surface.blit(self.img, (self.x, self.y))
		return



class InvaderHive:
	img  = pygame.image.load('./res/invaderinv.png')
	freq = (0.25, 1.25)
	sets = InvaderSets()
	nxt  = 0.0

	def __init__(self):
		pass

	def spawn(self, time):
		self.nxt -= time
		if self.nxt <= 0.0:
			self.nxt += uniform(*self.freq)
			imgrect   = self.img.get_rect()

			inv       = Invader(pygame.Rect(
				randint(0, glob.WIDTH - imgrect.width),
				-imgrect.height, imgrect.width, imgrect.height
			), self.img)
			inv.sets  = self.sets
			return inv
		return None





# END
