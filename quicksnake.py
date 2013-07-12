import pygame
from pygame.locals import *
from random import randint
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 300), 0, 32)
screenW, screenH = screen.get_size()  # store size values for later

# init for the game
def init():
	clock = pygame.time.Clock()

	direction = 2  # 1, 2, 3, 4 -> left, right, up, down, we'll start with left

	gameFont = pygame.font.SysFont("Trebuchet MS", 25)
	gameFontSml = pygame.font.SysFont("Trebuchet MS", 20)
	gamePsdTxt = gameFontSml.render("Paused", 1, (100, 100, 100))
	gameOvrTxt = gameFont.render("Game Over", 1, (50, 50, 50))

	head = pygame.Rect(screenW/2 - 60, screenH/2, 10, 10)
	body = []
	for i in range(1, 6):
		body.append(pygame.Rect(screenW/2 - 60 - (10 * i), screenH/2, 10, 10))

	randX, randY = randint(10, screenW - 10), randint(10, screenH - 10)
	apple = pygame.Rect(randX - randX % 10, randY - randY % 10, 10, 10)

	gamePaused = False
	gameRunning = True
	updateCount = 0

# handles key events
def handle_events():
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
			elif event.key == K_SPACE:
				gamePaused = not gamePaused
			#elif event.key == K_r:

			elif event.key == K_a:  # left
				if head.x == body[0].x:  # don't allow a reversal of direction
					direction = 1
			elif event.key == K_d:  # right
				if head.x == body[0].x:  # don't allow a reversal of direction
					direction = 2
			elif event.key == K_w:  # up
				if head.y == body[0].y:  # don't allow a reversal of direction
					direction = 3
			elif event.key == K_s:  # down
				if head.y == body[0].y:  # don't allow a reversal of direction
					direction = 4

# handles general screen updates
def update():
	# handle game pausing on space bar
	if gamePaused and gameRunning:
		screen.blit(gamePsdTxt, (screenW/2 - gamePsdTxt.get_width()/2, 20))
	else:
		# check for a collision with the apple, in which case we extend the snake
		if head.colliderect(apple):
			body += [pygame.Rect(head.x, head.y, 0, 0)]
			randX, randY = randint(10, screenW - 10), randint(10, screenH - 10)
			apple = pygame.Rect(randX - randX % 10, randY - randY % 10, 10, 10)

		# check for a collision between the head and any one of the body parts, in which case we end the game
		for bodyPart in body:
			if head.colliderect(bodyPart):
				gameRunning = False

		# check if the snake goes outside the window, in which case we end the game
		if head.x < 0 or head.x > screenW - 10 or head.y < 0 or head.y > screenH - 10:
			gameRunning = False

		# update the body for the next frame
		body = [pygame.Rect(head.x, head.y, 10, 10)] + body[:-1]

		# handle movement
		if direction == 1:
			head.x -= 10
		elif direction == 2:
			head.x += 10
		elif direction == 3:
			head.y -= 10
		elif direction == 4:
			head.y += 10

	clock.tick(15)

# handles screen drawing
def draw():
	screen.fill((150, 150, 150))

	if gameRunning:
		for bodyPart in body:
			pygame.draw.rect(screen, (50, 50, 50), bodyPart)

		pygame.draw.rect(screen, (181, 29, 29), apple)
	else:
		screen.blit(gameOvrTxt, (screenW/2 - gameOvrTxt.get_width()/2, screenH/2 - gameOvrTxt.get_height()/2 - 10))

	pygame.display.flip()

# main function to run the program
def main():
	init()
	while True:
		handle_events()  # first get any key events
		update()  # then update the next frame
		draw()  # then put everything on the screen

main()