def spriteSheetToArray( sourceImage, numberRows, numberColumns, transparencyColor):
    imageArray = []
    sourceRect = sourceImage.get_rect()
    spriteWidth = sourceRect.width/numberColumns
    spriteHeight = sourceRect.height/numberRows

    for rows in range(numberRows):
        for cols in range(numberColumns):
            subImage = sourceImage.subsurface( pygame.Rect((spriteWidth*cols, spriteHeight*rows),(spriteWidth,spriteHeight)))
            subImage.set_colorkey( transparencyColor )
            imageArray.append(subImage)

    return imageArray

import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

#Load the explosion
allExplosions = pygame.image.load("SkybusterExplosion.gif")
allExplosions = allExplosions.convert()
explosion = spriteSheetToArray( allExplosions, 5, 4, (0,1,0)) # the parameters come from inspection of the sprite sheet
explosionRect = explosion[0].get_rect()


pygame.key.set_repeat(10, 10) #delay before first repeat in ms and then how often in ms 

#A counter for which sprite frame we are on
count = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #handle movement using key state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                explosionRect = explosionRect.move([-5,0])
            if event.key == pygame.K_RIGHT:
                explosionRect = explosionRect.move([ 5,0])
            if event.key == pygame.K_UP:
                explosionRect = explosionRect.move([0,-5])
            if event.key == pygame.K_DOWN:
                explosionRect = explosionRect.move([0, 5])

    screen.fill(black)

    # the mod operator % makes numbers set back to zero. Like a clock resets at 12
    screen.blit(explosion[count%len(explosion)], explosionRect)
    count += 1 #each time we draw one frame of the sprite, move to the next
    pygame.display.flip()
    # Make the game loop wait for 30 milliseconds before going again
    pygame.time.wait(30)
