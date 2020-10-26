from copy import deepcopy
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear')

class boardStateClass:
    def __init__(self):
        self.board = []
        self.playerToMove = 1
        self.lastMove = 0
        self.history = []
    def printBoard(self):
        for c, i in enumerate(self.board):
            for j in i:
                if j == 0:
                    print("_", end = "")
                else:
                    print(j.symbol, end = "")
            print("  {}".format(8-c))
        print()
        print("ABCDEFGH")
        print()
    def createBoard(self):
        temporaryTab = []
        self.board.append([rook([0, 0], -1),knight([0, 1], -1),bishop([0, 2], -1),queen([0,3], -1),king([0,4], -1),bishop([0, 5], -1),knight([0, 6], -1),rook([0, 7], -1)])
        for i in range(8):
            temporaryTab.append(pon([1, i], -1))
        self.board.append(deepcopy(temporaryTab))
        self.board.append([0,0,0,0,0,0,0,0])
        self.board.append([0,0,0,0,0,0,0,0])
        self.board.append([0,0,0,0,0,0,0,0])
        self.board.append([0,0,0,0,0,0,0,0])
        temporaryTab = []
        for i in range(8):
            temporaryTab.append(pon([6, i], 1))
        self.board.append(deepcopy(temporaryTab))
        self.board.append([rook([7, 0], 1),knight([7, 1], 1),bishop([7, 2], 1),queen([7,3], 1),king([7, 4], 1),bishop([7, 5], 1),knight([7, 6], 1),rook([7, 7], 1)])

class pon:
    def __init__(self, place, colour):
        self.currentPlace = place
        self.colour = colour
        self.symbol = 'p'
        if self.colour == 1:
            self.symbol = 'P'
    def moves(self, boardState, targetMove="check"):
        possibleMoves = []
        if self.colour == 1:
            if self.currentPlace[0] == 6 and boardState.board[5][self.currentPlace[1]] == 0 and boardState.board[4][self.currentPlace[1]] == 0:
                possibleMoves.append([4, self.currentPlace[1]])
            if self.currentPlace[0] == 3 and boardState.lastMove == ["p", [[self.currentPlace[0]-2, self.currentPlace[1]-1], [self.currentPlace[0], self.currentPlace[1]-1]]]:
                possibleMoves.append([self.currentPlace[0]-1, self.currentPlace[1]-1])
            if self.currentPlace[0] == 3 and boardState.lastMove == ["p", [[self.currentPlace[0]-2, self.currentPlace[1]+1], [self.currentPlace[0], self.currentPlace[1]+1]]]:
                possibleMoves.append([self.currentPlace[0]-1, self.currentPlace[1]+1])
        else:
            if self.currentPlace[0] == 1 and boardState.board[2][self.currentPlace[1]] == 0 and boardState.board[3][self.currentPlace[1]] == 0:
                possibleMoves.append([3, self.currentPlace[1]])
            if self.currentPlace[0] == 4 and boardState.lastMove == ["p", [[self.currentPlace[0]+2, self.currentPlace[1]-1], [self.currentPlace[0], self.currentPlace[1]-1]]]:
                possibleMoves.append([self.currentPlace[0]+1, self.currentPlace[1]-1])
            if self.currentPlace[0] == 4 and boardState.lastMove == ["p", [[self.currentPlace[0]+2, self.currentPlace[1]+1], [self.currentPlace[0], self.currentPlace[1]+1]]]:
                possibleMoves.append([self.currentPlace[0]+1, self.currentPlace[1]+1])
        if boardState.board[self.currentPlace[0]-self.colour][self.currentPlace[1]] == 0:
            possibleMoves.append([self.currentPlace[0]-self.colour, self.currentPlace[1]])
        if self.currentPlace[1] > 0:
            if boardState.board[self.currentPlace[0]-self.colour][self.currentPlace[1]-1] != 0:
                if boardState.board[self.currentPlace[0]-self.colour][self.currentPlace[1]-1].colour == -self.colour:
                    possibleMoves.append([self.currentPlace[0]-self.colour, self.currentPlace[1]-1])
        if self.currentPlace[1] < 7: 
            if boardState.board[self.currentPlace[0]-self.colour][self.currentPlace[1]+1] != 0:
                if boardState.board[self.currentPlace[0]-self.colour][self.currentPlace[1]+1].colour == -self.colour:
                    possibleMoves.append([self.currentPlace[0]-self.colour, self.currentPlace[1]+1])
        
        if targetMove == "check":
            return possibleMoves

