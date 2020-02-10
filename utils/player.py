import pygame
import settings as settings


window = pygame.display.set_mode((settings.windowWidth,settings.windowHeight))


class Player():
	def __init__(self,window,image,x,y):
		self.window = window
		self.image = image
		self.x = x
		self.y = y
		self.moveX = 0

	def draw(self):
		self.window.blit(self.image,(self.x,self.y))

	def move(self):

		keyState = pygame.key.get_pressed()

		if keyState[pygame.K_LEFT]:

			self.moveX = -5
			self.x += self.moveX

		if keyState[pygame.K_RIGHT]:
			self.moveX  = 5
			self.x += self.moveX

		if self.x <= 0:
			self.x = 0
		elif self.x >= 760:
			self.x = 760


		


