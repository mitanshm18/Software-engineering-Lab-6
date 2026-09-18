import random

BOARD_SIZE = 8
LENGTH_OF_SHIPS = [2,3,3,4,5]  
PLAYER_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]
COMPUTER_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]
PLAYER_GUESS_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]
COMPUTER_GUESS_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}


def place_ship_on_board(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            board[row][i] = "X"
    else:
        for i in range(row, row + ship_length):
            board[i][column] = "X"

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#place Ships
def place_ships(board):
    #loop through length of ships
    for ship_length in LENGTH_OF_SHIPS:
        #loop until ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps
                        if ship_overlaps(board, row, column, orientation, ship_length) == False:
                            #place ship
                            place_ship_on_board(board, row, column, orientation, ship_length)
                            print_board(PLAYER_BOARD)
                            break 

#check if ship fits in board
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > BOARD_SIZE:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > BOARD_SIZE:
            return False
        else:
            return True

#check each position for overlap
def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False



def get_valid_input(prompt, valid_options, converter=str):
    while True:
        try:
            val = input(prompt).upper()
            if val in valid_options:
                return converter(val)
        except Exception:
            pass
        print("Invalid input.")

def user_input(place_ship):
    orientation = None
    if place_ship == True:
        orientation = get_valid_input("Enter orientation (H or V): ", ["H", "V"])
    
    row_val = get_valid_input("Enter the row 1-8 of the ship: ", [str(i) for i in range(1, 9)])
    row = int(row_val) - 1
    
    col_val = get_valid_input("Enter the column of the ship: ", list("ABCDEFGH"))
    column = LETTERS_TO_NUMBERS[col_val]
    
    if place_ship == True:
        return row, column, orientation 
    else:
        return row, column        

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                count += 1
    return count

#user and computer turn
def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

def main():
    place_ships(COMPUTER_BOARD)
    print_board(COMPUTER_BOARD)
    print_board(PLAYER_BOARD)
    place_ships(PLAYER_BOARD)
            
    while True:
        #player turn
        while True:
            print('Guess a battleship location')
            print_board(PLAYER_GUESS_BOARD)
            turn(PLAYER_GUESS_BOARD)
            break
        if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
            print("You win!")
            break   
        #computer turn
        while True:
            turn(COMPUTER_GUESS_BOARD)
            break           
        print_board(COMPUTER_GUESS_BOARD)   
        if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
            print("Sorry, the computer won.")
            break

if __name__ == "__main__":
    main()