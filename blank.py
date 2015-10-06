import pygame 
from pygame.locals import *

# open in 32 bit version of python only

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

running = 1
exitcode = 0
while running:

   for event in pygame.event.get():

        if event.type==pygame.QUIT:
    
            pygame.quit()
            exit(0)

    







    
