# 
# author:  nvx
# created: 2021.06.05 13:28:05
# 

import glob
import pygame





class ShipSets:
	ship_speed    = 200.0 # px/sec
	fire_speed    = 3.0   # shot/sec
	bullet_speed  = 400.0 # px/sec
	bullet_width  = 2
	bullet_height = 5
	bullet_color  = glob.WHITE


class Ship:
	x     = 0.0
	y     = 0.0
	img   = None
	rect  = pygame.Rect(0, 0, 0, 0)
	nshot = 0.0 # time to next shot
	buls  = []  # bullet rects
	sets  = ShipSets()


	def __init__(self, rect: pygame.Rect, img):
		self.x    = float(rect.left)
		self.y    = float(rect.top)
		self.rect = rect
		self.img  = img
		return


	def update(self, time):
		# shooting
		self.nshot = max(0.0, self.nshot - time)
		if glob.pressed[pygame.K_SPACE] and self.nshot <= 0.0:
			self.nshot += 1.0 / self.sets.fire_speed
			self.buls.append(pygame.Rect(
				self.rect.left + self.rect.width / 2.0,
				self.y + self.sets.bullet_height,
				self.sets.bullet_width,
				self.sets.bullet_height
			))


		# movement
		dir = [0.0, 0.0]
		if glob.pressed[pygame.K_LEFT]:
			dir[0] -= 1.0
		if glob.pressed[pygame.K_RIGHT]:
			dir[0] += 1.0
		if glob.pressed[pygame.K_DOWN]:
			dir[1] += 1.0
		if glob.pressed[pygame.K_UP]:
			dir[1] -= 1.0

		length = (dir[0]**2 + dir[1]**2)**0.5
		if length != 0:
			dir = dir[0] / length, dir[1] / length
			self.x += dir[0] * self.sets.ship_speed * time
			self.y += dir[1] * self.sets.ship_speed * time
			self.rect.left = self.x
			self.rect.top  = self.y


		# bullets
		for bul in self.buls:
			bul.top -= self.sets.bullet_speed * time
			if bul.bottom < 0:
				self.buls.remove(bul)

		return


	def draw_bullets(self, surface):
		for bul in self.buls[::-1]:
			pygame.draw.rect(surface, self.sets.bullet_color, bul)
		return
	

	def draw_ship(self, surface):
		surface.blit(self.img, (self.x, self.y))
		return


	def draw(self, surface):
		self.draw_bullets(surface)
		self.draw_ship(surface)
		return





# END
