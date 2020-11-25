import pygame,sys
from pygame.locals import *


BOARDWIDTH=7
BOARDHEIGHT=6
assert BOARDWIDTH>=4 and BOARDHEIGHT>=4,"Board must be at least 4*4."

FPS=30
WINDOWWIDTH=640
WINDOWHEIGHT=480

BRIGHTBLUE=(0,50,255)

BGCOLOR=BRIGHTBLUE

EMPTY=None

HUMAN="human"
COMPUTER="computer"

def main():
    global FPSCLOCK,DISPLAYSURF,HUMANWINNERIMG,COMPUTERWINNERIMG,WINNERRECT
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Four in a Row")


    HUMANWINNERIMG=pygame.image.load("4row_humanwinner.png")
    COMPUTERWINNERIMG=pygame.image.load("4row_computerwinner.png")
    WINNERRECT=HUMANWINNERIMG.get_rect()
    WINNERRECT.center=(int(WINDOWWIDTH/2),int(WINDOWHEIGHT/2))

    isFirstGame=True
    while True:
        runGame(isFirstGame)
        isFirstGame=False


def runGame(isFirstGame):
    if isFirstGame:
        turn=COMPUTER
        showHelp=True
    else:
        if random.randint(0,1)==0:
            turn=COMPUTER
        else:
            turn=HUMAN
        showHelp=False

        
    mainBoard=getNewBoard()

    while True:
        if turn==HUMAN:
            #getHumanMove(mainBoard,showHelp)
            winnerImg=HUMANWINNERIMG
            break
        else:
            winnerImg=COMPUTERWINNERIMG
            break


    while True:
        drawBoard(mainBoard)
        DISPLAYSURF.blit(winnerImg,WINNERRECT)
        pygame.display.update()
        FPSCLOCK.tick()
        while True:
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()


def drawBoard(board,extraToken=None):
    DISPLAYSURF.fill(BGCOLOR)
    
def getNewBoard():
    board=[]
    for x in range(BOARDWIDTH):
        board.append([EMPTY]*BOARDHEIGHT)
        return board
    
    
if __name__=="__main__":
    main()
