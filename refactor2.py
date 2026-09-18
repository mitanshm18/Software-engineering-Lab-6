with open('battleship.py', 'r') as f:
    content = f.read()

content = content.replace("LENGTH_OF_SHIPS = [2,3,3,4,5]", "BOARD_SIZE = 8\nLENGTH_OF_SHIPS = [2,3,3,4,5]")
content = content.replace('PLAYER_BOARD = [[" "] * 8 for i in range(8)]', 'PLAYER_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]')
content = content.replace('COMPUTER_BOARD = [[" "] * 8 for i in range(8)]', 'COMPUTER_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]')
content = content.replace('PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]', 'PLAYER_GUESS_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]')
content = content.replace('COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]', 'COMPUTER_GUESS_BOARD = [[" "] * BOARD_SIZE for i in range(BOARD_SIZE)]')

content = content.replace("random.randint(0,7)", "random.randint(0, BOARD_SIZE - 1)")
content = content.replace("column + SHIP_LENGTH > 8:", "column + SHIP_LENGTH > BOARD_SIZE:")
content = content.replace("row + SHIP_LENGTH > 8:", "row + SHIP_LENGTH > BOARD_SIZE:")

with open('battleship.py', 'w') as f:
    f.write(content)
