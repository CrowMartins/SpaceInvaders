import pygame
import settings as settings
from utils.button import Button


window = pygame.display.set_mode((settings.windowWidth,settings.windowHeight))


# Background Image

backgroundImage = pygame.image.load("assets/images/background/invaders.png")

# ----------------------------------------------------Image,Angle
rotateBackgroundImage = pygame.transform.rotate(backgroundImage,90)

# Scale Background Image --------------------- Image ----------------width------Height

scaleBackgroundImage = pygame.transform.scale(rotateBackgroundImage,(settings.windowWidth,settings.windowHeight))


# Logo
logoImage = pygame.image.load("assets/images/logo/logo.png")
logoImageWidth = int(logoImage.get_width() / 4)
logoImageHeight = int(logoImage.get_height() / 4)

scaleLogoImage = pygame.transform.scale(logoImage,(logoImageWidth,logoImageHeight))


#Create Buttons

playBtnImage = pygame.image.load("assets/images/btn/playBtn.png")

playBtn = Button(window,playBtnImage,settings.windowWidth / 2 - playBtnImage.get_width() / 2, 375)


speakerImage = pygame.image.load("assets/images/sound/speaker.png")
scaleImageSpeaker = pygame.transform.scale(speakerImage,(32,32))
sound = Button(window,scaleImageSpeaker,730,10)

muteImage = pygame.image.load("assets/images/sound/mute.png")

class Main():
	def __init__(self):
		self.window = window
		self.image = scaleBackgroundImage
		self.x = 0
		self.y = 0
		self.running = True
		self.speaker = True
		self.navigateTo = 'Main'

	def navigate(self):
		return self.navigateTo

	def draw(self):
		self.navigateTo = 'Main'
		self.window.blit(self.image,(self.x,self.y))
		window.blit(scaleLogoImage,(settings.windowWidth / 2 - logoImageWidth / 2,100))
		playBtn.draw()
		sound.draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = not self.running

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mousePosition = pygame.mouse.get_pos()

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
				if playBtn.mouseOver(mousePosition):
					self.navigateTo = "Battle"
