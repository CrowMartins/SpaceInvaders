import pygame

pygame.font.init()

class Score():
	def __init__(self,window,x,y):
		self.window = window
		self.x = x
		self.y = y
		self.value = 0

	def draw(self):
		font = pygame.font.Font('freesansbold.ttf',32)

		score = font.render("Score: " + str(self.value), True, (255,255,255))

		self.window.blit(score,(self.x,self.y))