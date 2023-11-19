#decide wether to have a program that plays with the computer or to thave a system with two players.
#if single player mode: player decides whether they play as X or O. Player X always come first.
#game should have: player X and player O
#make a game board
#
#make a system that shows the winner
#make the game restart if player wants to

import random 


print ("\n\t\tTIC TAC TOE \n\tType START to begin single player game \n\tType TWO for two player mode \n\tType HELP to know how to play \n\tType QUIT to stop the game")

command = ""

while True:
    command = input(">> ").upper()
    if command == "START":
        player_one = input("\tPlayer 1 \nEnter your name: ")
        print (f"{player_one}, you'll play as X")
        
        #board

        num_ingame = [1,2,3,4,5,6,7,8,9]
        game_board = [[1,2,3], [4,5,6], [7,8,9]]
        row = 3
        column = 3

        def printGameBoard():
            for x in range(row):
                print ("\n+---+---+---+")
                print("|", end="")
                for y in range(column):
                    print("", game_board[x][y], end=" |")
            print ("\n+---+---+---+")
        
        printGameBoard
        
        def modifyArray(num, turn):
            num -= 1
            if(num == 0):
                game_board[0][0] = turn
            elif(num == 1):
                game_board[0][1] = turn
            elif(num == 2):
                game_board[0][2] = turn
            elif(num == 3):
                game_board[1][0] = turn
            elif(num == 4):
                game_board[1][1] = turn
            elif(num == 5):
                game_board[1][2] = turn
            elif(num == 6):
                game_board[2][0] = turn
            elif(num == 7):
                game_board[2][1] = turn
            elif(num == 8):
                game_board[2][2] = turn

        ### Define function to check for a winner
        def checkForWinner(game_board):
            ### X axis
            if(game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O'):
                print("O has won!")
                return "O"
            elif(game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[1][0] == 'O' and game_board[1][1] == 'O' and game_board[1][2] == 'O'):
                print("O has won!")
                return "O"
            elif(game_board[2][0] == 'X' and game_board[2][1] == 'X' and game_board[2][2] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[2][0] == 'O' and game_board[2][1] == 'O' and game_board[2][2] == 'O'):
                print("O has won!")
                return "O"
            ### Y axis
            if(game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[0][0] == 'O' and game_board[1][0] == 'O' and game_board[2][0] == 'O'):
                print("O has won!")
                return "O"
            elif(game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[0][1] == 'O' and game_board[1][1] == 'O' and game_board[2][1] == 'O'):
                print("O has won!")
                return "O"
            elif(game_board[0][2] == 'X' and game_board[1][2] == 'X' and game_board[2][2] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[0][2] == 'O' and game_board[1][2] == 'O' and game_board[2][2] == 'O'):
                print("O has won!")
                return "O"
            ### Cross wins
            elif(game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X'):
                print("X has won!")
                return "X"
            elif(game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O'):
                print("O has won!")  
                return "O"
            elif(game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X'):
                print("X has won!")  
                return "X"
            elif(game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O'):
                print("O has won!") 
                return "O" 
            else:
                return "N"
        
        leaveLoop = False
        turnCounter = 0

        while(leaveLoop == False):
        ### It's the player turn
            if(turnCounter % 2 == 0):
                printGameBoard()
                numberPicked = int(input("\nChoose a number [1-9]: "))
                if(numberPicked >= 1 or numberPicked <= 9):
                    modifyArray(numberPicked, 'X')
                    num_ingame.remove(numberPicked)
                else:
                    print("Invalid input. Please try again.")
                turnCounter += 1
            ### It's the computer's turn
            else:
                while(True):
                    cpuChoice = random.choice(num_ingame)
                    print("\nCpu choice: ", cpuChoice)
                    if(cpuChoice in num_ingame):
                        modifyArray(cpuChoice, 'O')
                        num_ingame.remove(cpuChoice)
                        turnCounter += 1
                        break
            
            winner = checkForWinner(game_board)
            if(winner != "N"):
                print("\nGame over! Thank you for playing :)")
                break
        
    elif command == "TWO":
        player_one = input("\tPlayer 1 \nEnter your name: ")
        print (f"{player_one} will play as X")
        player_two = input ("\tPLayer 2 \nEnter your name: ")
        print (f"{player_two} will play as O")
        print (f"\n{player_one} moves first")
        printGameBoard()
        #game should start
    elif command == "HELP":
        print ("Single Player Game: \n\tThe player and the computer will decide whether to be X or O. \n\tThe two players will take turn putting their mark on the 3x3 grid. \n\tThe first player to put 3 marks in a row, up, down, or diagnoally, will be the winner.")
        print ("Two Player Game: \n\tSame rule as the single player game, but now your enemy has the brain to beat you in the game. lol")
        print ("\tGood Luck! ( ๑ ˃̵ᴗ˂̵)و ")
    elif command == "QUIT":
        quit_game = input("Do you want to end game? (Y/N) ").upper()
        if quit_game == "Y":
            print ("Thank you for playing the game! \n\t(・ε・｀)")
        elif quit_game == "N":
           continue
    else:
        print ("You seem to have entered the wrong command, try again. \n\t\t(º﹃º)...")

