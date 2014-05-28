#Tic Tac Toe

import random

def drawBoard(board):
    #this function prints out the board it was passed

    #"board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    #let player choose which letter they want to be.
    #returns a list with the player's letter as the first item, and computers letter as the second letter
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    #the 1st element in the tuple is the player's letter, the 2nd is the computer's letter
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #randomly choose the player who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #this function returns True if the player wants to play again, otherwise False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #given a board and a player's letter, this function returns True if that player has won.
    #We use bo instead of board and le instead of letter so we don't have to type as much.
    return (
    (bo[7] == le and bo[8] == le and bo[9] == le) or    #across top
    (bo[4] == le and bo[5] == le and bo[6] == le) or    #across middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or    #across bottom

    (bo[1] == le and bo[4] == le and bo[7] == le) or    #down left
    (bo[2] == le and bo[5] == le and bo[8] == le) or    #down middle
    (bo[3] == le and bo[6] == le and bo[9] == le) or    #down right

    (bo[1] == le and bo[5] == le and bo[9] == le) or    #diagonal
    (bo[3] == le and bo[5] == le and bo[7] == le))      #diagonal

def getBoardCopy(board):
    #make a duplicate of board list and return the duplicate
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

#checks if it is a valid move
def isSpaceFree(board, move):
    #return true if the passed move is free on the passed board
    return board[move] == ' '

def getPlayerMove(board):
    #let the player type in his move
    move = ' ' 
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #returns a valid move from the passed lsit on the passed board
    #returns None if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    #check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7,9])
    if move != None:
        return move

    #try to take center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    #move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    #reset the board
    theBoard = [' '] * 10
    
    for i in len(theBoard):
        theBoard

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
