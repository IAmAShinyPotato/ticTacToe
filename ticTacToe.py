# tic tac toe - now with 2x the protein

# module used for bot movements
import random

"""

board is set up like this

1 | 2 | 3
4 + 5 + 6
7 | 8 | 9

10 is used as a variable to see if user quits

"""

gameBoard = {
    "1": ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ', '10': ' '
}


# function to print the gameBoard
def board():
    print("""
Board Layout:
1|2|3
-----
4|5|6
-----
7|8|9

""")

    print(gameBoard['1'] + '|' + gameBoard['2'] + '|' + gameBoard['3'])
    print("------")
    print(gameBoard['4'] + '|' + gameBoard['5'] + '|' + gameBoard['6'])
    print("------")
    print(gameBoard['7'] + '|' + gameBoard['8'] + '|' + gameBoard['9'])


# takes a list and clears the screen
def clearScreen():
    screenLines = list(range(0, 100))
    for _ in screenLines:
        print("")


# func to determine if a space is empty
def emptySpace(position):
    if gameBoard[str(position)] == ' ':
        return True
    else:
        return False


# function to place down X on X's turn
def xTurn():
    while True:

        xMove = input("Where would you like to move, X? ")

        # checking if move is valid
        if xMove.isdigit():
            if emptySpace(int(xMove)):
                gameBoard[xMove] = 'X'
                return
        elif xMove == "q" or "quit":
            gameBoard["10"] = 'q'
            break
        else:
            print("That is not a valid option")


# function to place down O on O's turn
def oTurn():
    while True:

        oMove = input("Where would you like to move, O? ")

        # checking if move is valid
        if oMove.isdigit():
            if emptySpace(int(oMove)):
                gameBoard[oMove] = 'O'
                return
        elif oMove == "q" or "quit":
            gameBoard["10"] = 'q'
            break
        else:
            print("That is not a valid option")


# randomly chooses an empty box
def easyCompMove():
    while True:

        # create rand integer
        easyCompAttempt = random.randint(1, 10)

        # check if spot is taken
        if gameBoard[str(easyCompAttempt)] == ' ':
            gameBoard[str(easyCompAttempt)] = "O"
            return
        else:
            continue


# func to see if y wins
def oWin():
    # Checking for "O" win conditions
    if gameBoard['1'] == "O" and gameBoard['2'] == "O" and gameBoard['3'] == "O":
        return True
    elif gameBoard['4'] == "O" and gameBoard['5'] == "O" and gameBoard['6'] == "O":
        return True
    elif gameBoard["7"] == "O" and gameBoard["8"] == "O" and gameBoard["9"] == "O":
        return True
    elif gameBoard["1"] == "O" and gameBoard["4"] == "O" and gameBoard["7"] == "O":
        return True
    elif gameBoard["2"] == "O" and gameBoard["5"] == "O" and gameBoard["8"] == "O":
        return True
    elif gameBoard["3"] == "O" and gameBoard["6"] == "O" and gameBoard["9"] == "O":
        return True
    elif gameBoard["1"] == "O" and gameBoard["5"] == "O" and gameBoard["9"] == "O":
        return True
    elif gameBoard["3"] == "O" and gameBoard["5"] == "O" and gameBoard["7"] == "O":
        return True


# func to see if x wins
def xWin():
    if gameBoard["1"] == "X" and gameBoard["2"] == "X" and gameBoard["3"] == "X":
        return True
    elif gameBoard["4"] == "X" and gameBoard["5"] == "X" and gameBoard["6"] == "X":
        return True
    elif gameBoard["7"] == "X" and gameBoard["8"] == "X" and gameBoard["9"] == "X":
        return True
    elif gameBoard["1"] == "X" and gameBoard["4"] == "X" and gameBoard["7"] == "X":
        return True
    elif gameBoard["2"] == "X" and gameBoard["5"] == "X" and gameBoard["8"] == "X":
        return True
    elif gameBoard["3"] == "X" and gameBoard["6"] == "X" and gameBoard["9"] == "X":
        return True
    elif gameBoard["1"] == "X" and gameBoard["5"] == "X" and gameBoard["9"] == "X":
        return True
    elif gameBoard["3"] == "X" and gameBoard["5"] == "X" and gameBoard["7"] == "X":
        return True


# check for draws
def drawCheck():
    # this is dumb // checks if all keys are filled for a tie
    if gameBoard['1'] == ' ' or gameBoard['2'] == ' ' or gameBoard['3'] == ' ' or gameBoard['4'] == ' ' or gameBoard['5'] == ' ' or gameBoard['6'] == ' ' or gameBoard['7'] == ' ' or gameBoard['8'] == ' ' or gameBoard['9'] == ' ':
        return False
    else:
        return True


# main function that calls all other functions
def ticTacToe():

    print("Welcome to Tic-Tac-Toe!\n\n")
    print("Enter 'q' or 'quit' at any time to quit.")

    # init variables
    moveCount = 0
    turn = "X"
    win = False

    # creating two loops for the ability to replay
    while True:

        while True:
            gamemode = input("""
How would you like to play?
1.) Player v. Player
2.) Easy Bot       
""")
            if gamemode == '1' or '2':
                break
            elif gamemode == 'q' or 'quit':
                return
            else:
                print("That's not a valid input.")

        # game logic
        while True:
            clearScreen()
            board()
            print(f"It's {turn}'s turn.")

            if turn == "X":
                xTurn()
                moveCount += 1
            elif turn == "O" and gamemode == '1':
                oTurn()
                moveCount += 1
            else:
                easyCompMove()
                moveCount += 1

            # checking if player quits
            if gameBoard['10'] == "q":
                return

            # o win conditions
            if oWin() is True:
                win = True

            # "X" Win Conditions
            if xWin() is True:
                win = True

            # checking for ties
            if drawCheck() is True:
                clearScreen()
                board()
                print("You have tied the game.")
                break

            # printing if there is a winner
            if win:
                clearScreen()
                board()
                print(f"Congratulations! {turn} has won. They won in {moveCount} moves.")
                break

            # switching sides
            if turn == "X":
                turn = "O"
            else:
                turn = "X"

        # set in a loop in case of faulty user input
        while True:
            replayOption = input("Would you like to play again? (y/n) ")
            if replayOption == "y":

                # clearing board and variables for replay
                for spot in gameBoard:
                    gameBoard[spot] = ' '
                moveCount = 0
                turn = "X"
                win = False
                clearScreen()
                break

            # exits if player says no
            elif replayOption == "n":
                return
            else:
                print("That's not an option.")


ticTacToe()

print("end")

