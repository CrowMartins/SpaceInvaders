class Enemy():
	def __init__(self,window,image,x,y,moveX,moveY):
		self.window = window
		self.image = image
		self.x = x
		self.y = y
		self.moveX = moveX
		self.moveY = moveY

	def draw(self):
		self.window.blit(self.image,(self.x,self.y))

	def move(self):

		#Rulles

		if self.x <= 0:
			self.moveX = 5

			self.y += self.moveY

		elif self.x > 730:
			self.moveX = -5
			self.y += self.moveY

		self.x += self.moveX