import re

with open('battleship.py', 'r') as f:
    content = f.read()

new_func = """
def place_ship_on_board(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            board[row][i] = "X"
    else:
        for i in range(row, row + ship_length):
            board[i][column] = "X"

def print_board(board):"""

content = content.replace("def print_board(board):", new_func)

dup_code1 = """                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
"""

content = content.replace(dup_code1, "                            place_ship_on_board(board, row, column, orientation, ship_length)\n")

with open('battleship.py', 'w') as f:
    f.write(content)
