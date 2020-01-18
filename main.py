import pygame
from utils.button import Button

pygame.init()

# Create window

windowWidth = 800
windowHeight = 600

window = pygame.display.set_mode((windowWidth,windowHeight))

# Background Image

backgroundImage = pygame.image.load("assets/images/background/invaders.png")

# ----------------------------------------------------Image,Angle
rotateBackgroundImage = pygame.transform.rotate(backgroundImage,90)

# Scale Background Image --------------------- Image ----------------width------Height

scaleBackgroundImage = pygame.transform.scale(rotateBackgroundImage,(windowWidth,windowHeight))

# Logo
logoImage = pygame.image.load("assets/images/logo/logo.png")
logoImageWidth = int(logoImage.get_width() / 4)
logoImageHeight = int(logoImage.get_height() / 4)

scaleLogoImage = pygame.transform.scale(logoImage,(logoImageWidth,logoImageHeight))


# Sounds

pygame.mixer.music.load("assets/sounds/spaceinvaders.mpeg")

speakerImage = pygame.image.load("assets/images/sound/speaker.png")
muteImage = pygame.image.load("assets/images/sound/mute.png")

speaker = True

# If we don't pass in parameters -1 will just play once

pygame.mixer.music.play(-1)

# RGB COLORS Red Green Blue
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

# Create Buttons
playBtnImage = pygame.image.load("assets/images/btn/playBtn.png")

playBtn = Button(window,playBtnImage,windowWidth / 2 - playBtnImage.get_width() / 2, 375)

# Global var

running = True
sound = Button(window,speakerImage,730,10)

while running:
	window.fill(black)
	window.blit(scaleBackgroundImage,(0,0))
	window.blit(scaleLogoImage,(windowWidth / 2 - logoImageWidth / 2,100))
	playBtn.draw()
	sound.draw()

	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = not running

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			mousePosition = pygame.mouse.get_pos()
			if sound.mouseOver(mousePosition):
				if speaker:
					speaker = not speaker
					
					# Change image volume

					sound.image = muteImage

					# Pause music
					pygame.mixer.music.pause()
				else:
					speaker = True

					sound.image = speakerImage

					pygame.mixer.music.unpause()

	pygame.display.update()

pygame.quit
