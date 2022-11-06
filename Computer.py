from random import randint
from Colors import color
from Board import computer_board


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
