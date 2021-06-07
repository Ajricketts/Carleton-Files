# ============================================================
#
# Student Name (as it appears on cuLearn): Alyxander-Jacob Ricketts
# Student ID (9 digits in angle brackets): <101084146>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

"""
This Function provides the description of the program for the user.
@params                     None
@return                     None
"""
def description():
    # Print out a short description of the program.
    print("\nThis program enables the user to input the current state of a chessboard.")
    print("Once a current state is loaded multiple other functions can be performed.")
    print("Such as moving a peice and calculating the score.")


"""
This Function provides instructions for the user.
@params                     None
@return                     None
"""
def instructions():

    # Print out the instructions on how to use the program to the user.
    print("To input the current state of a chessboard you will be inputing the chessboard row by row.")
    print("With the character \"-\" as the blank spaces. ")
    print("The peices should be filled in as k for King, q for Queen, r for Rook")
    print("n for Knight, b for Bishop and p for Pawn.")
    print("When you type those charecters in lowercase that signifies those peices are on the white team.")
    print("When you type those chatecters in uppercase that signifies those peices are on the black team.")
    print("Please make your rows 8 characters as the program will return an error")
    print("Input the number 5 into the terminal while on the menu to quit.")

"""
This Function provides a way for the user to type in the current state of a
chessboard

@params                     None
@return                     chessboard, the completed chessboard with the pecies
                            in the places the user specified as well as blank spaces.
"""
def createBoard():
    x = 8
    y = 8
    count = 0
    # Create an empty list that will house our chessboard.
    chessboard = []
    # Loop through each row
    while True:
        if count < 8:
            temp_list = []
            row = input("Please input the current state of Row #%s: " % str(count + 1)) # get the row state from the user
            if len(row) != 7:
                temp_list.append(row) # add this row to the temporary list
                chessboard.append(temp_list) # add that list to the chessboard
                count += 1
            else:
                # Print this error message if the user typed in something longer than 8 characters.
                print("The length of the row was shorter or longer than 8 characters, please retype this row.")
        else:
            break
    print(chessboard)
    # Print the chessboard
    for i in chessboard: # Loop through the chessboard list (List of Lists)
        for j in i: # Loop through the inner list
            print(j, end='') # Print each list to the terminal
        print() # Move down to a new line for the next list.

    calculateScore(chessboard)
    return chessboard


"""
This Function calculates the score of the white team and the score of the black team.
Then reports who's winnig.

@params                     chessboard, this is the loaded in chessboard which has
                            all the peices on it.

@return                     The team that is winning.
"""
def calculateScore(chessboard):
    # Values of pecies
    values = [0.0, 10.0, 5.0, 3.5, 3.0, 1.0]

    # The score of each team.
    white_score = 0
    black_score = 0

    # Loop through the chessboard, the each list in chessboard, and then each element in each list.
    for i in chessboard:
        for k in i:
            for j in k:
                # Check to see an element in each list equals any of these characters.
                if j == "K":
                    # If it does, add the appropriate value to the score of the appropriate team.
                    black_score += values[0]
                elif j == "Q":
                    black_score += values[1]
                elif j == "B":
                    black_score += values[4]
                elif j == "N":
                    black_score += values[3]
                elif j == "R":
                    black_score += values[2]
                elif j ==  "P":
                    black_score += values[5]


                if j == "k":
                    white_score += values[0]
                elif j == "q":
                    white_score += values[1]
                elif j == "b":
                    white_score += values[4]
                elif j == "n":
                    white_score += values[3]
                elif j == "r":
                    white_score += values[2]
                elif j ==  "p":
                    white_score += values[5]

    # Display the score of each team
    print("\nBlack score: " + str(black_score), "White score: " + str(white_score))

    if black_score > white_score:
        return print("The black team is winning!") # Display this message if the white team is winning.
    elif black_score == white_score:
        return print("The match is tied at the moment!") # Display this message if it is a tie.
    else:
        return print("The white team is winning!") # Display this message if the white team is winning.

"""
This Function moves a peice from one place on the board to another.

@params                     chessboard, this is the loaded in chessboard which has
                            all the peices on it.

@return                     A print out of the current state of the board.
"""
def movePiece(chessboard):
    # Ask the user for a x and y position
    y_position = int(input("Enter an y position of the chess peice (A number 1-8): "))
    x_position = int(input("Enter an x position of the chess peice (A number 1-8): "))

    # If the position of the chesspeice given is invalid or there is no chess peice there
        # an error will print and they will be brought back to the menu.
    if (x_position > 8 or y_position > 8) or (x_position < 0 or y_position < 0): # If the position is less than 0 or greater than 8 print this error.
        print("That is not a valid location. Please select this option again and try again.")
    elif chessboard[y_position - 1][x_position - 1] == "-": # If there is no peice at this position then print this error
        print("There is no peice at that location. Please select this option again and try again.")

    else: # If the position is valid and there is a peice there then move the peice to the new location.
        new_y = int(input("\nEnter a new y position for the chess peice (A number 1-8): "))
        new_x = int(input("Enter a new x position for the chess peice (A number 1-8): "))
        chessboard[new_y - 1][new_x - 1] = chessboard[y_position - 1][x_position - 1]
        chessboard[y_position - 1][x_position - 1] = "-"
        print()

    # Print the chessboard
    for i in chessboard: # Loop through the chessboard list (List of Lists)
        for j in i: # Loop through the inner list
            print(j, end='') # Print each list to the terminal
        print() # Move down to a new line for the next list.

'''
This function displays a menu bar.
@params             none
@return             none
'''

def menu_bar():
    # Display a menu bar
    print("\n\t###################################################################")
    print("\t############################  MENU  ###############################")
    print("\t###################################################################\n")

'''
This function displays the menu.
@params             none
@return             none
'''

def menu():
    menu_bar()
    # Display a menu to the user, with each option numbered
    print("What would you like to do?\n")
    print("[1] Read the description of the program.")
    print("[2] Read the instructions.")
    print("[3] Enter in the current state of a chessboard.")
    print("[4] Move a Peice.")
    print("[5] Quit")

    selection = input("> ") # Take the selection from the user.
    return selection



'''
This is the main function, responsible for the user interface.

@params             none
@return             none
'''
def main():
    chessboard = [["-", "-", "-", "-", "-", "k", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "n", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "n", "-", "-", "-", "-"], ["-", "-", "-", "-", "K", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "Q", "-", "-", "-", "-"]]

    # See what the option the user selects and run the proper function.
    # This is in a loop to allow the user to perform one function and then keep using the program.
    while True:
        selection = menu()
        if selection == "1":
            description()
        elif selection =="2":
            instructions()
        elif selection == "3":
            createBoard()
        elif selection == "4":
            movePiece(chessboard)
        elif selection == "5":
            break # The program will end when the user selects option 6 "Quit".
        else:
            # If the user inputs another number that is not 1 through 6 then return this error
                # so they can make another selection.
            print("That is not a valid option, please make another selection.")






main() # Run the program.
