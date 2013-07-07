import sys, pygame, math
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

#Load the moving object
ball = pygame.image.load("ball.gif")
ballRect = ball.get_rect()
#make a mask for collision detection
ballMask = pygame.mask.from_surface( ball )

#Load a explosionRect
batMaster = pygame.image.load("bat.png")

pygame.key.set_repeat(10, 10) #delay before first repeat in ms and then how often in ms 

# how far the bat is rotated
degrees = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #handle movement using key state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballRect = ballRect.move([-5,0])
            if event.key == pygame.K_RIGHT:
                ballRect = ballRect.move([ 5,0])
            if event.key == pygame.K_UP:
                ballRect = ballRect.move([0,-5])
            if event.key == pygame.K_DOWN:
                ballRect = ballRect.move([0, 5])
            if event.key == pygame.K_SPACE:
                degrees += 5

    #When an object rotates, you need to remake its rect and mask each frame                
    bat = pygame.transform.rotate( batMaster, degrees )
    batRect = bat.get_rect()
    #center the bat. 
    batRect.center = (width/2, height/2)

    #A more complicated version that spins around the end of the bat
    #not really for the first example
    origbatRect = batMaster.get_rect()#this would be done once but I am keeping it together
    batRect.center = (width/2 + (origbatRect.width/2)* math.cos( math.radians( degrees )),
                      height/2 - (origbatRect.width/2)* math.sin( math.radians( degrees )))
     
    #make the mask
    batMask = pygame.mask.from_surface( bat )
    
    # check for overlap with the masks offset by their relative positions
    if batMask.overlap( ballMask, ( ballRect.left - batRect.left, ballRect.top - batRect.top )):
        print "hit!"
        
    screen.fill(black)
    screen.blit(ball, ballRect)
    screen.blit(bat, batRect)
    pygame.display.flip()
