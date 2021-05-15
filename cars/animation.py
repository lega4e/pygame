import pygame

from math import exp




# Functions
def linear(factor):
	return factor

def sigmoid(factor):
	return 1 / (1 + exp(-10*(factor - 0.5)))

class Moving:
	def __init__(self, rect, dur, fun=linear):
		self.rect = rect
		self.dur  = dur
		self.pas  = 0
		self.fun  = fun
		return

	def reset(self):
		self.pas = 0
		return

	def isRun(self):
		return abs(self.dur - self.pas) > 0.000001

	def proc(self):
		return self.pas / self.dur

	def __call__(self, time):
		newpas = min(self.dur, self.pas + time)
		delta = self.fun(newpas / self.dur) - self.fun(self.pas / self.dur)
		self.pas = newpas
		x = delta * (self.rect[2] - self.rect[0])
		y = delta * (self.rect[3] - self.rect[1])
		return x, y





# END
