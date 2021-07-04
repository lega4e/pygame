#!/usr/bin/python3

import pygame





# constants
WIDTH  = 500
HEIGHT = 500
FPS = 60

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
RED    = (255, 0,   0)
GREEN  = (0,   255, 0)
BLUE   = (0,   0,   255)
YELLOW = (255, 255, 0)


# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("comic sans ms", 30)
herospeed = 5

but1 = (100, 75,  300, 100)
but2 = (100, 215, 300, 100)
but3 = (100, 350, 300, 100)


def contains(rect, point):
	return (
		point[0] >= rect[0] and point[0] <= rect[0] + rect[2] and
		point[1] >= rect[1] and point[1] <= rect[1] + rect[3]
	)



# main
running = True
gamemode = 'menu'
while running:
	screen.fill(WHITE)
	if gamemode == 'menu':
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if contains(but1, event.pos):
					gamemode = 'play'
				elif contains(but2, event.pos):
					if event.button == 1:
						if herospeed < 10:
							herospeed += 1
					elif event.button == 3:
						if herospeed > 1:
							herospeed -= 1
				elif contains(but3, event.pos):
					running = False

		pygame.draw.rect(screen, GREEN,  but1)
		pygame.draw.rect(screen, YELLOW, but2)
		pygame.draw.rect(screen, RED,    but3)

		text = font.render("Сложность: " + str(herospeed), True, BLACK)
		screen.blit(text, (140, 240))

	elif gamemode == 'play':
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		pass

	pygame.display.update()
	clock.tick(FPS)


pygame.quit()
# END
