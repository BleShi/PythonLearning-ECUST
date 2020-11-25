import pygame,sys,random
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

#设置电脑智能度
DIFFICULTY=2

#屏幕刷新频率
FPS=30


#定义主函数
def main():
    global DISPLAYSURF,BOARDIMG,REDTOKENIMG,BLACKTOKENIMG,REDPILERECT,BLACKPILERECT,FPSCLOCK
    pygame.init()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("四连珠")

    #
    FPSCLOCK=pygame.time.Clock()

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
    if isFirstGame:
        #首次游戏计算机先走
        turn="computer"
        showHelp=True
    else:
        #随机选择谁先走
        if random.randint(0,1)==0:
            turn="computer"
        else:
            turn="human"
        showHelp=False
        
    #初始化界面数据
    mainBoard=getNewBoard()
    
    while True:
        if turn=="human":
            #轮到你走
            getHumanMove(mainBoard,showHelp)
            if showHelp:
                showHelp=False
            if isWinner(mainBoard,"red"):
                winnerImg=HUMANWINNERIMG
                break
            turn="computer"
        else:
            #轮到计算机走
            #确定走子位置
            column=getComputerMove(mainBoard)
            #计算机走棋子动画
            animateComputerMoving(mainBoard,column)
            #游戏板棋子分布数据更新
            makeMove(mainBoard,"black",column)
            if isWinner(mainBoard,"black"):
                winnerImg=COMPUTERWINNERIMG
                break
            turn="human"
            
        if isBoardFull(mainBoard):
            winnerImg=TIEWINNERIMG
            break
        
    while True:
        #画游戏界面
        drawBoard(mainBoard)
        DISPLAYSURF.blit(winnerImg,WINNERRECT)
        pygame.display.update()
        FPSCLOCK.tick()
    
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()


#游戏板棋子分布数据更新（已完成）
def makeMove(board,player,column):
    lowest=getLowestEmptySpace(board,column)
    if lowest!=-1:
        board[column][lowest]=player

        
#画游戏板及棋子（已完成）
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
        elif extraToken["color"]=="black":
            DISPLAYSURF.blit(BLACKTOKENIMG,(extraToken["x"],extraToken["y"],SPACESIZE,SPACESIZE))
            
    #画游戏板
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE),YMARGIN+(y*SPACESIZE))
            DISPLAYSURF.blit(BOARDIMG,spaceRect)

    #画左右图案
    DISPLAYSURF.blit(REDTOKENIMG,REDPILERECT)
    DISPLAYSURF.blit(BLACKTOKENIMG,BLACKPILERECT)


#
def getHumanMove(board,isFirstMove):
    draggingToken=False
    tokenx,tokeny=None,None

    #
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN and not draggingToekn and REDPILERECT.collidepoint(event.pos):
                #开始走红棋
                draggingToken=True
                tokenx,tokeny=event.pos


#初始化界面数据
def getNewBoard():
    board=[]
    for x in range(BOARDWIDTH):
        board.append([None]*BOARDHEIGHT)
    return board



#计算机走棋子动画（已完成）
def animateComputerMoving(board,column):
    #黑子向上移动（动画来了）
    x=BLACKPILERECT.left
    y=BLACKPILERECT.top
    speed=1.0
    while y>(YMARGIN-SPACESIZE):
        y-=int(speed)
        speed+=0.5
        drawBoard(board,{"x":x,"y":y,"color":"black"})
        pygame.display.update()
        FPSCLOCK.tick()

    #黑子向左移动
    y=YMARGIN-SPACESIZE
    speed=1.0
    while x>(XMARGIN+column*SPACESIZE):
        x-=int(speed)
        speed+=0.5
        drawBoard(board,{"x":x,"y":y,"color":"black"})
        pygame.display.update()
        FPSCLOCK.tick()

    #column列black颜色的棋子向下移动
    animateDroppingToken(board,column,"black")


#column列color颜色的棋子向下移动（已完成）
def animateDroppingToken(board,column,color):
    x=XMARGIN+column*SPACESIZE
    y=YMARGIN-SPACESIZE
    dropSpeed=1.0

    #确定column列的最下面空位
    lowestEmptySpace=getLowestEmptySpace(board,column)
    #棋子向下移动
    while True:
        y+=int(dropSpeed)
        dropSpeed+=0.5
        if int((y-YMARGIN)/SPACESIZE)>=lowestEmptySpace:
            return
        drawBoard(board,{"x":x,"y":y,"color":color})
        pygame.display.update()
        FPSCLOCK.tick()


#确定下落位置
def getLowestEmptySpace(board,column):
    #从下面开始检查column列空的位置
    for y in range(BOARDHEIGHT-1,-1,-1):
        if board[column][y]==None:
            return y
    return -1


#确定计算机走子位置
def getComputerMove(board):
    #为各个位置确定优劣
    potentialMoves=getPotentialMoves(board,"black",DIFFICULTY)
    #确定最优值
    bestMoveFitness=-1
    for i in range(BOARDWIDTH):
        #假如位置最优并且没有走满
        if potentialMoves[i]>bestMoveFitness and isValidMove(board,i):
            bestMoveFitness=potentialMoves[i]
    #根据最优值找到所有位置
    bestMoves=[]
    for i in range(BOARDWIDTH):
        if potentialMoves[i]==bestMoveFitness and isValidMove(board,i):
            bestMoves.append(i)
    return random.choice(bestMoves)


#为各个位置确定优劣
def getPotentialMoves(board,tile,lookAhead):
    #假如计算机智能级别最低，或者游戏板已满
    if lookAhead==0 or isBoardFull(board):
        return [0]*BOARDWIDTH

    if tile=="red":
        enemyTile="black"
    else:
        enemyTile="red"

    #找到最佳走法
    potentialMoves=[0]*BOARDWIDTH
    return potentialMoves


#检测当前位置是否可以走子（已完成）
def isValidMove(board,column):
    if column<0 or column>=(BOARDWIDTH) or board[column][0]!=None:
        return False
    return True


#检测游戏板是否已满（已完成）
def isBoardFull(board):
    #假如游戏板没有空位，返回Ture，否则返回False
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y]==None:
                return False
    return True


#
def isWinner(board,tile):
    pass
if __name__=="__main__":
    main()
