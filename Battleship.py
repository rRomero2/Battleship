# Import Libraries
import copy
import random
from random import randint
import sys


# Font Colours

class color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


# Board Setups, Copies and Printing Functions
board = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]  # Number row at the top


def board_setup(board):
    template_row = ["O", color.BLUE + "-", "-", "-", "-", "-", "-", "-", "-", "-", "-" + color.END]  # Empty rows
    empty_row = []
    alpha = 65
    for index in range(11):
        new_row = copy.deepcopy(template_row)
        board.append(new_row)
        if board[index][0] == "O":
            board[index][0] = color.END + chr(alpha)
            alpha += 1
    del board[-1]
    return board


def print_board(board):  # Print board not in list form
    for row in board:
        print("    ".join(row))


board_setup(board)
computer_board = copy.deepcopy(board)
player_board_shots = copy.deepcopy(board)
player_board_ships = copy.deepcopy(board)

# Variable Initialization
carrier_hits = 0
battleship_hits = 0
destroyer_hits = 0
submarine_hits = 0
paddle_boat_hits = 0
ships_sunk = 0
guesses_made = []
exit_inputs = ['Exit', 'exit', 'E', 'e', 'EXIT', 'QUIT', 'Quit', 'quit', 'Q', 'q']

# Ship lengths and Positions Dictionaries
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Submarine": 3,
    "Destroyer": 3,
    "Paddle Boat": 2
}
ships_position = {
    "Carrier": [],
    "Battleship": [],
    "Submarine": [],
    "Destroyer": [],
    "Paddle Boat": []
}


# Generate Computer Board Ships
class place_ship:
    def __init__(self, ship, length):
        self.ship = ship
        self.length = length

    def position(self):
        global temporary_position
        temporary_position = []
        global direction
        direction = randint(0, 1)  # Horizontal or vertical
        if direction == 0:  # Horizontal
            row = randint(1, 10)
            column = randint(1, 6)
        else:  # Vertical
            row = randint(1, 6)
            column = randint(1, 10)
        for i in range(self.length):
            position = str(row) + str(column)
            temporary_position.append(position)
            if direction == 0:  # Horizontal, add column
                column += 1
            else:  # Vertical, add row
                row += 1

    def placing(self):
        check_overlap = 0
        while check_overlap < 5:
            for ships in ships_position:  # Iterate through the dictionary
                check = any(item in ships_position[ships] for item in temporary_position)  # Check if the ship overlaps
                if check is True:  # At least one value already taken
                    del temporary_position[:]
                    if direction == 0:  # Horizontal
                        row = randint(1, 10)
                        column = randint(1, 6)
                    else:  # Vertical
                        row = randint(1, 6)
                        column = randint(1, 10)
                    for i in range(self.length):
                        position = str(row) + str(column)
                        temporary_position.append(position)
                        if direction == 0:  # Horizontal, add column
                            column += 1
                        else:  # Vertical, add row
                            row += 1
                    check_overlap = 0
                else:  # Everything is OK
                    check_overlap += 1
        if check_overlap >= 5:  # No overlapping, place the ship on the board
            ships_position[self.ship] = temporary_position
            for i in range(len(temporary_position)):
                if len(temporary_position[i]) > 2:  # Either row or column (or both) is 10
                    if int(temporary_position[i][-1]) == 0:  # Column is 10
                        place_row = int(temporary_position[i][:1])
                        place_col = int(temporary_position[i][1:])
                        computer_board[place_row][place_col] = color.END + "X" + color.BLUE
                    elif int(temporary_position[i][-1]) == 0 and len(temporary_position[i]) == 4:  # Both is 10
                        place_row = int(temporary_position[i][:2])
                        place_col = int(temporary_position[i][2:])
                        computer_board[place_row][place_col] = color.END + "X" + color.BLUE
                    else:  # Row is 10
                        place_row = int(temporary_position[i][:2])
                        place_col = int(temporary_position[i][2:])
                        computer_board[place_row][place_col] = color.END + "X" + color.BLUE
                else:  # Neither are 10
                    place_row = int(temporary_position[i][:1])
                    place_col = int(temporary_position[i][1:])
                    computer_board[place_row][place_col] = color.END + "X" + color.BLUE
        return computer_board


