import argparse
#!/usr/bin/env python3
"""TicTacToe with Minimax"""
__author__="Marco A Cortes | Andrew Envia"


class gameboard:
    board=[[' ' for i in range(3)] for i in range(3)]
    def printboard(self):
        for y,yvalue in enumerate(self.board):
            for x,xvalue in enumerate(self.board):
                #print(""+self.board[x][y],end=" ")
                if x<2:
                    print(""+self.board[x][y]+" | ",end="")
                    #print("| ",end="")
                else:
                    print(""+self.board[x][y])
            #print("---------")
            if y<2:
                print("---------")
    def clearBoard(self):
        for x in range(0,3):
            for y in range(0,3):
                self.board[x][y]=' '
        self.printboard()
                #self.board[x][y]=0
    def getChar(self, pos):
        return self.board[int(pos[0])][int(pos[1])]

    def setCharAI(self,player,pos):
        self.board[int(pos[0])][int(pos[1])]=player

    def setChar(self,player,pos):
        try:
            if self.board[int(pos[0])][int(pos[1])]!=" ":
                self.printboard()
                print("Space taken")
                return False
            else:
                self.board[int(pos[0])][int(pos[1])]=player
                return True
        except:
            print("!!Reminder!!\n!!Move position for both integers must be between 0 and 2!!\n!!Example: for bottom right slot, input '22'!!")
            return False

class tttRules:
    count=0
    tttboard=gameboard()
    win1=0
    win2=0
    draw=0
    continueGame=True

    def displayScore(self):
        print("Player 1: "+str(self.win1)+"\nPlayer 2: "+str(self.win2)+"\nDraws: "+str(self.draw))

    def setCount(self):
        self.count=0

    def play(self):
        self.tttboard.clearBoard()
        self.setCount()
        #self.tttboard.printboard()
        self.continueGame=True
        while self.continueGame==True:
            self.checkTurn()
    def checkTurn(self):
        if self.count%2==0:
            self.turn1()
        else:
            self.turn2()
        self.tttboard.printboard()
        #self.tttboard.printboard()
    def turn1(self):
        #possibleMoves(self.tttboard)
        full=0
        spaceTaken=False
        while spaceTaken==False:
            space=input("Player 1, make move:")
            spaceTaken=self.tttboard.setChar('x',space)
        self.count+=1
        for x in range(0,3):
            for y in range(0,3):
                if self.tttboard.board[x][y]!=" ":
                    full+=1


        if checkforwin(self.tttboard,'x'):
            self.continueGame=False
            self.win1+=1
        elif full==9:
            self.continueGame=False
            self.draw+=1

    def turn2(self):
        print("Minimax")
        move=self.returnbestmove(self.tttboard)
        self.tttboard.setChar('o',move)
        self.count+=1
        full=0
        for x in range(0,3):
            for y in range(0,3):
                if self.tttboard.board[x][y]!=" ":
                    full+=1
        if checkforwin(self.tttboard,'o'):
            self.continueGame=False
            self.win2+=1
        elif full==9:
            self.continueGame=False
            self.draw+=1

    def returnbestmove(self,tempBoard):
        bestScore=-1000
        for x in possibleMoves(tempBoard):
            tempBoard.setCharAI("o",x)
            moveScore=self.minimax(tempBoard,'x')
            tempBoard.setCharAI(" ",x)
            if moveScore>bestScore:
                bestMove=x
                bestScore=moveScore
        return bestMove

    def minimax(self,tempBoard,currentPlayer):
        availablemoves=possibleMoves(tempBoard)
        #checks for terminal state and returns heuristic value
        if checkforwin(tempBoard,'o'):
            return 10
        elif checkforwin(tempBoard,'x'):
            return -10
        elif len(availablemoves) == 0:
            return 0

        if currentPlayer=='o':
            bestscore=-1000
            for x in availablemoves:
                tempBoard.setCharAI('o',x)
                #bestscore=max(bestscore,self.minimax(tempBoard,'x'))
                if self.minimax(tempBoard,'x')>bestscore:
                    bestscore=self.minimax(tempBoard,'x')
                tempBoard.setCharAI(' ',x)
            return bestscore

        else:
            bestscore=1000
            for x in availablemoves:
                tempBoard.setCharAI('x',x)
                #bestscore=min(bestscore,self.minimax(tempBoard,'o'))
                if self.minimax(tempBoard,'o')<bestscore:
                    bestscore=self.minimax(tempBoard,'o')
                tempBoard.setCharAI(' ',x)
            return bestscore
        #fc+=1
def possibleMoves(tboard):
    posMoves=[]
    for x in range(0,3):
        for y in range(0,3):
            if tboard.board[x][y]==" ":
                #print(str(x)+str(y))
                posMoves.append(str(x)+str(y))
    #print(posMoves)
    return posMoves
def checkforwin(tboard,player):
    #print(tboard.board[0][0])
    parseShit=0
    if tboard.board[0][0]==player:
        if tboard.board[0][1]==player and tboard.board[0][2]==player:
            return True
        if tboard.board[1][1]==player and tboard.board[2][2]==player:
            return True
        if tboard.board[1][0]==player and tboard.board[2][0]==player:
            return True
    if tboard.board[2][2]==player:
        if tboard.board[2][1]==player and tboard.board[2][0]==player:
            return True
        if tboard.board[1][2]==player and tboard.board[0][2]==player:
            return True
    if tboard.board[0][1]==player and tboard.board[1][1]==player and tboard.board[2][1]==player:
        return True
    if tboard.board[1][0]==player and tboard.board[1][1]==player and tboard.board[1][2]==player:
        return True
    if tboard.board[2][0]==player and tboard.board[1][1]==player and tboard.board[0][2]==player:
        return True
    return False

def start():
    print("This is tictactoe ")
    newgame=tttRules()
    keepPlaying=True
    while keepPlaying==True:
        newgame.play()
        newgame.displayScore()
        if input("Play again?:")=='y':
            keepPlaying=True
        else:
            keepPlaying=False
    print("Thanks for playing:\n")
    newgame.displayScore()

start()
"""
parser = argparse.ArgumentParser()
parser.add_argument("argument", help="Use argument 'help' for instructions.\nUse argument 'start' to start the game.")
args = parser.parse_args()
#print(args.argument)
if args.argument=="help":
    print("\n\nThis is a game of Tic Tac Toe played against the minimax algorithm.\nWhen prompted, you will input your moves using two integers, each between 0 and 2.\nThe first will specify the column, with 0 being the left-most column and 2 being the right-most column.\nThe second will specify the row, with 0 being the top row and 2 being the bottom.\nFor example: playing '12' will place your move in the center column of the bottom row.\n\nUse argument 'start' to run the game.\n\n")
if args.argument=="start":
    start()

"""
