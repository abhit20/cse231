##################################################################
#  CSE 231 Project 4
#  Rolls two dice and get the sum of the dice
#
#       If sum is 7 or 11 on first roll, player wins
#       If sum is 2, 3, or 12 on first roll, player loses
#       If sum is 4, 5, 6, 8, 9, or 10 first roll, it becomes player point
#
#       Must keep rolling until the dice sum is equal to player point
#       If sum dice is 7 before it equals player point, player loses
#
####################################################################

#from random import randint  # the real Python random
from cse231_random import randint  # the cse231 test random for Mimir testing

#Displays game rules
def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

#Prompts the user to input bank balance
def get_bank_balance():
    balance_input = input("Enter an initial bank balance (dollars): ")
    #Returns initial bank balance as an integer
    return int(balance_input)

#Adds to the bank balance if the player wants to
def add_to_bank_balance():
    add_balance = input("Enter how many dollars to add to your balance: ")
    # Returns add_balance as an integer
    return int(add_balance)

#Prompts the user to input the wager amount and returns it as int
def get_wager_amount():
    wager = input("Enter a wager (dollars): ")
    return int(wager)

#Checks if the wager amount is valid
def is_valid_wager_amount(wager, balance):
    #if wager amount is greater than or equal to the wager amount, return True
    if balance>=wager:
        return True
    #else returns false
    else:
        return False

#Rolls two dice
def roll_die():
    #Produces a number between 1 and 6 (inclusive)
    die_value = int(randint(1,6))
    return die_value

#Calculates the sum of two dice
def calculate_sum_dice(die1_value, die2_value):
    sum_dice = die1_value + die2_value
    #Prints the sum of the dice and returns it
    return int(sum_dice)

#First roll and produces a return based on the roll
def first_roll_result(sum_dice):
    if sum_dice == 7 or sum_dice == 11:
        return "win"
    elif sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        return "loss"
    elif sum_dice == 4 or sum_dice == 5 or sum_dice == 6 or sum_dice == 8 or sum_dice == 9 or sum_dice == 10:
        return "point"

#Will be called after first roll and returns between three different options
def subsequent_roll_result(sum_dice, point_value):
    if sum_dice == point_value:
        return "point"
    elif sum_dice == 7:
        return "loss"
    else:
        return "neither"

