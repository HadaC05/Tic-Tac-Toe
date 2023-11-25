
#import random so that we can have the computer player. Basically used in the single player mode. Because of this, the computer player can commit a move later in the game.
import random 

num_ingame = [1,2,3,4,5,6,7,8,9] #indicates the nunbers within the grid. This limits the player into having these set of numbers as the only valid number. otherwise, the terminal would show an invalid message.
game_board = [[1,2,3], [4,5,6], [7,8,9]] #an array that corresponds to the number within the grid to be modified as the player/s make/s their move. 
row = 3 #value as determinant for the game board
column = 3 #value as determinant for the game board

#define the gameboard to be used throughout the game. 
#this loops to make a three dimensional array
def printGameBoard():
    for x in range(row): #this iterate 3 t  imes
        print ("\n+---+---+---+") #important and \n dari dapit aron dili siya musunod sa line after ningbalik ang loop
        print("|", end="") #end= let's you print the next object in the same line
        for y in range(column): #prints out the number
            print("", game_board[x][y], end=" |") #x y to reference the points within the 2d array
    print ("\n+---+---+---+") #explain the \n backward slash

#printed as is. serves as the game interface
print ("\n\t\t TIC TAC TOE \n\t\t°˖✧◝(⁰▿⁰)◜✧˖° \n\n\tType START to begin single player game \n\tType TWO for two player mode \n\tType HELP to know how to play \n\tType QUIT to stop the game")

command = ""

