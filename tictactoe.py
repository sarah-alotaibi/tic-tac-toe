import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board [0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board [3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board [6] + "|" + board[7] + "|" + board[8])
    print("------")

def playerInput(board):
    inp = int(input("enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer

    else:
        print("theres a player in that spot!")


# check for win or tie 
def chechHorizontle(board): 
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True 
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
         winner = board[0]
         return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
         winner = board[2]
         return True
    
  

def chechTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("its a tie!") 
        gameRunning = False


def checkWin():
    if checkDiag(board) or chechHorizontle(board) or checkRow(board):
        print(f"the winner is {winner}")



def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"     


#computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


    

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    chechTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    chechTie(board)


