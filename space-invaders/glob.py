# 
# author:  nvx
# created: 2021.06.05 13:33:32
# 

import pygame





WIDTH   = 800
HEIGHT  = 600
FPS     = 60

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED   = (255, 0,   0)
GREEN = (0,   255, 255)
BLUE  = (0,   0,   255)


HANDLED_KEYS = [
	pygame.K_LEFT,
	pygame.K_RIGHT,
	pygame.K_UP,
	pygame.K_DOWN,
	pygame.K_SPACE,
]

pressed = { key : False for key in HANDLED_KEYS }






# END
