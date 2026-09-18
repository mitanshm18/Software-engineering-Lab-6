import pytest
import battleship
from battleship import check_ship_fit, ship_overlaps, count_hit_ships, print_board, user_input, turn, place_ships, main
from unittest.mock import patch, MagicMock

def setup_function(function):
    battleship.PLAYER_BOARD = [[" "] * 8 for i in range(8)]
    battleship.COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
    battleship.PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
    battleship.COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

def test_check_ship_fit():
    assert check_ship_fit(3, 0, 0, "H") == True
    assert check_ship_fit(3, 0, 6, "H") == False
    assert check_ship_fit(5, 4, 0, "V") == False
    assert check_ship_fit(5, 3, 0, "V") == True

def test_ship_overlaps():
    board = [[" "] * 8 for _ in range(8)]
    board[0][0] = "X"
    board[0][1] = "X"
    board[0][2] = "X"
    assert ship_overlaps(board, 0, 1, "H", 3) == True
    assert ship_overlaps(board, 0, 0, "V", 3) == True
    assert ship_overlaps(board, 1, 0, "H", 3) == False
    assert ship_overlaps(board, 1, 0, "V", 3) == False

def test_count_hit_ships():
    board = [[" "] * 8 for _ in range(8)]
    board[0][0] = "X"
    board[1][1] = "O"
    board[2][2] = "X"
    assert count_hit_ships(board) == 2

def test_print_board(capsys):
    board = [[" "] * 8 for _ in range(8)]
    print_board(board)
    captured = capsys.readouterr()
    assert "A B C D E F G H" in captured.out
    assert "1| | | | | | | | |" in captured.out

@patch('builtins.input', side_effect=['H', '1', 'A'])
def test_user_input(mock_input):
    row, col, ori = user_input(True)
    assert ori == 'H'
    assert row == 0
    assert col == 0

@patch('builtins.input', side_effect=['Z', 'V', '9', '2', 'Z', 'B'])
def test_user_input_invalid_retries(mock_input):
    # Tests exception handling and loop continuation
    row, col, ori = user_input(True)
    assert ori == 'V'
    assert row == 1
    assert col == 1

@patch('builtins.input', side_effect=['1', 'A'])
def test_turn_player(mock_input):
    board = battleship.PLAYER_GUESS_BOARD
    battleship.COMPUTER_BOARD[0][0] = "X"
    turn(board)
    assert board[0][0] == "X"

@patch('builtins.input', side_effect=['2', 'B'])
def test_turn_player_miss(mock_input):
    board = battleship.PLAYER_GUESS_BOARD
    turn(board)
    assert board[1][1] == "-"

def test_turn_computer():
    # If board is computer guess board, it uses random instead of input
    battleship.PLAYER_GUESS_BOARD[0][0] = "-" # Make boards unequal in value!
    board = battleship.COMPUTER_GUESS_BOARD
    turn(board)
    # Just verifies it doesn't crash and modifies board
    count = sum(row.count("X") + row.count("-") for row in board)
    assert count == 1

@patch('battleship.user_input', side_effect=[
    (0, 0, 'H'), (1, 0, 'V'), (2, 0, 'H'), (3, 0, 'V'), (4, 0, 'H'),
    (5, 0, 'V'), (6, 0, 'H'), (7, 0, 'V'), (0, 7, 'V'), (7, 7, 'H'),
    (2, 2, 'H'), (3, 3, 'V'), (4, 4, 'H'), (5, 5, 'V'), (6, 6, 'H')
])
def test_place_ships_player(mock_input):
    battleship.place_ships(battleship.PLAYER_BOARD)
    assert battleship.PLAYER_BOARD[0][0] == 'X'

def test_place_ships_computer():
    battleship.place_ships(battleship.COMPUTER_BOARD)
    # The board should have exactly 17 'X's placed
    assert sum(row.count('X') for row in battleship.COMPUTER_BOARD) == 17
