import pygame,sys
from pygame.locals import *

WINDOWWITH=640
WINDOWHEIGHT=480
BGCOLOR=(0,0,255)


def main():
    pygame.init()


    DISPLAYSURF=pygame.display.set_mode((WINDOWWITH,WINDOWHEIGHT))
    pygame.display.set_caption("Four in a Row")
    DISPLAYSURF.fill(BGCOLOR)


    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()

    
if __name__=="__main__":
    main()
