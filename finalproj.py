import argparse
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
        if self.board[int(pos[0])][int(pos[1])]!=" ":
            self.printboard()
            print("Space taken")
            return False
        else:
            self.board[int(pos[0])][int(pos[1])]=player
            return True
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
    def turn1(self):
        possibleMoves(self.tttboard)
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
        #print(full)

        #print(checkforwin(self.tttboard,'x'))
        #print(self.checkforWin('x'))
        if self.checkforWin('x')==True:
            self.continueGame=False
            self.win1+=1
        elif full==9:
            self.continueGame=False
            self.draw+=1

    def turn2(self):
        #move=self.minimax(self.tttboard,'o')
        move=self.returnbestmove(self.tttboard)
        self.tttboard.setChar('o',move)
        self.count+=1
    def turn3(self):
        full=0
        spaceTaken=False
        self.minimax(self.tttboard,'o')
        while spaceTaken==False:
            space=input("Player 2, make move:")
            spaceTaken=self.tttboard.setChar('o',space)
        self.count+=1
        for x in range(0,3):
            for y in range(0,3):
                if self.tttboard.board[x][y]!=" ":
                    full+=1
        if full==9:
            self.continueGame=False
            self.draw+=1
        elif checkforwin(self.tttboard,'o')==True:
            self.continueGame=False
            self.win2+=1
        #elif self.checkforWin('o')==True:
         #   self.continueGame=False
         #   self.win2+=1

    def checkforWin(self,player):
        parseShit=0
        if self.tttboard.board[parseShit][parseShit]==player:
            if self.tttboard.board[parseShit][parseShit+1]==player and self.tttboard.board[parseShit][parseShit+2]==player:
                return True
            elif self.tttboard.board[parseShit+1][parseShit+1]==player and self.tttboard.board[parseShit+2][parseShit+2]==player:
                return True
            elif self.tttboard.board[parseShit+1][parseShit]==player and self.tttboard.board[parseShit+2][parseShit]==player:
                return True
        elif self.tttboard.board[parseShit+2][parseShit+2]==player:
            if self.tttboard.board[parseShit+2][parseShit+1]==player and self.tttboard.board[parseShit+2][parseShit]==player:
                return True
            elif self.tttboard.board[parseShit+1][parseShit+2]==player and self.tttboard.board[parseShit][parseShit+2]==player:
                return True
        elif self.tttboard.board[parseShit][parseShit+1]==player and self.tttboard.board[parseShit+1][parseShit+1]==player and self.tttboard.board[parseShit+2][parseShit+1]==player:
            return True
        elif self.tttboard.board[parseShit+1][parseShit]==player and self.tttboard.board[parseShit+1][parseShit+1]==player and self.tttboard.board[parseShit+1][parseShit+2]==player:
            return True
        elif self.tttboard.board[parseShit+2][parseShit]==player and  self.tttboard.board[parseShit+1][parseShit+1]==player and self.tttboard.board[parseShit][parseShit+2]==player:
            return True
        return False

    def possibleMoves(self):
        posMoves=[]
        for x in range(0,3):
            for y in range(0,3):
                if self.tttboard.board[x][y]==" ":
                    #print(str(x)+str(y))
                    posMoves.append(str(x)+str(y))
        print(posMoves)
        print("WORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONEWORNGONE")
        return posMoves
<<<<<<< HEAD
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
        #availablemoves=self.possibleMoves()
        #print(tempBoard.board)
=======
    def minimax(self):
        availablemoves=self.possibleMoves()
        score=0
        if self.checkforWin('o'):
            score = 10
        elif self.checkforWin('o'):
            score = -10
        elif len(availablemoves) == 0:
            score=0
        print(score)
        move=[]
>>>>>>> origin/master

        availablemoves=possibleMoves(tempBoard)
        #print("length"+str(len(availablemoves)))
        #print(availablemoves)
        #print("LOSS=================================================LOSS=================================================")
        movescore=0
        if checkforwin(tempBoard,'o'):
            #print("10")
            return 10
        elif checkforwin(tempBoard,'x'):
            #print("-10")
            return -10
        elif len(availablemoves) == 0:
            #print("zero moves left")
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
    parseShit=0
    if tboard.board[parseShit][parseShit]==player:
        if tboard.board[parseShit][parseShit+1]==player and tboard.board[parseShit][parseShit+2]==player:
            return True
        elif tboard.board[parseShit+1][parseShit+1]==player and tboard.board[parseShit+2][parseShit+2]==player:
            return True
        elif tboard.board[parseShit+1][parseShit]==player and tboard.board[parseShit+2][parseShit]==player:
            return True
    elif tboard.board[parseShit+2][parseShit+2]==player:
        if tboard.board[parseShit+2][parseShit+1]==player and tboard.board[parseShit+2][parseShit]==player:
            return True
        elif tboard.board[parseShit+1][parseShit+2]==player and tboard.board[parseShit][parseShit+2]==player:
            return True
    elif tboard.board[parseShit][parseShit+1]==player and tboard.board[parseShit+1][parseShit+1]==player and tboard.board[parseShit+2][parseShit+1]==player:
        return True
    elif tboard.board[parseShit+1][parseShit]==player and tboard.board[parseShit+1][parseShit+1]==player and tboard.board[parseShit+1][parseShit+2]==player:
        return True
    elif tboard.board[parseShit+2][parseShit]==player and tboard.board[parseShit+1][parseShit+1]==player and tboard.board[parseShit][parseShit+2]==player:
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help = "The postition you want to use.",type = int) #Suppose to print out help message
    args = parser.parse_args()

    print("This is tictactoe ")
    newgame=tttRules()
    keepPlaying=True
    while keepPlaying==True:
        newgame.play()
        newgame.displayScore()
        if input("Play again?:")=='y':
            keepPlaying==True
        else:
            keepPlaying=False
    print("Thanks for playing:")
    newgame.displayScore()
if __name__ == "__Main__":
    Main()
