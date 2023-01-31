import pygame
from pygame.locals import *
import random
from algorithms.bubblesort import bubblesort
from components import is_sorted
from algorithms.bogosort import bogosort
from algorithms.selectionsort import selectionsort
import sys

# Debug mode waits for a keystroke before drawing next screen
debugMode = False

# DO NOT CHANGE

BOGOSORT = "bogosort"
BUBBLESORT = "bubblesort"
SELECTIONSORT = "selectionsort"

index = 0
unsorted_index = 0
sorted = False
list_sorted = False
fpsClock = pygame.time.Clock()
# Constants



algorithm = BUBBLESORT

RED = (255,0,0)

# Dictates the running speed of the program
# Set fps to low amount for better visualization or high for faster sorting 
FPS = 60

WIDTH, HEIGHT = 800, 650
SIZE = 15
LINE_WIDTH = 4
MARGIN = LINE_WIDTH+1


# List Variables
# Manipulate these variables to change the range of numbers in the list or the size of the list
MINNUM = 5
MAXNUM = 60
LENGTH = 20
numlist = [random.randint(MINNUM,MAXNUM) for x in range(LENGTH)]






 
pygame.init()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
startX = (WIDTH/2)-(LENGTH*(MARGIN/2))
y = 25

def drawList(listi):
    for ind,num in enumerate(listi):
        p1 = (startX+((MARGIN)*ind),y)
        p2 = (startX+((MARGIN)*ind),y+(num*SIZE/2))
        if ind != index:
            pygame.draw.line(screen,(255,255,255),p1,p2,width=LINE_WIDTH)
        else:
            pygame.draw.line(screen,RED,p1,p2,width=LINE_WIDTH)


drawList(numlist) # Initializes 
pygame.display.flip()

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw.

    if not sorted:
        if debugMode:
            flag = True
            while flag:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        flag = False
                    elif event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
        if algorithm == "bogosort":
            numlist = bogosort(numlist)
            if is_sorted(numlist):
                sorted = True

        elif algorithm == "bubblesort":
            if index > len(numlist)-2:
                if not is_sorted(numlist):
                    index = 0
                else:
                    sorted = True
            if not sorted:
                numlist = bubblesort(numlist,index)
                index += 1

        elif algorithm == "selectionsort":
            index,numlist = selectionsort(numlist)
            if is_sorted(numlist):
                sorted = True
            

    else:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                quit()


    
    drawList(numlist)

    pygame.display.flip()
    fpsClock.tick(FPS)
