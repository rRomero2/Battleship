from Colors import color
from Board import print_board, computer_board, player_board_shots, player_board_ships
import sys
from Computer import ships_position, computer_guess

# Variable Initialization
guesses_made = []
exit_inputs = ['Exit', 'exit', 'E', 'e', 'EXIT', 'QUIT', 'Quit', 'quit', 'Q', 'q']
ships_sunk_player = 0  # Counter for the number of ships the player has sunk against the computer
ships_sunk_computer = 0  # Counter for the number of ships the computer has sunk against the player
carrier_hits = 0
battleship_hits = 0
destroyer_hits = 0
submarine_hits = 0
paddle_boat_hits = 0


def user_guess():
    global guess_modified, ships_sunk_player, carrier_hits, destroyer_hits, battleship_hits, submarine_hits, paddle_boat_hits
    valid_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    hit_tracker = False
    guess_validity = False
    while not guess_validity:
        guess = input("Enter your shot: ")  # User input for guess
        if guess in exit_inputs:
            if ships_sunk_player != 5:
                stats()  # Abort game, doesn't matter what guess user was at
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
                    ships_sunk_player += 1
            elif ship_hit == "Battleship":
                battleship_hits += 1
                if battleship_hits == 4:
                    print("You sunk the Battleship.")
                    ships_sunk_player += 1
            elif ship_hit == "Destroyer":
                destroyer_hits += 1
                if destroyer_hits == 3:
                    print("You sunk the Destroyer.")
                    ships_sunk_player += 1
            elif ship_hit == "Submarine":
                submarine_hits += 1
                if submarine_hits == 3:
                    print("You sunk the Submarine.")
                    ships_sunk_player += 1
            elif ship_hit == "Paddle Boat":
                paddle_boat_hits += 1
                if paddle_boat_hits == 2:
                    print("You sunk the Paddle Boat.")
                    ships_sunk_player += 1
            hit_tracker = True
    if hit_tracker is True:
        player_board_shots[int(ord(guess_alpha) - 96)][int(guess_num)] = color.RED + "X" + color.BLUE
        print_board(player_board_shots)
        print(color.RED + "\nHit!\n" + color.END)
        stats()
        return player_board_shots
    else:
        player_board_shots[int(ord(guess_alpha) - 96)][int(guess_num)] = color.END + "X" + color.BLUE
        print_board(player_board_shots)
        print("\nMiss!\n")
        stats()
        return player_board_shots


# Helper functions for checking ship coordinate and placing ship on the board
# Return -1 if the ship wasn't placed and 1 if the ship was
def moveRight(length, place_ship_alpha, place_ship_num):
    place = True
    for i in range(1, length):
        if player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num) + i] != color.BLUE + "-" + color.END:
            place = False
            print(color.END + "Not enough free tiles for the ship." + color.END)
            print(color.END + "Please enter another coordinate.\n" + color.END)
            return -1
    if place:  # If only one way to place the ship from that coordinate, place automatically
        for i in range(0, length):
            player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num) + i] = color.END + "0" + color.BLUE
        return 1


def moveLeft(length, place_ship_alpha, place_ship_num):
    place = True
    for i in range(1, length):
        if player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num) - i] != color.BLUE + "-" + color.END:
            place = False
            print(color.END + "Not enough free tiles for the ship." + color.END)
            print(color.END + "Please enter another coordinate.\n" + color.END)
            return -1
    if place:  # If only one way to place the ship from that coordinate, place automatically
        for i in range(0, length):
            player_board_ships[int(ord(place_ship_alpha) - 96)][int(place_ship_num) - i] = color.END + "0" + color.BLUE
        return 1


def moveDown(length, place_ship_alpha, place_ship_num):
    place = True
    for i in range(1, length):
        if player_board_ships[int(ord(place_ship_alpha) - 96 + i)][int(place_ship_num)] != color.BLUE + "-" + color.END:
            place = False
            print(color.END + "Not enough free tiles for the ship." + color.END)
            print(color.END + "Please enter another coordinate.\n" + color.END)
            return -1
    if place:  # If only one way to place the ship from that coordinate, place automatically
        for i in range(0, length):
            player_board_ships[int(ord(place_ship_alpha) - 96 + i)][int(place_ship_num)] = color.END + "0" + color.BLUE
        return 1


