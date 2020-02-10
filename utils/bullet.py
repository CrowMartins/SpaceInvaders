import pygame

class Bullet():
	def __init__(self,window,image,x,y):
		self.window = window
		self.image = image
		self.x = x
		self.y = y
		self.moveY = 10
		self.state = 'ready'

	def draw(self,x,y):
		self.window.blit(self.image,(x,y))

	def fire(self,x):
		playerX = x + 21
		self.x = playerX

		#Rulles

		if self.y <= 0:
			self.y = 400
			self.state = "ready"

		if self.state == "fire":
			self.draw(playerX,self.y)
			self.y -= self.moveY