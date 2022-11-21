import copy
from Colors import color

# Board Setups, Copies and Printing Functions
board = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]  # Number row at the top


def board_setup(board):
    template_row = ["O", color.BLUE + "-" + color.END, color.BLUE + "-" + color.END, color.BLUE + "-" + color.END,
                    color.BLUE + "-" + color.END, color.BLUE + "-" + color.END, color.BLUE + "-" + color.END,
                    color.BLUE + "-" + color.END, color.BLUE + "-" + color.END, color.BLUE + "-" + color.END,
                    color.BLUE + "-" + color.END]  # Empty rows
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