class knight:
    def __init__(self, place, colour):
        self.currentPlace = place
        self.colour = colour
        self.symbol = 'n'
        if self.colour == 1:
            self.symbol = 'N'
    def moves(self, boardState, targetMove="check"):
        allPossibleMoves = []
        if self.currentPlace[0] > 1 and self.currentPlace[1] > 0:
            allPossibleMoves.append([self.currentPlace[0]-2, self.currentPlace[1]-1])
        if self.currentPlace[0] > 1 and self.currentPlace[1] < 7:
            allPossibleMoves.append([self.currentPlace[0]-2, self.currentPlace[1]+1])

        if self.currentPlace[0] < 6 and self.currentPlace[1] > 0:
            allPossibleMoves.append([self.currentPlace[0]+2, self.currentPlace[1]-1])
        if self.currentPlace[0] < 6 and self.currentPlace[1] < 7:
            allPossibleMoves.append([self.currentPlace[0]+2, self.currentPlace[1]+1])

        if self.currentPlace[0] > 0 and self.currentPlace[1] > 1:
            allPossibleMoves.append([self.currentPlace[0]-1, self.currentPlace[1]-2])
        if self.currentPlace[0] < 7 and self.currentPlace[1] > 1:
            allPossibleMoves.append([self.currentPlace[0]+1, self.currentPlace[1]-2])
            
        if self.currentPlace[0] > 0 and self.currentPlace[1] < 6:
            allPossibleMoves.append([self.currentPlace[0]-1, self.currentPlace[1]+2])
        if self.currentPlace[0] < 7 and self.currentPlace[1] < 6:
            allPossibleMoves.append([self.currentPlace[0]+1, self.currentPlace[1]+2])

        possibleMoves = []
        for i in allPossibleMoves:
            if boardState.board[i[0]][i[1]] == 0:
                possibleMoves.append(i)
            elif boardState.board[i[0]][i[1]].colour != self.colour:
                possibleMoves.append(i)

        if targetMove == "check":
            return possibleMoves

class bishop:
    def __init__(self, place, colour):
        self.currentPlace = place
        self.colour = colour
        self.symbol = 'b'
        if self.colour == 1:
            self.symbol = 'B'
    def moves(self, boardState, targetMove="check"):
        possibleMoves = []
        y = self.currentPlace[0]
        x = self.currentPlace[1]
        for i in range(1, 8):
            yy = deepcopy(y)-i
            xx = deepcopy(x)+i
            if yy >= 0 and xx <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)+i
            xx = deepcopy(x)+i
            if yy <= 7 and xx <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)+i
            xx = deepcopy(x)-i
            if yy <= 7 and xx >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)-i
            xx = deepcopy(x)-i
            if yy >= 0 and xx >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        
        if targetMove == "check":
            return possibleMoves

class rook:
    def __init__(self, place, colour):
        self.currentPlace = place
        self.colour = colour
        self.symbol = 'r'
        if self.colour == 1:
            self.symbol = 'R'
    def moves(self, boardState, targetMove="check"):
        possibleMoves = []
        y = self.currentPlace[0]
        x = self.currentPlace[1]
        for i in range(1, 8):
            yy = deepcopy(y)-i
            xx = deepcopy(x)
            if yy >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)+i
            xx = deepcopy(x)
            if yy <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            xx = deepcopy(x)-i
            yy = deepcopy(y)
            if xx >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            xx = deepcopy(x)+i
            yy = deepcopy(y)
            if xx <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        
        if targetMove == "check":
            return possibleMoves

class queen:
    def __init__(self, place, colour):
        self.currentPlace = place
        self.colour = colour
        self.symbol = 'q'
        if self.colour == 1:
            self.symbol = 'Q'
    def moves(self, boardState, targetMove="check"):
        possibleMoves = []
        y = self.currentPlace[0]
        x = self.currentPlace[1]
        for i in range(1, 8):
            yy = deepcopy(y)-i
            xx = deepcopy(x)
            if yy >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)+i
            xx = deepcopy(x)
            if yy <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            xx = deepcopy(x)-i
            yy = deepcopy(y)
            if xx >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            xx = deepcopy(x)+i
            yy = deepcopy(y)
            if xx <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
                y = self.currentPlace[0]
        for i in range(1, 8):
            yy = deepcopy(y)-i
            xx = deepcopy(x)+i
            if yy >= 0 and xx <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)+i
            xx = deepcopy(x)+i
            if yy <= 7 and xx <= 7:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)+i
            xx = deepcopy(x)-i
            if yy <= 7 and xx >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        for i in range(1, 8):
            yy = deepcopy(y)-i
            xx = deepcopy(x)-i
            if yy >= 0 and xx >= 0:
                if boardState.board[yy][xx] == 0:
                    possibleMoves.append([yy, xx])
                elif boardState.board[yy][xx].colour != self.colour:
                    possibleMoves.append([yy, xx])
                    break
                else:
                    break
        
        if targetMove == "check":
            return possibleMoves

