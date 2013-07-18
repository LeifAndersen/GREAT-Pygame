import math, pygame
from resources import *


class HUD(object):
	def __init__(self, x, y, w, h):
		self.x, self.y = x, y
		self.width, self.height = w, h

		self.shipHealth = 100
		self.shipShield = 100

		self.score = 0
		self.scoreFont = pygame.font.SysFont("Droid Sans", 22)

		self.healthMultiplier = self.width/self.shipHealth
		self.healthImg = pygame.image.load("imgs/health.png")
		self.shipHealthBar = pygame.Rect(0, 0, self.shipHealth * 2, self.height)

		self.shipLives = 3
		self.lifeImg = pygame.image.load("imgs/bgbattleship.png")
		self.lifeImg = pygame.transform.smoothscale(self.lifeImg,
												(math.floor(self.lifeImg.get_size()[0] * .22),
												math.floor(self.lifeImg.get_size()[1] * .22)))
		#self.lifeImg = Resources.spriteSheetToArray(self.lifeImg, 1, 2, (0, 0, 0))

	def draw(self, surface):
		pygame.draw.rect(surface, (50, 50, 50), pygame.Rect(self.x, self.y, self.width, self.height))

		for i in range(0, math.floor(self.shipHealth * self.healthMultiplier)):
			surface.blit(self.healthImg, (i, 0))

		self.shieldSurface = pygame.Surface((self.width, self.height))  # the size of your rect
		self.shieldSurface.set_alpha(128)                # alpha level
		pygame.draw.rect(self.shieldSurface, (0, 0, 200), pygame.Rect(self.x, self.y,
													math.floor(self.shipShield * self.healthMultiplier),
													self.height))
		surface.blit(self.shieldSurface, (0,0))    # (0,0) are the top-left coordinates

		for i in range(0, self.shipLives):
			surface.blit(self.lifeImg, (self.width - ((i + 1) * 30), 2))

		scoreTxt = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
		surface.blit(scoreTxt, (5, 1))
