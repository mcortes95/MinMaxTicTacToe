class gameboard:
    board=[[' ' for i in range(3)] for i in range(3)]
    #def __init__(self):
        #board=[['o' for i in range(3)] for i in range(3)]
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
    def setC(self, row, col):
        if self.board[row][col]!=" ":
            print("Space taken")
            return False
        else:
            self.board[row][col]='x'
            return True


    def setChar(self,player,pos):
        if self.board[int(pos[0])][int(pos[1])]!=" ":
            print("Space taken")
            return False
        else:
            self.board[int(pos[0])][int(pos[1])]=player
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
        self.tttboard.printboard()
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
        if full==9:
            self.continueGame=False
            self.draw+=1
        if self.checkforWin('x')==True:
            self.continueGame=False
            self.win1+=1

    def turn2(self):
        full=0
        spaceTaken=False
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
        if self.checkforWin('o')==True:
            self.continueGame=False
            self.win2+=1

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
        else:
            return False
#print (gameboard.board)
#print (gameboard.board[2][2])
newboard=gameboard()
#newboard.printboard()
newboard.clearBoard()
newgame=tttRules()
#newgame.tttboard.printboard()
newgame.displayScore()
newgame.play()
newgame.tttboard.printboard()
newgame.turn1()
newgame.tttboard.printboard()
newgame.turn2()
newgame.tttboard.printboard()

