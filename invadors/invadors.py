import sys, pygame
pygame.init()

move_left  = False
move_right = False
move_up    = False
move_down  = False

resolution = width, height = 700, 700

# Your ship
shipSprite = pygame.image.load("ship.jpg")
ship = shipSprite.get_rect()

# Enemy Ships
enemySprite = pygame.image.load("enemy.jpg")
enemies = [enemySprite.get_rect() for i in range(100)]
enemyVelocities = [1 for enemy in enemies]

# Lazers
laserSprite = pygame.image.load("laser.jpg")
lasers = []

screen = pygame.display.set_mode(resolution)

black = 0, 0, 0
white = 255, 255, 255

# Music
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(0)

explosion = pygame.mixer.Sound("explosion1.wav")
pew = pygame.mixer.Sound("pew1.wav")

def end_game():
    pygame.quit()
    sys.exit()

def init():
    # Setup Ship
    ship.x = 350
    ship.y = 600
    x = 0
    y = 10
    for enemy in enemies:
        enemy.x = x
        enemy.y = y
        x += 50
        if x > 650:
            x = 0
            y += 40

def create_laser(location):
    laser = laserSprite.get_rect()
    laser.x = location.x
    laser.y = location.y
    return laser

def draw():
    screen.fill(black)
    screen.blit(shipSprite, ship)
    for enimy in enemies:
        screen.blit(enemySprite, enimy)
    for laser in lasers:
        screen.blit(laserSprite, laser)
    pygame.display.flip()

def events():
    global move_up, move_down, move_right, move_left
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_ESCAPE:
                end_game()
            if event.key == pygame.K_SPACE:
                pew.play()
                lasers.append(create_laser(ship))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

def move():
    # Move Self
    if move_left:
        ship.x -= 1
    elif move_right:
        ship.x += 1
    if ship.x < 0:
        ship.x = 1
    elif ship.x > width-32:
        ship.x = width-33

    # Set Enemy Velocity
    i = 0
    for enemy in enemies:
        if enemy.x > width - 32:
            enemyVelocities[i] = -1
            enemy.x = width - 33
            enemy.y += 30
        if enemy.x < 0:
            enemyVelocities[i] = 1
            enemy.x = 1
            enemy.y += 30
        i += 1

    # Move Enemies
    i = 0
    for enemy in enemies:
        enemy.x += enemyVelocities[i]
        i += 1

    # Move Bullets
    for laser in lasers:
        laser.y -= 1

    # Check to see if ship has collided/game over
    for enemy in enemies:
        if enemy.colliderect(ship) or enemy.y > height:
            explosion.play()
            end_game()

    # Laser Enemy Collisions
    for laser in lasers[:]:
        for enemy in enemies[:]:
            if laser.colliderect(enemy):
                explosion.play()
                try:
                    lasers.remove(laser)
                except:
                    pass
                try:
                    enemies.remove(enemy)
                except:
                    pass
    # Check to see if won
    if len(enemies) == 0:
        end_game()

def main():
    init()
    while True:
        pygame.time.delay(10)
        events()
        move()
        draw()

if __name__ == '__main__':
    main()
