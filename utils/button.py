import pygame

class Button():
	def __init__(self,window,image,x,y):
		self.window = window
		self.image = image
		self.x = x
		self.y = y
		self.width = image.get_width()
		self.height = image.get_height()

	def draw(self):
		self.window.blit(self.image,(self.x,self.y))

	def mouseOver(self,mousePosition):
		if mousePosition[0] > self.x and mousePosition[0] < self.x + self.width:
			if mousePosition[1] > self.y and mousePosition[1] < self.y + self.height:
				return True
		return False