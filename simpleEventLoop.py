import sys, pygame
pygame.init()

size = width,height = 800,600
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        #handle closing the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #show key presses
        if event.type == pygame.KEYDOWN:
            print pygame.key.name(event.key)

            