class king:
    def __init__(self, place, colour):
        self.currentPlace = place
        self.colour = colour
        self.symbol = 'k'
        if self.colour == 1:
            self.symbol = 'K'
    def moves(self, boardState, targetMove="check"):
        y = deepcopy(self.currentPlace[0])
        x = deepcopy(self.currentPlace[1])

        xx = x-1
        xxx = x+1
        yy = y-1
        yyy = y+1

        allPossibleMoves = [[yy, xx],[yy, x],[yy, xxx],[y, xxx],[yyy, xxx],[yyy, x],[yyy, xx],[y, xx]]
        possibleMoves = []
        for i in allPossibleMoves:
            for j in range(2):
                if i[j] < 0 or i[j] > 7:
                    break
            else:
                if boardState.board[i[0]][i[1]] == 0:
                    possibleMoves.append(i)
                elif boardState.board[i[0]][i[1]].colour != self.colour:
                    possibleMoves.append(i)
        
        if targetMove == "JC":
            return possibleMoves

        if boardState.playerToMove == 1:
            pos = 7
        else:
            pos = 0
        if (boardState.board[pos][1] == 0 and boardState.board[pos][2] == 0 and boardState.board[pos][3] == 0) or (boardState.board[pos][5] == 0 and boardState.board[pos][6] == 0):
            toBreak = False
            for i in boardState.history:
                if i[0] == [pos, 4]:
                    toBreak = True
                    break
            else:
                tab = [i[0] for i in boardState.history if (i[0] == [pos, 0] or i[0] == [pos,7])]
            if toBreak:
                return possibleMoves
            if [pos,0] not in tab:
                cop = deepcopy(boardState)
                if move([pos,4], [pos,3], cop) != None:
                    if move([pos,4],[pos,2], cop) != None:
                        possibleMoves.append([pos,2])
            if [pos,7] not in tab:
                cop = deepcopy(boardState)
                if move([pos,4], [pos,5], cop) != None:
                    if move([pos,4],[pos,6], cop) != None:
                        possibleMoves.append([pos,6])
        return possibleMoves

def move(firstPlace, secondPlace, board):
    gameState = deepcopy(board)
    save = deepcopy(firstPlace)
    gameState.board[firstPlace[0]][firstPlace[1]].currentPlace = secondPlace
    gameState.board[secondPlace[0]][secondPlace[1]] = gameState.board[save[0]][save[1]]
    if gameState.board[secondPlace[0]][secondPlace[1]].symbol.lower() == "p":
        if gameState.playerToMove == 1 and gameState.lastMove == ["p", [[1, save[1]-1], [3, save[1]-1]]] and secondPlace == [2, save[1]-1]:
            gameState.board[3][save[1]-1] = 0
        elif gameState.playerToMove == 1 and gameState.lastMove == ["p", [[1, save[1]+1], [3, save[1]+1]]] and secondPlace == [2, save[1]+1]:
            gameState.board[3][save[1]+1] = 0
        elif gameState.playerToMove == -1 and gameState.lastMove == ["p", [[6, save[1]+1], [4, save[1]+1]]] and secondPlace == [5, save[1]+1]:
            gameState.board[4][save[1]+1] = 0
        elif gameState.playerToMove == -1 and gameState.lastMove == ["p", [[6, save[1]-1], [4, save[1]-1]]] and secondPlace == [5, save[1]-1]:
            gameState.board[4][save[1]-1] = 0
    if save == [max(0, gameState.playerToMove*7),4] and secondPlace == [max(0, gameState.playerToMove*7),2]:
        gameState.board[max(0, gameState.playerToMove*7)][0], gameState.board[max(0, gameState.playerToMove*7)][3] = 0, gameState.board[max(0, gameState.playerToMove*7)][0]
    elif save == [max(0, gameState.playerToMove*7),4] and secondPlace == [max(0, gameState.playerToMove*7),6]:
        gameState.board[max(0, gameState.playerToMove*7)][7], gameState.board[max(0, gameState.playerToMove*7)][5] = 0, gameState.board[max(0, gameState.playerToMove*7)][7]
    #if gameState.board[secondPlace[0]][secondPlace[1]].symbol.lower() == "p":
    #    if secondPlace[0] in [0, 7]:
    #        promotion = input("Promotion: ").lower()
    #        if promotion == "q":
    #            gameState.board[secondPlace[0]][secondPlace[1]] = queen([secondPlace[0], secondPlace[1]], gameState.board[secondPlace[0]][secondPlace[1]])
    #        elif promotion == "r":
    #            gameState.board[secondPlace[0]][secondPlace[1]] = rook([secondPlace[0], secondPlace[1]], gameState.board[secondPlace[0]][secondPlace[1]])
    #        elif promotion == "b":
    #            gameState.board[secondPlace[0]][secondPlace[1]] = bishop([secondPlace[0], secondPlace[1]], gameState.board[secondPlace[0]][secondPlace[1]])
    #        elif promotion == "n":
    #            gameState.board[secondPlace[0]][secondPlace[1]] = knight([secondPlace[0], secondPlace[1]], gameState.board[secondPlace[0]][secondPlace[1]])
    gameState.board[save[0]][save[1]] = 0
    gameState.lastMove = [gameState.board[secondPlace[0]][secondPlace[1]].symbol.lower(), [save, secondPlace]]
    gameState.playerToMove *= -1

    checkIfKingAttacked = []
    for i in range(8):
        for j in range(8):
            if gameState.board[j][i] != 0:
                if gameState.board[j][i].colour == gameState.playerToMove:
                    if gameState.board[j][i].symbol.lower() == "k":
                        checkIfKingAttacked += gameState.board[j][i].moves(gameState, "JC")
                    else:
                        checkIfKingAttacked += gameState.board[j][i].moves(gameState)
    for i in range(8):
        for j in range(8):
            if gameState.board[j][i] != 0:
                if gameState.board[j][i].colour == -gameState.playerToMove and gameState.board[j][i].symbol.lower() == "k":
                    kingPosition = [j, i]
    if kingPosition in checkIfKingAttacked:
        return None
    else:
        gameState.history.append([firstPlace, secondPlace])
        return gameState