def main():
    game_over = False
    #Calls the display_game_rules which prints the rules
    display_game_rules()
    #Gets the initial bank balance
    initial_bank_balance = get_bank_balance()

    while game_over == False:
        #Wager equals to the wager amount inputted by the player
        wager = get_wager_amount()

        #While the wager amount is more than initial bank balance, it will keep asking for an wager
        while is_valid_wager_amount(wager, initial_bank_balance) != True:
            #Prints error and asks for input again
            print("Error: wager > balance. Try again.")
            wager = get_wager_amount()

        #Else it runs the algorithm
        else:
            #First die rolls and prints
            a = roll_die()
            print("Die 1:",a)
            # Second die rolls and prints
            b = roll_die()
            print("Die 2:", b)
            #Calls the sum of the two dice and prints it
            sum_dice = calculate_sum_dice(a,b)
            print("Dice sum:",sum_dice)
            #Inputs the sum_dice into the first_roll_result and returns one of three options
            first_roll = first_roll_result(sum_dice)

            #If first_roll_result() returns "win", it runs the following
            if first_roll == "win":
                #Prints player is the winner
                print("Natural winner.\nYou WIN!")
                #Adds wager amount to the initial_bank_balance and prints it
                initial_bank_balance = initial_bank_balance + wager
                print("Balance:",initial_bank_balance)

                continue_play = input("Do you want to continue? ")
                #If the player wants to continue the game the loop will restart
                if continue_play.lower() == "yes":
                    #Prompts the user to see if they want to add to bank balance
                    add_to_balance = input("Do you want to add to your balance? ")

                    #If yes: calls add_to_bank_balance, adds it to initial_bank_balance, and prints it
                    if add_to_balance.lower() == "yes":
                        add_balance = add_to_bank_balance()
                        initial_bank_balance += add_balance
                        print("Balance: ",initial_bank_balance)
                        continue
                    # If the bank balance is 0 and the player doesn't want to add to the bank balance, the loop breaks
                    elif add_to_balance.lower() == "no" and initial_bank_balance == 0:
                        print("You don't have sufficient balance to continue.\nGame is over.")
                        break
                    # Else just continues
                    else:
                        continue
                #Else the algorithm will end
                else:
                    print("Game is over.")
                    game_over = True

            # If first_roll_result() returns "lose", it runs the following
            elif first_roll == "loss":
                print("Craps.")
                print("You lose.")
                initial_bank_balance = initial_bank_balance - wager
                print("Balance:", initial_bank_balance)


                continue_play = input("Do you want to continue? ")
                # If the player wants to continue the game the loop will restart
                if continue_play.lower() == "yes":
                    # Prompts the user to see if they want to add to bank balance
                    add_to_balance = input("Do you want to add to your balance? ")

                    # If yes: calls add_to_bank_balance, adds it to initial_bank_balance, and prints it
                    if add_to_balance.lower() == "yes":
                        add_balance = add_to_bank_balance()
                        initial_bank_balance += add_balance
                        print("Balance: ", initial_bank_balance)
                        continue
                    # If the bank balance is 0 and the player doesn't want to add to the bank balance, the loop breaks
                    elif add_to_balance.lower() == "no" and initial_bank_balance == 0:
                        print("You don't have sufficient balance to continue.\nGame is over.")
                        break
                    # Else just continues
                    else:
                        continue
                # Else the algorithm will end
                else:
                    print("Game is over.")
                    game_over = True

            # If first_roll_result() returns "point", it runs the following
            elif first_roll == "point":
                print("*** Point:",sum_dice)
                point_value = sum_dice
                # First die rolls and prints
                a = roll_die()
                print("Die 1:", a)
                # Second die rolls and prints
                b = roll_die()
                print("Die 2:", b)
                # Calls the sum of the two dice and prints it
                sum_dice = calculate_sum_dice(a, b)
                print("Dice sum:", sum_dice)
                subsequent_roll = subsequent_roll_result(sum_dice, point_value)

                #while subsequent_roll is neither, the keeps rolling the dice
                while subsequent_roll == "neither":
                    # First die rolls and prints
                    a = roll_die()
                    print("Die 1:", a)
                    # Second die rolls and prints
                    b = roll_die()
                    print("Die 2:", b)
                    # Calls the sum of the two dice and prints it
                    sum_dice = calculate_sum_dice(a, b)
                    print("Dice sum:", sum_dice)
                    subsequent_roll = subsequent_roll_result(sum_dice, point_value)

                else:
                    #if subsequent_roll is equal to point, you win and asks to continue
                    if subsequent_roll == "point":
                        # Prints player is the winner
                        print("You matched your Point.\nYou WIN!")
                        initial_bank_balance = initial_bank_balance + wager
                        print("Balance:", initial_bank_balance)

                        continue_play = input("Do you want to continue? ")
                        # If the player wants to continue the game the loop will restart
                        if continue_play.lower() == "yes":
                            # Prompts the user to see if they want to add to bank balance
                            add_to_balance = input("Do you want to add to your balance? ")

                            # If yes: calls add_to_bank_balance, adds it to initial_bank_balance, and prints it
                            if add_to_balance.lower() == "yes":
                                add_balance = add_to_bank_balance()
                                initial_bank_balance += add_balance
                                print("Balance: ", initial_bank_balance)
                                continue
                            #If the bank balance is 0 and the player doesn't want to add to the bank balance, the loop breaks
                            elif add_to_balance.lower() == "no" and initial_bank_balance == 0:
                                print("You don't have sufficient balance to continue.\nGame is over.")
                                break
                            # Else just continues
                            else:
                                continue
                        # Else the algorithm will end
                        else:
                            print("Game is over.")
                            game_over = True

                    # if subsequent_roll is equal to point, you lose and asks to continue
                    elif subsequent_roll == "loss":
                        print("You lose.")
                        initial_bank_balance = initial_bank_balance - wager
                        print("Balance:", initial_bank_balance)

                        continue_play = input("Do you want to continue? ")
                        # If the player wants to continue the game the loop will restart
                        if continue_play.lower() == "yes":
                            # Prompts the user to see if they want to add to bank balance
                            add_to_balance = input("Do you want to add to your balance? ")

                            # If yes: calls add_to_bank_balance, adds it to initial_bank_balance, and prints it
                            if add_to_balance.lower() == "yes":
                                add_balance = add_to_bank_balance()
                                initial_bank_balance += add_balance
                                print("Balance: ", initial_bank_balance)
                                continue
                            # If the bank balance is 0 and the player doesn't want to add to the bank balance, the loop breaks
                            elif add_to_balance.lower() == "no" and initial_bank_balance == 0:
                                print("You don't have sufficient balance to continue.\nGame is over.")
                                break
                            # Else just continues
                            else:
                                continue
                        # Else the algorithm will end
                        else:
                            print("Game is over.")
                            game_over = True



if __name__ == "__main__":
    main()