def moveUp(length, place_ship_alpha, place_ship_num):
    place = True
    for i in range(1, length):
        if player_board_ships[int(ord(place_ship_alpha) - 96 - i)][int(place_ship_num)] != color.BLUE + "-" + color.END:
            place = False
            print(color.END + "Not enough free tiles for the ship." + color.END)
            print(color.END + "Please enter another coordinate.\n" + color.END)
            return -1
    if place:  # If only one way to place the ship from that coordinate, place automatically
        for i in range(0, length):
            player_board_ships[int(ord(place_ship_alpha) - 96 - i)][int(place_ship_num)] = color.END + "0" + color.BLUE
        return 1


def place_user_ships(name, length):
    valid_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    valid_orientation_hor = ['horizontal', 'HORIZONTAL', 'H', 'h']
    valid_orientation_ver = ['vertical', 'VERTICAL', 'V', 'v']

    print(f"Placing {name}, length {length}")
    while True:
        orient = input("Place carrier horizontally or vertically? (h/v): ")
        if orient in valid_orientation_hor:
            orient = "h"
            break
        elif orient in valid_orientation_ver:
            orient = "v"
            break
        else:
            print("Please enter a valid orientation (h/v).")

    print_board(player_board_ships)

    while True:
        place_ship = input("Enter a coordinate: ")
        if len(place_ship) < 2 or len(place_ship) > 3:  # Input too short or too long
            print("Guesses must contain a row (A-J) and a column (1-10).")
            print("Please enter a valid guess.")
        else:
            place_ship_alpha = place_ship[0].lower()
            place_ship_num = place_ship[1:]

            if place_ship_alpha not in valid_alpha:  # Row not valid
                print("Rows must be between A and J.")
                print("Please enter a valid row.")
            elif not place_ship_num.isdigit() or not 1 <= int(place_ship_num) <= 10:  # Column not valid
                print("Columns must be between 1 and 10.")
                print("Please enter a valid column.")
            elif player_board_ships[int(ord(place_ship_alpha) - 96)][
                int(place_ship_num)] != color.BLUE + "-" + color.END:
                print("Coordinate already taken.")
                print("Please enter another coordinate.")
            else:
                place = True
                if orient == "h":
                    if place_ship_num == '1':
                        if moveRight(length, place_ship_alpha, place_ship_num) == 1:
                            return
                    elif place_ship_num == "10":
                        if moveLeft(length, place_ship_alpha, place_ship_num) == 1:
                            return
                    else:
                        if int(place_ship_num) <= 11 - length:
                            if moveRight(length, place_ship_alpha, place_ship_num) == 1:
                                return
                        elif int(place_ship_num) > 11 - length:
                            for i in range(0, length):
                                if player_board_ships[int(ord(place_ship_alpha) - 96)][(11 - length) + i] != color.BLUE + "-" + color.END:
                                    place = False
                                    print(color.END + "Not enough free tiles for the ship." + color.END)
                                    print(color.END + "Please enter another coordinate.\n" + color.END)
                                    break
                            if place:
                                for i in range(0, length):
                                    player_board_ships[int(ord(place_ship_alpha) - 96)][(11 - length) + i] = color.END + "0" + color.BLUE
                                return

                elif orient == "v":
                    if place_ship_alpha == 'a':
                        if moveDown(length, place_ship_alpha, place_ship_num) == 1:
                            return
                    elif place_ship_alpha == "j":
                        if moveUp(length, place_ship_alpha, place_ship_num) == 1:
                            return
                    else:
                        if (11 - int(
                                ord(place_ship_alpha) - 96)) >= length:  # Check if enough tiles below the coordinate
                            if moveDown(length, place_ship_alpha, place_ship_num) == 1:
                                return
                        elif (11 - int(ord(place_ship_alpha) - 96)) < length:
                            # If the player enters a vertical coordinate that would not have enough files
                            # straight the ship is placed straight up starting from 'j' (eg. i7 places the carrier
                            # f7-j7
                            for i in range(0, length):
                                if player_board_ships[11 - length + i][int(place_ship_num)] != color.BLUE + "-" + color.END:
                                    place = False
                                    print(color.END + "Not enough free tiles for the ship." + color.END)
                                    print(color.END + "Please enter another coordinate.\n" + color.END)
                                    break
                            if place:
                                for i in range(0, length):
                                    player_board_ships[11 - length + i][int(place_ship_num)] = color.END + "0" + color.BLUE
                                return


