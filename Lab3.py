from Paddle import Paddle
from Ball import Ball
import random
import pygame
pygame.init()

pygame.display.set_caption("Lab2")
WIDTH = 800
HEIGHT = 480
BORDER = 20
VELOCITY = 5
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
#walls
wcolor = pygame.Color("white")
bgcolor = pygame.Color("black")
#upper wall
#Rect((left, top), (width, height))
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH, BORDER)))
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))
pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT - BORDER),(WIDTH, HEIGHT)))

#ball init
ran = random.choice((-1, 1))
x0 = WIDTH - Ball.RADIUS
y0 = HEIGHT//2
vx0 = -VELOCITY
vy0 = VELOCITY * ran

#TODO:
    #start +/- random 45 ang.
b0 = Ball(x0, y0, vx0, vy0, screen, wcolor, bgcolor)
b0.show(wcolor)

pygame.display.update()

# define a variable to control the main loop
running = True
clock = pygame.time.Clock()
    
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
    pygame.display.update()
    clock.tick(FPS)

    #Ball     
    b0.update()