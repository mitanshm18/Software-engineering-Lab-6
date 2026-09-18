with open('battleship.py', 'r') as f:
    content = f.read()

count_old = """def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count"""

count_new = """def count_hit_ships(board):
    count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                count += 1
    return count"""

content = content.replace(count_old, count_new)

with open('battleship.py', 'w') as f:
    f.write(content)
