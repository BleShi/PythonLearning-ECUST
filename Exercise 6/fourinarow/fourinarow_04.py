import pygame,sys
from pygame.locals import *


def main():
    pygame.init()

    isFirstGame=True
    runGame(isFirstGame)
    isFirstGame=False


def runGame(isFirstGame):
    DISPLAYSURF=pygame.display.set_mode((400,300))
    pygame.display.set_caption("Four in a Row")
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()



    
if __name__=="__main__":
    main()