board = boardStateClass()
board.createBoard()

preMoved = []
allColumns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
players = {-1: "Black", 1: "White"}

while True:
    print()
    print("Move of: {}".format(players[board.playerToMove]))
    print()
    board.printBoard()
    allLegalMoves = {}
    numberOfMoves = 0
    for i in range(8):
        for j in range(8):
            if board.board[i][j] != 0:
                if board.board[i][j].colour == board.playerToMove:
                    if board.board[i][j].symbol.lower() == "k":
                        allLegalMoves[i*8+j] = board.board[i][j].moves(board)
                    else:
                        allLegalMoves[i*8+j] = board.board[i][j].moves(board)
                    numberOfMoves += len(allLegalMoves[i*8+j])
    for i in list(allLegalMoves.keys()):
        numberOfMoves += len(allLegalMoves[i])
    
    checkIfKingAttacked = []
    gameState = deepcopy(board)
    gameState.playerToMove *= -1
    for i in range(8):
        for j in range(8):
            if gameState.board[j][i] != 0:
                if gameState.board[j][i].colour == gameState.playerToMove:
                    if gameState.board[j][i].symbol.lower() == "k":
                        checkIfKingAttacked += gameState.board[j][i].moves(gameState, "JC")
                    else:
                        checkIfKingAttacked += gameState.board[j][i].moves(gameState)
                if gameState.board[j][i].colour == -gameState.playerToMove and gameState.board[j][i].symbol.lower() == "k":
                    kingPosition = [j, i]
    gameState.playerToMove *= -1

    if kingPosition in checkIfKingAttacked and numberOfMoves == 0:
        print("Player {} has lost.".format(players[board.playerToMove]))
        break
    elif numberOfMoves == 0:
        print("Draw")
        break
    ans = False
    for i in list(allLegalMoves.keys()):
        for j in allLegalMoves[i]:
            if move([i//8, i%8], j, deepcopy(gameState)) != None:
                ans = True
                break
        if ans:
            break
    else:
        print("Player {} has lost.".format(players[board.playerToMove]))
        break
        

    while True:
        if len(preMoved) > 0:
            inp = preMoved[0]
            preMoved.pop(0)
            yx = inp[0:2]
            yyxx = inp[3:5]
            break
        inp = input()
        if len(inp) == 5:
            yx = inp[0:2]
            yyxx = inp[3:5] 
            break
        else:
            print("Input error")

    y = 8-int(yx[1])
    x = allColumns[yx[0].lower()]
    yy = 8-int(yyxx[1])
    xx = allColumns[yyxx[0].lower()]

    try:
        if [yy, xx] in allLegalMoves[y*8+x]:
            answer = move([y,x], [yy, xx], board)
            if answer != None:
                board = answer
        else:
            print("Illegal Move")
    except:
        print("Illegal Move")