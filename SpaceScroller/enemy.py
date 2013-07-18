import pygame
from random import randint

from bullet import *

class Enemy(object):
	def __init__(self, x, y, vx, vy, health, spritePath, shipType):
		self.x, self.y = x, y
		self.vx, self.vy = vx, vy
		self.sprite = pygame.image.load(spritePath)
		self.type = shipType

		self.health = health

		self.mask = pygame.mask.from_surface(self.sprite)
		self.rect = self.sprite.get_rect()

		self.bulletCounter = 0
		self.bulletFrequency = randint(50, 110)

		self.shots = []  # list to store all of the shots the sprite has created

	def createBullet(self):
		if self.type == 1:
			return Bullet(self.x + self.sprite.get_size()[0]/2,
							self.y + self.sprite.get_size()[1]/2, 3, 5, "imgs/laserRed.png", .15)
		elif self.type == 2:
			return Bullet(self.x + self.sprite.get_size()[0]/2,
							self.y + self.sprite.get_size()[1]/2, 5, 10, "imgs/laserOrng.jpg", .20)

	def isColliding(self, other, otherRect):
		if self.mask.overlap(other, (otherRect.left - self.rect.left, otherRect.top - self.rect.top)):
			return True
		else:
			return False

	def update(self):
		self.bulletCounter += 1
		self.x += self.vx
		self.y += self.vy

		self.rect.x = self.x
		self.rect.y = self.y

		if self.bulletCounter == self.bulletFrequency:
			self.bulletFrequency = randint(50, 110)
			self.bulletCounter = 0
			return True

		return False

	def draw(self, surface):
		surface.blit(self.sprite, self.rect)