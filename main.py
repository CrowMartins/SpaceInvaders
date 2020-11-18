import pygame
import settings as settings
from screens.mainScreen import Main
from screens.battleScreen import Battle



#Icon and Caption

pygame.display.set_caption('Space Invaders')

icon = pygame.image.load("assets/images/spaces/spaceship.png")
pygame.display.set_icon(pygame.transform.scale(icon,(32,32)))


#Sounds

pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/spaceinvaders.mpeg")

# If we don't pass in parameters -1 will just play once

pygame.mixer.music.play(-1)

screens = {
	'Main':Main(),
	'Battle':Battle()

}

screenName = 'Battle'

screen = screens[screenName]

clock = pygame.time.Clock()

while screen.running:
	screenName = screen.navigate()
	screen.draw()
	screen = screens[screenName]
	clock.tick(60)
	pygame.display.flip()

pygame.quit
