import pygame
from bullet import *
from resources import *


class Ship(object):
	def __init__(self, x, y, screenWid, screenHei, spritePath):
		global screenW, screenH
		screenW, screenH = screenWid, screenHei

		spriteImg = pygame.image.load(spritePath)
		spriteImg = pygame.transform.smoothscale(spriteImg, (120, 120))
		self.sprite = spriteImg

		self.mask = pygame.mask.from_surface(self.sprite)
		self.rect = self.sprite.get_rect()

		self.explosion = Resources.spriteSheetToArray(pygame.image.load("imgs/explosion.gif"), 5, 4, (0, 0, 0))
		self.frameCntr = 0

		self.x = x - self.sprite.get_size()[0]/2
		self.y = y - self.sprite.get_size()[1]/2
		self.vx = self.vy = self.ax = self.ay = 0
		self.destroyed = False

		self.health = 100
		self.shield = 100
		self.lives = 3

	def createBullet(self):
		return Bullet(self.x + self.sprite.get_size()[0]/2,
						self.y, -3, 5, "imgs/laserGrn.png", .15)

	def isColliding(self, other, otherRect):
		if self.mask.overlap(other, (otherRect.left - self.rect.left, otherRect.top - self.rect.top)):
			return True
		else:
			return False

	def draw(self, surface):
		if not self.destroyed:
			surface.blit(self.sprite, self.rect)
		else:
			surface.blit(self.explosion[self.frameCntr],
						((self.rect.x + self.rect.width/2) - self.explosion[self.frameCntr].get_size()[0]/2,
						(self.rect.y + self.rect.height/2) - self.explosion[self.frameCntr].get_size()[1]/2))
			self.frameCntr += 1

			if self.frameCntr == len(self.explosion) - 1:
				self.x, self.y = self.rect.x, self.rect.y = screenW/2, screenH/2 + 200
				self.destroyed = False
				self.frameCntr = 0

	def update(self):
		global screenW, screenH

		if not(self.x < 0 or self.x > screenW - self.sprite.get_size()[0]):
			self.x += self.vx
			self.rect.x = self.x
		elif self.x < 0:
			self.x = 0
		elif self.x > screenW - self.sprite.get_size()[0]:
			self.x = screenW - self.sprite.get_size()[0]

		if not(self.y < 27 or self.y > screenH - self.sprite.get_size()[1]):
			self.y += self.vy
			self.rect.y = self.y
		elif self.y < 27:  # not the top of the screen, because we have a HUD
			self.y = 27
		elif self.y > screenH - self.sprite.get_size()[1]:
			self.y = screenH - self.sprite.get_size()[1]