import math, pygame
from resources import *

class Bullet(object):
	def __init__(self, x, y, vy, damage, spritePath, resizeRatio=0):
		self.vy = vy
		self.damage = damage
		self.sprite = pygame.image.load(spritePath)
		self.sprite = Resources.convertToAlpha(self.sprite, (0, 0, 0))

		if resizeRatio != 0:
			self.sprite = pygame.transform.scale(self.sprite,
												(math.floor(self.sprite.get_size()[0] * resizeRatio),
												math.floor(self.sprite.get_size()[1] * resizeRatio)))

		self.boundingRect = self.sprite.get_rect()
		self.boundingRect.x = x - self.sprite.get_size()[0]/2
		self.boundingRect.y = y

		self.mask = pygame.mask.from_surface(self.sprite)

	def update(self):
		self.boundingRect.y += self.vy

	def draw(self, surface):
		surface.blit(self.sprite, self.boundingRect)