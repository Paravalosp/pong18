import pygame

class Ball:
    #class var
    RADIUS = 10
    
    def __init__(self, x, y, vx, vy, screen, wcolor, bgcolor):
        #instance var
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.wcolor = wcolor
        self.bgcolor = bgcolor
    
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        self.show(self.bgcolor)
        if(self.x < 40 or self.x == 800):
            self.vx = -1*self.vx
        if(self.y < 40 or self.y > 440):
            self.vy = -1*self.vy

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.wcolor)
        #TODO:
        #check if colliding:
            #flip velocity