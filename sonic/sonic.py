#!/usr/bin/env python2.7

import pygame, sys, math

# Init Pygame
pygame.init()
pygame.mixer.init()

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def get_rect(self, width = 0, height = 0):
        return pygame.Rect(self.x, self.y, width, height)

    def set_rect(self, rect):
        rect.x = self.x
        rect.y = self.y

# Screen
resolution = width, height = 700, 700
screen = pygame.display.set_mode(resolution)

# Colors
black = 0, 0, 0
white = 255, 255, 255

# Sonic
sonicSprite = pygame.image.load("sonic.png")
sonic = sonicSprite.get_rect()

# World
blockSprite = pygame.image.load("block.png")
world = [blockSprite.get_rect() for i in range(120)]

# Sonic's position
position = Vector(0, 0)
velocity = Vector(0, 0)
acceleration = Vector(0, 0.005)
starting_acceleration = Vector(0, 0.005)
terminal_velocity = 1

# Movement
move_up = False
move_down = False
move_left = False
move_right = False
jump = False

def end_game():
    pygame.quit()
    sys.exit()

def init():
    position.x = 100
    position.y = 600
    position.set_rect(sonic)
    x = 0
    y = 90
    right = False
    for block in world:
        block.x = x
        block.y = y
        x += 32
        if right and x > 800:
            x = 0
            y += 90
            right = False
        elif not right and x > 400:
            x = 300
            y += 90
            right = True

def events():
    global move_up, move_down, move_left, move_right, jump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_ESCAPE:
                end_game()
            if event.key == pygame.K_SPACE:
                jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_SPACE:
                jump = False

def update():
    global position, velocity, acceleration
    # Update Velocity and Position
    walking = False
    for block in world: # sonic should still be at correct position
        walking = walking or sonic.colliderect(block)
    if velocity.y < 0:
        walking = False
    if walking:
        velocity = Vector(0, 0)
        acceleration = Vector(0, 0)
        if jump:
            print "Here"
            velocity.y = -1
            position += velocity
        else:
            pass
    else:
        acceleration = starting_acceleration
        if abs(velocity.y + acceleration.y) <= terminal_velocity:
            velocity += acceleration
        else:
            velocity.y = terminal_velocity
        position += velocity

    # Character Movements
    if move_up:
        pass
    elif move_down:
        pass
    if move_left:
        position.x -= 0.5
    elif move_right:
        position.x += 0.5

    # Set Sonic to the new position
    position.set_rect(sonic)

def draw():
    screen.fill(black)
    screen.blit(sonicSprite, sonic)
    for block in world:
        screen.blit(blockSprite, block)
    pygame.display.flip()

def main():
    init()
    while True:
        events()
        update()
        draw()

if __name__ == '__main__':
    main()

