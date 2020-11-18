import pygame
import random
import math

import settings as settings
from utils.button import Button
from utils.player import Player
from utils.player import bullet
from utils.enemy import Enemy
from utils.score import Score

window = pygame.display.set_mode((settings.windowWidth,settings.windowHeight))


# Background Image

backgroundImage = pygame.image.load("assets/images/background/invaders.png")

# ----------------------------------------------------Image,Angle
rotateBackgroundImage = pygame.transform.rotate(backgroundImage,90)

# Scale Background Image --------------------- Image ----------------width------Height

scaleBackgroundImage = pygame.transform.scale(rotateBackgroundImage,(settings.windowWidth,settings.windowHeight))




#Create Buttons


speakerImage = pygame.image.load("assets/images/sound/speaker.png")
scaleImageSpeaker = pygame.transform.scale(speakerImage,(32,32))
sound = Button(window,scaleImageSpeaker,680,10)

muteImage = pygame.image.load("assets/images/sound/mute.png")

#Create Pause Button
pauseButton = pygame.image.load("assets/images/btn/pause.png");
scalePauseButton = pygame.transform.scale(pauseButton,(32,32))
pauseBtn = Button(window,scalePauseButton,720,10)


#Home  Button
homeButton = pygame.image.load("assets/images/btn/home.png");
scaleHomeButton = pygame.transform.scale(homeButton,(32,32))
homeBtn = Button(window,scaleHomeButton,760,10)

#Exit  Button
exitButton = pygame.image.load("assets/images/btn/exit.png");
scaleExitButton = pygame.transform.scale(exitButton,(32,32))
exitBtn = Button(window,scaleExitButton,400,400)


#Create Player
playerImage = pygame.image.load("assets/images/spaces/spaceship.png")
player = Player(window,pygame.transform.scale(playerImage,(64,64)),372,400)


#Create Enemies

enemyCrow = Enemy(window,pygame.image.load("assets/images/enemies/saucer1b.ico"),random.randint(0,730),random.randint(0,200),4,30)
enemyCrowMartins = Enemy(window,pygame.image.load("assets/images/enemies/saucer1b.ico"),random.randint(0,730),random.randint(0,200),4,30)
enemyCrow1 = Enemy(window,pygame.image.load("assets/images/enemies/saucer1b.ico"),random.randint(0,730),random.randint(0,200),4,30)
enemyCrowMartins2 = Enemy(window,pygame.image.load("assets/images/enemies/saucer1b.ico"),random.randint(0,730),random.randint(0,200),4,30)
enemyCrow3 = Enemy(window,pygame.image.load("assets/images/enemies/saucer1b.ico"),random.randint(0,730),random.randint(0,200),4,30)
enemyCrowMartins4 = Enemy(window,pygame.image.load("assets/images/enemies/saucer1b.ico"),random.randint(0,730),random.randint(0,200),4,30)

enemies = [enemyCrow,enemyCrowMartins,enemyCrow1,enemyCrowMartins2,enemyCrow3,enemyCrowMartins4]



# Create Score

score = Score(window,8,8)

class Battle():
	def __init__(self):
		self.window = window
		self.image = scaleBackgroundImage
		self.x = 0
		self.y = 0
		self.running = True
		self.speaker = True
		self.pause = False
		self.navigateTo = 'Battle'

	def navigate(self):
		return self.navigateTo

	def play(self):


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = not self.running

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.fire()

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mousePosition = pygame.mouse.get_pos()


				if homeBtn.mouseOver(mousePosition):
					self.navigateTo = "Main"

				if pauseBtn.mouseOver(mousePosition):
					if self.pause:
						self.pause = not self.pause
					else:
						self.pause = True



				if sound.mouseOver(mousePosition):
					if self.speaker:
						self.speaker = not self.speaker

						# Change image volume

						sound.image = muteImage

						# Pause music
						pygame.mixer.music.pause()
					else:
						self.speaker = True

						sound.image = scaleImageSpeaker

						pygame.mixer.music.unpause()
	def draw(self):
		self.navigateTo = 'Battle'
		self.window.blit(self.image,(self.x,self.y))
		sound.draw()
		player.draw()

		if self.pause == False:
			player.move()
			pygame.mixer.music.unpause()
		else:
			pygame.mixer.music.pause()
			exitBtn.draw()

		score.draw()
		pauseBtn.draw()
		homeBtn.draw()

		for enemy in enemies:
			enemy.draw()

			if self.pause == False:
				enemy.move()

			colision = math.hypot(enemy.x - bullet.x,enemy.y - bullet.y)

			if colision < 27:

				explosion = pygame.mixer.Sound("assets/sounds/explosion.wav")
				explosion.play()

				enemy.x = random.randint(0,730)
				enemy.y = random.randint(0,200)
				bullet.state = "ready"
				bullet.y = 400

				score.value += 1




		self.play()
