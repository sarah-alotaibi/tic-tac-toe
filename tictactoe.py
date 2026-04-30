import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board [0] + "|" + board[1] + "|" + board[2])
    # print("------")
    print(board [3] + "|" + board[4] + "|" + board[5])
    # print("------")
    print(board [6] + "|" + board[7] + "|" + board[8])
    # print("------")

def playerInput(board):
    inp = int(input("enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("there\'s a player in that spot!")


# check for win or tie 
def chechHorizontal( board ):
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
    
def checkColumn( board ):
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
    global gameRunning
    if checkDiag(board) or chechHorizontal( board ) or checkColumn( board ):
        print(f"the winner is {winner}")
        gameRunning = False



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




def run_game_1() :
    while gameRunning :
        printBoard( board )
        playerInput( board )
        checkWin()
        chechTie( board )
        switchPlayer()
        computer( board )
        checkWin()
        chechTie( board )


def computer_2( board ) :
    while True :
        position = random.randint( 0, 8 )
        if board[ position ] == "-":
            board[ position ] = "O"

            break


def run_game_2() :
    while gameRunning :
        # One iteration per one move - human's or computer's.

        printBoard( board )

        if currentPlayer == 'X' :
            playerInput( board )
        elif currentPlayer == 'O' :
            print( '\nComputer:' )
            computer_2( board )
        else :
            print( 'error : current player symbol is not X or O' )

            break

        checkWin()
        chechTie( board )
        switchPlayer()

    printBoard( board )


if __name__ == '__main__' :
    run_game_1()
    # run_game_2()