while True:
    command = input(">> ").upper() #.upper() so that, even if dili naka uppercase ang giinput ni user, is ginabasa siya as it would if it were in uppercase.
    if command == "START":
        player_one = input("\tPlayer 1 \nEnter your name: ")
        print (f"\n{player_one}, you'll play as X")

        printGameBoard #prints the gameboard as we had defined ahead

        def modifyArray(num, turn): #supposedly modifies array. this helps avoid repetition of input by user or computer. it does not overlap
            #num is actually what the player will input
            num -= 1 #since index starts at 0. 
            if(num == 0):
                game_board[0][0] = turn #turn refers to the player's role, whether it is X or O that's going to replace the number 
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


        def checkForWinner(game_board): #looks overwhelming, but it is simply the combinations of winning patterns and the tie combi.
            # X axis
            if(game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X'):
                print("\nX has won! (/￣w￣)/‥∵:*:☆*゜★")
                return "X"
            elif(game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O'):
                print("\nO has won! (ﾉ >ω<)ﾉ :｡･:*:･ﾟ’★")
                return "O"
            elif(game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X'):
                print("\nX has won! (/￣w￣)/‥∵:*:☆*゜★")
                return "X"

            #no winners yet
            else:
                return "N"
        

        #the actual game

        leaveLoop = False
        turnCounter = 0

        while(leaveLoop == False):
            # It's the player turn
            try: #Try and Except function. If not used, the code would result to a ValueError which happens when the a function or operation anticipates a specific object or value.
                if(turnCounter % 2 == 0):
                    printGameBoard()
                    numberPicked = int(input(f"\n{player_one}, choose a number [1-9]: "))
                    if(numberPicked >= 1 or numberPicked <= 9):
                        modifyArray(numberPicked, 'X') #it will change what was on the board from the number picked into X or whatever role you have
                        num_ingame.remove(numberPicked) #to keep track of what numbers are picked and had already been picked. the numberPicked will be removed from the array. so that if inputted again, it will result to an invalid message.
                    turnCounter += 1
            except:
                print("\nInvalid input. Please try again.")
            
            winner = checkForWinner(game_board)
            if(winner != "N"):
                print("\nGame over! Thank you for playing ✺◟(-^〇^-)◞✺")
                break
            elif (winner == "T"):
                print ("\nIt's a tie! o(≧◇≦)o")

            # It's the computer's turn
            else:
                while(True):
                    cpuChoice = random.choice(num_ingame) #the imported module is used here. the computer chooses a random number within the possibleNumbers array
                    print("\nCpu choice: ", cpuChoice)
                    if(cpuChoice in num_ingame):
                        modifyArray(cpuChoice, 'O')
                        num_ingame.remove(cpuChoice)
                        turnCounter += 1
                        break
            #there is no chances that the cpu will pick an already chosen number since numbers already used had already been removed from the possibleNumbers array

            #in order to check the winner, the define function to checkforwiiner will be used. 
            winner = checkForWinner(game_board)
            if(winner != "N"):
                print("\nGame over! Thank you for playing ✺◟(-^〇^-)◞✺")
                break
            elif (winner == "T"):
                print ("\nIt's a tie! o(≧◇≦)o")
        
    elif command == "TWO":
        player_one = input("\tPlayer 1 \nEnter your name: ")
        print (f"{player_one} will play as X")
        player_two = input ("\n\tPLayer 2 \nEnter your name: ")
        print (f"{player_two} will play as O")
        print (f"\n{player_one} moves first")
        
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

        def checkForWinner(game_board):
            # X axis
            if(game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X'):
                print("\nX has won! (/￣w￣)/‥∵:*:☆*゜★")
                return "X"
            elif(game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O'):
                print("\nO has won! (ﾉ >ω<)ﾉ :｡･:*:･ﾟ’★")
                return "O"

            
            #tie
            if(game_board[0][0]  == 'O' and game_board[0][1] == 'X' and game_board[0][2] == 'O' and game_board[1][0] == 'X' and game_board[1][1] == 'O' and game_board[1][2] == 'X' and game_board[2][0] == 'X' and game_board[2][1] == 'O' and game_board[2][2] == 'X'):
                print ("\nIt's a tie! (￣ω￣;)")
                return "T"

            
            #no winners yet
            else:
                return "N"
        
        leaveLoop = False
        turnCounter = 0

        while(leaveLoop == False):
            # It's the player turn
            try:
                if(turnCounter % 2 == 0):
                    printGameBoard()
                    numberPicked = int(input(f"\n{player_one}, choose a number [1-9]: "))
                    if(numberPicked >= 1 or numberPicked <= 9):
                        modifyArray(numberPicked, 'X')
                        num_ingame.remove(numberPicked)
                    turnCounter += 1
            except:
                print("\nInvalid input. Please try again.")
            
            winner = checkForWinner(game_board)
            if(winner != "N"):
                print("\nGame over! Thank you for playing ✺◟(-^〇^-)◞✺")
                break
            elif (winner == "T"):
                print ("\nIt's a tie! o(≧◇≦)o")

            # It's the other player's turn
            try:
                if(turnCounter % 2 != 0):
                    printGameBoard()
                    numberPicked = int(input(f"\n{player_two}, choose a number [1-9]: "))
                    if(numberPicked >= 1 or numberPicked <= 9):
                        modifyArray(numberPicked, 'O')
                        num_ingame.remove(numberPicked)
                    turnCounter += 1
            except:
                print("\nInvalid input. Please try again.")
            
            winner = checkForWinner(game_board)
            if(winner != "N"):
                print("\nGame over! Thank you for playing ✺◟(-^〇^-)◞✺")
                break
            elif (winner == "T"):
                print ("\nIt's a tie! o(≧◇≦)o")
                break

#Straighforward lang na operation ni part
    elif command == "HELP":
        print ("\nSingle Player Game: \n\tThe player and the computer will decide whether to be X or O. \n\tThe two players will take turn putting their mark on the 3x3 grid. \n\tThe first player to put 3 marks in a row, up, down, or diagnoally, will be the winner.")
        print ("\nTwo Player Game: \n\tSame rule as the single player game, but now your enemy has the brain to beat you in the game. lol")
        print ("\tGood Luck! ( ๑ ˃̵ᴗ˂̵)و ")

#Serves no purpose other than mimic an actual game. estitik lang aron ignon murag game app jud siya
    elif command == "QUIT":
        quit_game = input("Do you want to exit? (Y/N) ").upper()
        if quit_game == "Y":
            print ("Thank you for checking out the game! \n\t(・ε・｀)")
        elif quit_game == "N":
           continue

#in case the user inputs anything that wasn't indicated    
    else:
        print ("You seem to have entered the wrong command, try again. \n\t\t(º﹃º)...")