# Call Class to Generate Computer Board (Ships Position)
carrier = place_ship("Carrier", 5)
carrier.position()
carrier.placing()

battle = place_ship("Battleship", 4)
battle.position()
battle.placing()

destroyer = place_ship("Destroyer", 3)
destroyer.position()
destroyer.placing()

submarine = place_ship("Submarine", 3)
submarine.position()
submarine.placing()

paddle = place_ship("Paddle Boat", 2)
paddle.position()
paddle.placing()


# print_board(computer_board) # Testing only
# print ships_position # Testing only

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


def play_game_1():      # Version 1: player guesses against the computer, but doesn't place their own ships
    print("\nWelcome to Battleship!\n")
    print_board(player_board_shots)
    if limited_guesses is True:     # Repeat for the max number of guesses
        while len(guesses_made) < guesses_max:
            if ships_sunk < 5:      # At least one ship still in play
                user_guess(ships_position)
            else:
                print("Congratulations! You sunk all enemy ships!")
                sys.exit()
        if len(guesses_made) == guesses_max:
            if ships_sunk == 5:
                print("Congratulations! You sunk all enemy ships!")
                sys.exit()
            else:
                print("You ran out of guesses.")
                stats()
                print("Here were the enemy ship positions: \n")
                print_board(computer_board)
                sys.exit()
    else:
        while ships_sunk < 5:
            user_guess(ships_position)
        if ships_sunk == 5:
            print("Congratulations! You sunk all enemy ships!")
            sys.exit()


def play_game_2():
    print("\nWelcome to Battleship!\n")
    place_user_ships()


def place_user_ships():
    valid_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    print("Placing carrier (length 5)")
    place_ship = input("Enter a coordinate: ")
    if len(place_ship) < 2 or len(place_ship) > 3:  # Input too short or too long
        print("Guesses must contain a row (A-J) and a column (1-10).")
        print("Please enter a valid guess.")
    else:
        place_ship_alpha = place_ship[0].lower()
        place_ship_num = place_ship[1:]
        if place_ship_alpha not in valid_alpha:
            print("Rows must be between A and J.")
            print("Please enter a valid row.")
        elif not place_ship_num.isdigit() or not 1 <= int(place_ship_num) <= 10:
            print("Columns must be between 1 and 10.")
            print("Please enter a valid column.")
        else:
            if player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num)] == "0":
                print("Coordinate already taken.")
                print("Please enter another coordinate.")
            else:
                for i in range(5):
                    if (int(place_ship_num)+i <= 10) and (int(place_ship_num)+i >= 1) and player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num)+i] == "0":
                        print("Coordinate already taken.")
                        print("Please enter another coordinate.")
                    player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num)] = color.END + "0" + color.BLUE
    print_board(player_board_ships)

#player_board_shots[int(ord(guess_alpha) - 96)][int(guess_num)]

