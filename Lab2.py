import pygame
pygame.init()

pygame.display.set_caption("Lab2")
WIDTH = 800
HEIGHT = 480
BORDER = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
#walls
wcolor = pygame.Color("white")
#upper wall
#Rect((left, top), (width, height))
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH, BORDER)))
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))
pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT - BORDER),(WIDTH, HEIGHT)))


pygame.display.update()

# define a variable to control the main loop
running = True
    
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False