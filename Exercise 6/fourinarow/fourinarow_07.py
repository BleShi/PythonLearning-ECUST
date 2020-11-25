import pygame,sys
from pygame.locals import *


#设置游戏板大小
BOARDWIDTH=7
BOARDHEIGHT=6
assert BOARDWIDTH>=4 and BOARDHEIGHT>=4,"游戏板最小尺寸为4*4"

#设置窗口大小
WINDOWWIDTH=640
WINDOWHEIGHT=480

#设置游戏板每个格子（正方形）的边长
SPACESIZE=50

#设置游戏板起始位置
XMARGIN=int((WINDOWWIDTH-BOARDWIDTH*SPACESIZE)/2)
YMARGIN=int((WINDOWHEIGHT-BOARDHEIGHT*SPACESIZE)/2)

#定义颜色
BRIGHTBLUE=(0,50,255)
WHITE=(255,255,255)

#设置颜色
BGCOLOR=BRIGHTBLUE
TEXTCOLOR=WHITE


#定义主函数
def main():
    global DISPLAYSURF,BOARDIMG,REDTOKENIMG,BLACKTOKENIMG,REDPILERECT,BLACKPILERECT
    pygame.init()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("四连珠")

    #加载图形
    BOARDIMG=pygame.image.load("4row_board.png")
    BOARDIMG=pygame.transform.smoothscale(BOARDIMG,(SPACESIZE,SPACESIZE))
    REDTOKENIMG=pygame.image.load("4row_red.png")
    REDTOKENIMG=pygame.transform.smoothscale(REDTOKENIMG,(SPACESIZE,SPACESIZE))
    BLACKTOKENIMG=pygame.image.load("4row_black.png")
    BLACKTOKENIMG=pygame.transform.smoothscale(BLACKTOKENIMG,(SPACESIZE,SPACESIZE))

    #指定图形位置大小
    REDPILERECT=pygame.Rect(int(SPACESIZE/2),WINDOWHEIGHT-int(3*SPACESIZE/2),SPACESIZE,SPACESIZE)
    BLACKPILERECT=pygame.Rect(WINDOWWIDTH-int(3*SPACESIZE/2),WINDOWHEIGHT-int(3*SPACESIZE/2),SPACESIZE,SPACESIZE)

    isFirstGame=True
    while True:
        #开始游戏
        runGame(isFirstGame)
        isFirstGame=False


#开始游戏
def runGame(isFirstGame):
    #初始化界面数据
    mainBoard=getNewBoard()
    
    #画游戏界面
    drawBoard(mainBoard)
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()


def drawBoard(board,extraToken=None):
    DISPLAYSURF.fill(BGCOLOR)

    #画棋子
    spaceRect=pygame.Rect(0,0,SPACESIZE,SPACESIZE)
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE),YMARGIN+(y+SPACESIZE))
            if board[x][y]=="red":
                DISPLAYSURF.blit(REDTOKENIMG,spaceRect)
            elif board[x][y]=="black":
                DISPLAYSURF.blit(BLACKTOKENIMG,spaceRect)
    #
    if extraToken!=None:
        if extraToken["color"]=="red":
            DISPLAYSURF.blit(REDTOKENIMG,(extraToken["x"],extraToken["y"],SPACESIZE,SPACESIZE))
        elif extraToken["color"]==BLACK:
            DISPLAYSURF.blit(BLACKTOKENIMG,(extraToken["x"],extraToken["y"],SPACESIZE,SPACESIZE))
            
    #画游戏板
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE),YMARGIN+(y*SPACESIZE))
            DISPLAYSURF.blit(BOARDIMG,spaceRect)

    #画左右图案
    DISPLAYSURF.blit(REDTOKENIMG,REDPILERECT)
    DISPLAYSURF.blit(BLACKTOKENIMG,BLACKPILERECT)


#初始化界面数据
def getNewBoard():
    board=[]
    for x in range(BOARDWIDTH):
        board.append([None]*BOARDHEIGHT)
    return board


if __name__=="__main__":
    main()