def user_guess(ships_position):
    global guess_modified, ships_sunk, paddle_boat_hits, submarine_hits, destroyer_hits, battleship_hits, carrier_hits
    valid_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    hit_tracker = False
    guess_validity = False
    while not guess_validity:
        guess = input("Enter your shot: ")  # User input for guess
        if guess in exit_inputs:
            if ships_sunk != 5:
                stats()
                print("Here were the enemy ship positions: \n")
                print_board(computer_board)
                print("\nThank you for playing.")
                sys.exit()
        elif len(guess) < 2 or len(guess) > 3:  # Input too short or too long
            print("Guesses must contain a row (A-J) and a column (1-10).")
            print("Please enter a valid guess.")
        else:
            guess_alpha = guess[0].lower()
            guess_num = guess[1:]
            if guess_alpha not in valid_alpha:  # Letter not in range
                print("Rows must be between A and J.")
                print("Please enter a valid row.")
            elif not guess_num.isdigit() or not 1 <= int(guess_num) <= 10:  # Number not in range
                print("Columns must be between 1 and 10.")
                print("Please enter a valid column.")
            else:
                guess_modified = str(ord(guess_alpha) - 96) + str(guess_num)
                if guess_modified not in guesses_made:
                    guesses_made.append(guess_modified)
                    guess_validity = True
                else:
                    print("You already guessed that.")
                    print("Please enter a new guess.")
    for key, value in ships_position.items():
        if guess_modified in value:
            ship_hit = key
            if ship_hit == "Carrier":
                carrier_hits += 1
                if carrier_hits == 5:
                    print("You sunk the Carrier.")
                    ships_sunk += 1
            elif ship_hit == "Battleship":
                battleship_hits += 1
                if battleship_hits == 4:
                    print("You sunk the Battleship.")
                    ships_sunk += 1
            elif ship_hit == "Destroyer":
                destroyer_hits += 1
                if destroyer_hits == 3:
                    print("You sunk the Destroyer.")
                    ships_sunk += 1
            elif ship_hit == "Submarine":
                submarine_hits += 1
                if submarine_hits == 3:
                    print("You sunk the Submarine.")
                    ships_sunk += 1
            elif ship_hit == "Paddle Boat":
                paddle_boat_hits += 1
                if paddle_boat_hits == 2:
                    print("You sunk the Paddle Boat.")
                    ships_sunk += 1
            hit_tracker = True
    if hit_tracker is True:
        player_board_shots[int(ord(guess_alpha) - 96)][int(guess_num)] = color.RED + "X" + color.BLUE
        print_board(player_board_shots)
        print(color.RED + "\nHit!\n" + color.END)
        stats()
        return player_board_shots
    else:
        player_board_shots[int(ord(guess_alpha) - 96)][int(guess_num)] = color.END + "0" + color.BLUE
        print_board(player_board_shots)
        print("\nMiss!\n")
        stats()
        return player_board_shots


def stats():
    print("Stats".center(40, '-'))
    if limited_guesses is True:
        print("Rounds played: %d of %d" % (len(guesses_made), guesses_max))
    else:
        print("Rounds played: %d" % len(guesses_made))
    print("Ships sunk: %d of 5 " % (ships_sunk))
    if carrier_hits == 5:
        car = "Carrier: " + color.RED + "Sunk" + color.END
        print(car)
    else:
        print("Carrier: Still in Play")
    if battleship_hits == 4:
        bat = "Battleship: " + color.RED + "Sunk" + color.END
        print(bat)
    else:
        print("Battleship: Still in Play")
    if destroyer_hits == 3:
        des = "Destroyer: " + color.RED + "Sunk" + color.END
        print(des)
    else:
        print("Destroyer: Still in Play")
    if submarine_hits == 3:
        sub = "Submarine: " + color.RED + "Sunk" + color.END
        print(sub)
    else:
        print("Submarine: Still in Play")
    if paddle_boat_hits == 2:
        pad = "Paddle Boat: " + color.RED + "Sunk" + color.END
        print(pad)
    else:
        print("Paddle Boat: Still in Play")
    print("\n")


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
            play_game_1()
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
        global guesses_max
        if guesses_choice == "1":
            guesses_max = 100
            play_game_1()
            break
        elif guesses_choice == "2":
            guesses_max = 70
            play_game_1()
            break
        elif guesses_choice == "3":
            guesses_max = 45
            play_game_1()
            break
        elif guesses_choice == "4":
            guesses_max = 30
            play_game_1()
            break
        elif guesses_choice == "5":
            pick_max_guesses()
            break
        else:
            print("I don't understand. Please enter a number from 1-5.")


def pick_max_guesses():
    while True:
        global guesses_max
        guesses_input = input("Enter the maximum number of guesses you would like to play with: ")
        if guesses_input.isdigit() and int(guesses_input) > 0:
            guesses_max = int(guesses_input)
            print(guesses_max)
            play_game_1()
            break
        else:
            print("Maximum number of guesses must be a number greater than 0.")


# Calling the Function to Start Game
start_screen()
