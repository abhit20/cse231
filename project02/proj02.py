##################################################################
#  CSE 231 Project 2
#
#   Asks to begin the game
#
#       Begins with player's turn
#       Asks to choose from one of two piles of 5 stones each
#       Asks how many stones to remove from each
#       Algorithm subtracts specified number of stones from the pile
#
#       Computer's turn
#       Removes one stone from the pile not specified by the player unless that pile is 0
#
#       Whoever goes last is the winner
####################################################################

# Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

#Declares and initializes variables to keep track of player and computer score
global player_score, computer_score
player_score = 0
computer_score = 0

#Prompts the user if they would like to play
play_str = input("Would you like to play? (0=no, 1=yes) ")

#Starts the game if play_str is 1
while int(play_str) != 0:
    #Initializes the variables for the game
    pile_1 = 5
    pile_2 = 5
    player_turn = True
    game_over = False

    #Prints the initial number of stones in each pile
    print("Start --> Pile 1: 5    Pile 2: 5")

    #Runs until game is over
    while not game_over:

            #Game always begins with the human. Player's turn
            if player_turn == True:
                #Prompt for number of stones
                choose_pile = int(input("Choose a pile (1 or 2):"))

                #Player_pile is equal to the pile chosen
                if choose_pile == 1 and pile_1 !=0:
                    player_pile = pile_1
                elif choose_pile == 2 and pile_2 !=0:
                    player_pile = pile_2
                elif choose_pile == 1 and pile_1 == 0:
                    #Prints the folowing statement when the users inputs numbers other than 1 or 2
                    print(" Pile must be 1 or 2 and non-empty. Please try again.")
                    #choose_pile_again is a function that runs the choose pile part again if the user inputted irrelevant numbers
                    def choose_pile_again():
                        if player_turn == True:
                            # Prompt for number of stones
                            global choose_pile
                            choose_pile = int(input("Choose a pile (1 or 2):"))
                            # Player_pile is equal to the pile chosen
                            if choose_pile == 1:
                                global player_pile
                                player_pile = pile_1
                            elif choose_pile == 2:
                                player_pile = pile_2
                    choose_pile_again()
                elif choose_pile == 2 and pile_2 == 0:
                    print(" Pile must be 1 or 2 and non-empty. Please try again.")
                    # choose_pile_again is a function that runs the choose pile part again if the user inputted irrelevant numbers
                    def choose_pile_again():
                        if player_turn == True:
                            # Prompt for number of stones
                            global choose_pile
                            choose_pile = int(input("Choose a pile (1 or 2):"))
                            # Player_pile is equal to the pile chosen
                            if choose_pile == 1:
                                global player_pile
                                player_pile = pile_1
                            elif choose_pile == 2:
                                player_pile = pile_2
                    choose_pile_again()
                else:
                    #If a different pile is chosen other than 1 or 2. User is prompted to choose again
                    print(" Pile must be 1 or 2 and non-empty. Please try again.")
                    # choose_pile_again is a function that runs the choose pile part again if the user inputted irrelevant numbers
                    def choose_pile_again():
                        if player_turn == True:
                            # Prompt for number of stones
                            global choose_pile
                            choose_pile = int(input("Choose a pile (1 or 2):"))
                            # Player_pile is equal to the pile chosen
                            if choose_pile == 1:
                                global player_pile
                                player_pile = pile_1
                            elif choose_pile == 2:
                                player_pile = pile_2
                    choose_pile_again()

                # Prompt for number of stones
                choose_stones = int(input(" Choose stones to remove from pile:"))

                # Remove the number of stones chosen from the chosen pile
                player_pile = player_pile-choose_stones

                #Prints the player's choice in one statement
                print(" Player -> Remove",choose_stones,"stones from pile", choose_pile)

                #Changes the pile to reflect the removed stones
                if choose_pile == 1:
                    pile_1 = player_pile
                else:
                    pile_2 = player_pile

                #Prints the number of stones in each pile after player's turn
                print("Pile 1:", pile_1, "   Pile 2:", pile_2)

            #Ends the game if both piles reach 0 and prints the results. Else goes to computer turn
            if pile_1 == 0 and pile_2 == 0:
                game_over = True
                player_score = player_score+1
                print("\nPlayer wins!")
                print("Score -> human:",player_score,"; computer:",computer_score)
            else:
                player_turn = False

            #Computer's turn
            if player_turn == False:
                #Chooses the pile not choosen by the player or selects the pile with more than 0 stones
                if choose_pile == 2 and pile_1 == 0:
                    computer_pile = pile_2
                elif choose_pile == 1 and pile_2 ==0:
                    computer_pile = pile_1
                elif choose_pile == 1 and pile_2 !=0:
                    computer_pile = pile_2
                else:
                    computer_pile = pile_1

                #Removes one stone from the computer_pile
                remove_stone_computer = computer_pile - 1

                # Changes the pile to reflect the removed stones
                if choose_pile == 2 and pile_1 == 0:
                    pile_2 = remove_stone_computer
                elif choose_pile == 1 and pile_2 ==0:
                    pile_1 = remove_stone_computer
                elif choose_pile == 1 and pile_2 !=0:
                    pile_2 = remove_stone_computer
                else:
                    pile_1 = remove_stone_computer

                # The computer_pile_number is equal to the pile number selected by the computer
                if choose_pile == 2 and pile_1 == 0:
                    computer_pile_number = "2"
                elif choose_pile == 1 and pile_2 ==0:
                    computer_pile_number = "1"
                elif choose_pile == 1 and pile_2 !=0:
                    computer_pile_number = "2"
                else:
                    computer_pile_number = "1"

                #Prints the computer's action in one statement
                print("Computer -> Remove 1 stones from pile", computer_pile_number)

                # Prints the number of stones in each pile after computer's turn
                print("Pile 1:", pile_1, "   Pile 2:", pile_2)

            # Ends the game if both piles reach 0 and prints the results. Else goes to player turn
            if player_turn==False and pile_1 == 0 and pile_2 == 0:
                game_over = True
                computer_score=computer_score+1
                print("\nComputer wins!")
                print("Score -> human:", player_score, "; computer:", computer_score)
            else:
                player_turn = True;

    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")


else:
    print("\nThanks for playing! See you again soon!")
