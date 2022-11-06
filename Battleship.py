# Import Libraries and files
import sys
from Player import play_game_1, play_game_2
exit_inputs = ['Exit', 'exit', 'E', 'e', 'EXIT', 'QUIT', 'Quit', 'quit', 'Q', 'q']

# Game Play Related Functions
def start_screen():
    start_inputs = ['Start', 'start', 's', 'S', 'START']
    instruction_inputs = ['Instructions', 'instructions', 'I', 'i', 'INSTRUCTIONS']
    exit_inputs = ['Exit', 'exit', 'E', 'e', 'EXIT']
    yes_commands = ['Yes', 'yes', 'y', 'Y', 'YES']
    no_commands = ['No', 'no', 'n', 'N', 'NO']

    def menu():
        print(" Battleship ".center(50, '-'))
        print("\n")
        print("Start".center(50))
        print("Instructions".center(48))
        print("Exit".center(48))
        print("\n")

    menu()
    while True:
        user_input1 = input(" What would you like to do? ")
        if user_input1 in start_inputs:
            game_choice()
            break
        elif user_input1 in instruction_inputs:
            print("\n")
            print("Instructions".center(50))
            print("\n")
            print(
                "Battleship is a game of strategy and deduction. In the single-player version, you will play against "
                "the computer.\n\n "
                "There are 5 ships placed in the ocean:\n"
                "Carrier: 5 holes\n"
                "Battleship: 4 holes\n"
                "Destroyer: 3 holes\n"
                "Submarine: 3 holes\n"
                "Paddle Boat: 2 holes\n"
                "The computer will place the ships in the ocean, either horizontally or vertically - but not "
                "diagonally. Ships will not overlap each other\n "
                "or overhang the 10x10 square.\n"
                "\n"
                "Your board will represent your shots. In each turn, you will pick a target. Rows are represented by "
                "letters A-J and columns by numbers 1-10.\n "
                "Each shot must be in the format LetterNumber: eg. A1, H10 etc.\n"
                "If your shot hit a ship, your board will be updated with a red X on your board. If you missed, "
                "a white X will be placed instead.\n "
                "You will not be told what shipped you have hit, but you will be told when a ship has been sunk.\n"
                "After each turn, you will be told how many turns you have played, how many ships are still in play "
                "and the status of each ship (still in play or sunk).\n "
                "You will win the game when all 5 enemy ships have been sunk.\n"
                "If you want to quit mid-game, enter Quit, QUIT, Q, q, Exit, EXIT, E, or e when prompted for your "
                "shot.\n")
            instructions = input("Return to main menu (y) ")
            if instructions in yes_commands:
                menu()
            else:
                exit_user = input("Quit? ")
                if exit_user in yes_commands:
                    sys.exit()
                else:
                    menu()
        elif user_input1 in exit_inputs:
            print("Thank you for playing.")
            sys.exit()

        else:
            print("I don't understand. Please enter a valid option.")


def game_choice():
    print("Game Type".center(45, '-'))
    print("1. Solo (Guess against AI without placing ships)")
    print("\n2. Normal (Both player and Comp place ships and take turns guessing)")
    while True:
        game_choice = input("\nEnter Choice [1/2]: ")
        if game_choice == "1":
            level_choice()
            break
        elif game_choice == "2":
            print("Normal - Coming Soon")
            play_game_2()
            break
        else:
            print("I don't understand. Please enter 1 or 2.")


def level_choice():
    print("Difficulty".center(45, '-'))
    print("1. Free Play (Unlimited Guesses)")
    print("2. Limited Number of Guesses")
    global limited_guesses
    limited_guesses = False
    while True:
        level_choice = input("\nEnter Choice: ")
        if level_choice == "1":
            play_game_1(False, None)
            break
        elif level_choice == "2":
            limited_guesses = True
            guesses_difficulty()
            break
        else:
            print("I don't understand. Please enter a number from 1-3.")


def guesses_difficulty():
    print("Limited Number of Guesses Difficulty".center(25, '-'))
    print("1. Easy: 90 Guesses")
    print("2. Medium: 70 Guesses")
    print("3. Hard: 50 Guesses")
    print("4. Speedrun: 30 Guesses")
    print("5. Custom")
    while True:
        guesses_choice = input("\nEnter Choice: ")
        if guesses_choice == "1":
            play_game_1(True, 100)
            break
        elif guesses_choice == "2":
            play_game_1(True, 70)
            break
        elif guesses_choice == "3":
            play_game_1(True, 45)
            break
        elif guesses_choice == "4":
            play_game_1(True, 30)
            break
        elif guesses_choice == "5":
            pick_max_guesses()
            break
        else:
            print("I don't understand. Please enter a number from 1-5.")


def pick_max_guesses():
    while True:
        guesses_input = input("Enter the maximum number of guesses you would like to play with: ")
        if guesses_input.isdigit() and int(guesses_input) > 0:
            guesses_max = int(guesses_input)
            print(guesses_max)
            play_game_1(True, guesses_max)
            break
        else:
            print("Maximum number of guesses must be a number greater than 0.")


# Calling the Function to Start Game
start_screen()
