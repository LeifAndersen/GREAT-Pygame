
#setup initial stuff
import pygame,sys,random
#init pygame
pygame.init()
#set up dimensions and saved colors
size = width,height = 800,600
black = 0,0,0
white = 255,255,255
red = 255,0,0
#setup a clock for FPS stuffs
clock = pygame.time.Clock()
#set up the screen
screen = pygame.display.set_mode(size)
#set up the rect for the ball and the paddle

#build snake head
head_start = (40,300)
head = pygame.Rect(head_start,(20,20))

#build snake body
snake = [head]

#set up a font for writing to the screen
font = pygame.font.Font(None,32)
display_rect = pygame.Rect((0,0),(100,100))

# set initial direction for snake
direction = 0

#make initial apple
apple_location = ( random.randrange(0,width,20), random.randrange( 0, height, 20 ) )
apple = pygame.Rect( apple_location, (20,20) )
keep_playing = True
while keep_playing:

# use arrow keys to control snake and set direction
    for event in pygame.event.get():
        #handle closing the game
        if event.type == pygame.QUIT:
            sys.exit()
        #handle movement using key state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 2
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_UP:
                direction = 3
            if event.key == pygame.K_DOWN:
                direction = 1

# move snake head based on direction
    if direction == 0:
        head = head.move((20,0))
    if direction == 1:
        head = head.move((0,20))
    if direction == 2:
        head = head.move((-20,0))
    if direction == 3:
        head = head.move((0,-20))

    snake.pop(0)
#check for head body collisions
    for bodypart in snake:
        if head.colliderect(bodypart):
            direction = -1
            print("Die on body!!!")
            keep_playing = False

    snake.append( head )

#check for wall collision
    if head.top < 0 or head.bottom > height or head.left < 0 or head.right > width:
        direction = -1
        keep_playing = False
        print("Die!!")

#check for apple collision
    if head.colliderect( apple ):
        #make new apple location
        apple_location = ( random.randrange(0,width,20), random.randrange( 0, height, 20 ) )
        apple = pygame.Rect( apple_location, (20,20) )
        #grow snake body
        snake.append( head )

#draw everything
    #clear the screen
    screen.fill(black)

    #draw the snake
    for rectangle in snake:
        pygame.draw.rect(screen,white,rectangle)

    #draw the apple
    pygame.draw.rect(screen,red,apple)

    #screen.blit(font.render("lives: " + str(balls),True,white),display_rect)
    #tell the screen to update
    pygame.display.flip()
    #use the clock to limit the game to 40 frames/sec
    clock.tick(10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
