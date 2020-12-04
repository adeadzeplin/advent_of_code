import pygame
import random
from getexpenses import get_expenses
import numpy as np

WIDTH = 700
HEIGHT = 500

DONE = False

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLUE = (0,255,255)

class V():
    def __init__(self):
        self.x = (random.random()*2 - 1)*5
        self.y = (random.random()*2 - 1)*5

MAXVEL = 5
class S():
    def __init__(self,n,x,y,color=WHITE):
        self.n=n
        self.x =x
        self.y =y
        self.w = random.randint(10,15)
        self.h = random.randint(10,15)
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.v = V()
        self.color = color
        self.timer = 0
        self.time_enable = False
        self.endtimer = 0


    def m(self):
        self.x += self.v.x
        self.y += self.v.y
        if self.x < 0:
            self.x = 1
            if self.v.x < MAXVEL:
                self.v.x *= -1.1
            else:
                self.v.x *= -.5

        if self.y < 0:
            self.y = 1
            if self.v.y < MAXVEL:
                self.v.y *= -1.1
            else:
                self.v.y *= -.5

        if self.x + self. w > WIDTH:
            self.x = WIDTH-1 - self. w
            if self.v.x < MAXVEL:
                self.v.x *= -1.1
            else:
                self.v.x *= -.5
        if self.y + self. h  > HEIGHT:
            self.y = HEIGHT-1 - self. h
            if self.v.y < MAXVEL:
                self.v.y *= -1.1
            else:
                self.v.y *= -.5
        if self.color == GREEN:
            self.endtimer +=1
            if self.endtimer > 200:
                global DONE
                DONE = True

        elif self.n == 927 or self.n == 1093:
            self.color = BLUE

        elif self.time_enable:
            self.timer+=1
            if self.timer > 5:
                self.time_enable = False
                self.timer = 0

            else:
                self.color = RED
        else:
            self.color = WHITE

        self.updaterect()
    def updaterect(self):

        self.rect.x = self.x
        self.rect.y = self.y

    def printR(self,screen):
        pygame.draw.rect(screen, self.color,self.rect)


def moverects(listor):
    for r in listor:
        r.m()

def printrects(listor,screen):
    for r in listor:
        r.printR(screen)

def create_rects():
    def n():
        return random.randint(0,WIDTH), random.randint(0,HEIGHT)
    array_of_expenses = get_expenses()
    array_of_rects = []
    for e in array_of_expenses:
        x, y = n()
        boob = S(e,x,y)

        array_of_rects.append(boob)
    return array_of_rects

def collide(list_r):
    newlist = list_r.copy()
    for x, r in enumerate(newlist):
        for r2 in newlist:
            if r == r2:
                continue
            if r.rect.colliderect(r2.rect):
                # print("FUCK YES")
                r.time_enable = True
                r2.time_enable = True
                # print(r.n + r2.n)

                if (r.n + r2.n) == 2020:
                    print(r.n*r2.n)
                    r.color = GREEN
                    r2.color= GREEN
                    success_list = [r,r2]
                    return success_list
    return list_r

        # newlist.pop(x)
def reset(alist):
    while len(alist) > 0:
        alist.pop()
    alist = create_rects()
    return alist


def main():
    global DONE
    DONE = False
    rects = create_rects()
    pygame.init()
    # Set the width and height of the screen [width, height]
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")
    # Loop until the user clicks the close button.

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    done = False
    while not done:


        if DONE:
            rects = reset(rects)
            DONE = False
            print("reset")

        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # --- Game logic should go here
        moverects(rects)
        rects = collide(rects)

        # --- Screen-clearing code goes here
        screen.fill(BLACK)

        # --- Drawing code should go here
        printrects(rects,screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()

# Best Sauce ever = dijjon mustard + maple syrup