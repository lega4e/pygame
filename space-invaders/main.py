#!/usr/bin/python3

import glob
import pygame

from game import Game





# main
pygame.init()
screen = pygame.display.set_mode((glob.WIDTH, glob.HEIGHT))

game = Game(screen)
game.run()

pygame.quit()





# END
