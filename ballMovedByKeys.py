import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

pygame.key.set_repeat(10, 10) #delay before first repeat in ms and then how often in ms 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #handle movement using key state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballrect = ballrect.move([-5,0])
            if event.key == pygame.K_RIGHT:
                ballrect = ballrect.move([ 5,0])
            if event.key == pygame.K_UP:
                ballrect = ballrect.move([0,-5])
            if event.key == pygame.K_DOWN:
                ballrect = ballrect.move([0, 5])

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
