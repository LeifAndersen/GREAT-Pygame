import pygame
from pygame.locals import *
from random import randint, uniform
from sys import exit
import time

# Local Imports
from bullet import *
from enemy import *
from HUD import *
from ship import *


def handle_events():
	global character, characterShots

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				exit()
			if event.key == K_w or event.key == K_UP:
				character.vy = -2.5
			if event.key == K_a or event.key == K_LEFT:
				character.vx = -2.5
			if event.key == K_s or event.key == K_DOWN:
				character.vy = 2.5
			if event.key == K_d or event.key == K_RIGHT:
				character.vx = 2.5
			if event.key == K_SPACE:
				characterShots.append(character.createBullet())

		if event.type == KEYUP:
			if event.key == K_w or event.key == K_UP:
				character.vy = 0
			if event.key == K_a or event.key == K_LEFT:
				character.vx = 0
			if event.key == K_s or event.key == K_DOWN:
				character.vy = 0
			if event.key == K_d or event.key == K_RIGHT:
				character.vx = 0


def update():
	global character, characterShots, enemies, enemyShots, gameRunning, hud, screenW
	global back1Y, back2Y, back3Y, lastShipGenTime

	if int(round(time.time() * 1000)) - lastShipGenTime > 3000:
		shipType = randint(0, 3)
		speed = uniform(1.5, 3)
		vy = uniform(.10, .25)
		y = randint(5, 100)

		if shipType == 0:
			for i in range(1, randint(4, 8)):
				enemies.append(Enemy(i * -100, y, speed, vy, 15, "imgs/bgspeedship.png", 1))
		elif shipType == 1:
			for i in range(1, randint(2, 4)):
				enemies.append(Enemy(i * -100, y,  speed, vy, 30, "imgs/heavyfreighter.png", 2))
		elif shipType == 2:
			for i in range(1, randint(4, 8)):
				enemies.append(Enemy((i * 100) + screenW, y, -speed, vy, 15, "imgs/bgspeedship.png", 1))
		elif shipType == 3:
			for i in range(1, randint(2, 4)):
				enemies.append(Enemy(i * -100, y,  -speed, vy, 30, "imgs/heavyfreighter.png", 2))

		lastShipGenTime = int(round(time.time() * 1000))

	back1Y += 2
	back2Y += 2
	back3Y += 2
	if back1Y > 600:
		back1Y = -600
	if back2Y > 600:
		back2Y = -600
	if back3Y > 600:
		back3Y = -600

	for bullet in characterShots:
		bullet.update()
		if bullet.boundingRect.y < 27 - bullet.sprite.get_size()[1]:
			characterShots.remove(bullet)

	for bullet in enemyShots:
		bullet.update()
		if bullet.boundingRect.y > screenH:
			enemyShots.remove(bullet)

	for enemy in enemies:
		if enemy.update():
			enemyShots.append(enemy.createBullet())

	character.update()

	# check collisions
	for enemy in enemies:
		for bullet in characterShots:
			if enemy.isColliding(bullet.mask, bullet.boundingRect):
				hud.score += 5
				characterShots.remove(bullet)
				enemy.health -= bullet.damage
				if enemy.health == 0:
					enemies.remove(enemy)
					hud.score += 10

		if enemy.isColliding(character.mask, character.rect):
			enemies.remove(enemy)
			hud.score -= 10
			if character.shield > 0:
				character.shield -= 10
			else:
				character.health -= 10


	for bullet in enemyShots:
		if character.isColliding(bullet.mask, bullet.boundingRect):
			enemyShots.remove(bullet)
			if character.shield > 0:
				character.shield -= bullet.damage
			else:
				character.health -= bullet.damage

	if character.health <= 0:
		enemies = []
		enemyShots = []
		characterShots = []

		character.destroyed = True

		character.lives -= 1
		character.health = 100
		character.shield = 100

		if character.lives == 0:
			pygame.quit()
			exit()

	hud.shipLives = character.lives
	hud.shipShield = character.shield
	hud.shipHealth = character.health

def draw():
	global character, characterShots, enemyShots, gameRunning, hud, screen
	global backgroundImg, back1Y, back2Y, back3Y
	screen.fill((0, 0, 0))

	screen.blit(backgroundImg, (0, back1Y))
	screen.blit(backgroundImg, (0, back2Y))
	screen.blit(backgroundImg, (0, back3Y))

	for bullet in characterShots:
		bullet.draw(screen)

	for bullet in enemyShots:
		bullet.draw(screen)

	for enemy in enemies:
		enemy.draw(screen)

	character.draw(screen)

	hud.draw(screen)

	pygame.display.flip()


def main():
	global character, characterShots, enemies, enemyShots, gameRunning, hud, screen, screenH, screenW
	global backgroundImg, back1Y, back2Y, back3Y, lastShipGenTime

	pygame.init()
	screenW, screenH = 800, 600
	screen = pygame.display.set_mode((screenW, screenH), 0, 32)

	hud = HUD(0, 0, screenW, 27)

	backgroundImg = pygame.image.load("imgs/starback.png")
	back1Y, back2Y, back3Y = 0, 400, -400

	character = Ship(screenW/2, screenH/2 + 200, screenW, screenH, "imgs/bgbattleship.png")
	characterShots = []

	enemies = []
	enemyShots = []

	#lastShipGenTime = int(round(time.time() * 1000))
	lastShipGenTime = 0

	gameRunning = True
	while gameRunning:
		handle_events()
		update()
		draw()

if __name__ == "__main__":
	main()