# Version 1: player guesses against the computer, but doesn't place their own ships
def play_game_1(limited, guesses):
    global guesses_max, limited_guesses
    guesses_max = guesses
    limited_guesses = limited
    print("\nWelcome to Battleship!\n")
    print_board(player_board_shots)
    if limited_guesses is True:  # Repeat for the max number of guesses
        while len(guesses_made) < guesses_max:
            if ships_sunk_player < 5:  # At least one ship still in play
                user_guess()
            else:
                print("Congratulations! You sunk all enemy ships!")
                sys.exit()
        if len(guesses_made) == guesses_max:
            if ships_sunk_player == 5:
                print("Congratulations! You sunk all enemy ships!")
                sys.exit()
            else:
                print("You ran out of guesses.")
                stats()
                print("Here were the enemy ship positions: \n")
                print_board(computer_board)
                sys.exit()
    else:
        while ships_sunk_player < 5:
            user_guess()
        if ships_sunk_player == 5:
            print("Congratulations! You sunk all enemy ships!")
            sys.exit()


# Version 2: player places their ships and plays against the computer
def play_game_2(limited, guesses):
    global guesses_max, limited_guesses
    guesses_max = guesses
    limited_guesses = limited
    print("\nWelcome to Battleship!\n")
    place_user_ships("Carrier", 5)
    print_board(player_board_ships)
    place_user_ships("Battleship", 4)
    print_board(player_board_ships)
    place_user_ships("Destroyer", 3)
    print_board(player_board_ships)
    place_user_ships("Submarine", 3)
    print_board(player_board_ships)
    place_user_ships("Paddle boat", 2)
    print("Your shots:")
    print_board(player_board_shots)
    print("\n Your ships:")
    print_board(player_board_ships)
    print("Game coming soon...")
    if limited_guesses is True:
        while len(guesses_made) < guesses_max:  # Still have guesses left
            if ships_sunk_player < 5 and ships_sunk_computer < 5:  # Both still have at least 1 ship in play
                user_guess()
                if ships_sunk_player == 5:
                    print("Congratulations! You sunk all enemy ships!")
                    sys.exit()
                computer_guess()
                if ships_sunk_computer == 5:
                    print("You lost! The computer has sunk all your ships.")
                    sys.exit()
            # elif ships_sunk_player == 5:
            # print("Congratulations! You sunk all enemy ships.")
            # sys.exit()
            # elif ships_sunk_computer == 5:
            # print("You lost! The computer has sunk all your ships.")
            # sys.exit()
        if len(guesses_made) == guesses_max:  # No guesses left
            if ships_sunk_player == 5:
                print("Congratulations! You sunk all enemy ships!")
                sys.exit()
            elif ships_sunk_computer == 5:
                print("You lost! The computer has sunk all your ships.")
                sys.exit()
            else:
                print("You ran out of guesses.")
                stats()
                print("Here were the enemy ship positions: \n")
                print_board(computer_board)
                sys.exit()

    else:
        while ships_sunk_player < 5 and ships_sunk_computer < 5:
            user_guess()
            if ships_sunk_player == 5:
                print("Congratulations! You sunk all enemy ships!.")
                sys.exit()
            computer_guess()
            if ships_sunk_computer == 5:
                print("You lost! The computer has sunk all your ships.")
                sys.exit()


def stats():
    print("Stats".center(40, '-'))
    if limited_guesses is True:
        print("Rounds played: %d of %d" % (len(guesses_made), guesses_max))
    else:
        print("Rounds played: %d" % len(guesses_made))
    print("Ships sunk: %d of 5 " % ships_sunk_player)
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
