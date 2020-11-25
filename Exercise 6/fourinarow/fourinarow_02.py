import pygame,sys
from pygame.locals import *


pygame.init()
DISPLAYSURF=pygame.display.set_mode((400,300))
pygame.display.set_caption("Four in a Row")
DISPLAYSURF.fill((255,0,0))


while True:
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.display.update()
