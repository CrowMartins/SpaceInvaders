import pygame
from utils.bullet import Bullet
import settings as settings

window = pygame.display.set_mode((settings.windowWidth,settings.windowHeight))


bulletImage = pygame.image.load("assets/images/bullet/bullet.png")
bullet = Bullet(window,bulletImage,372,400)

class Player():
	def __init__(self,window,image,x,y):
		self.window = window
		self.image = image
		self.x = x
		self.y = y
		self.moveX = 0

	def draw(self):
		bullet.draw(self.x + 21,self.y)
		self.window.blit(self.image,(self.x,self.y))

		if bullet.state == "fire":
			bullet.fire(self.x)

	def move(self):

		keyState = pygame.key.get_pressed()

		if keyState[pygame.K_LEFT]:
			self.moveX  = -5

			self.x += self.moveX

		if keyState[pygame.K_RIGHT]:
			self.moveX  = 5

			self.x += self.moveX

	def fire(self):
		if bullet.state == "ready":
			bulletSong = pygame.mixer.Sound("assets/sounds/laser.wav")
			bulletSong.play()
			
			bullet.state = "fire"