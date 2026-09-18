with open('battleship.py', 'r') as f:
    content = f.read()

helper = """
def get_valid_input(prompt, valid_options, converter=str):
    while True:
        try:
            val = input(prompt).upper()
            if val in valid_options:
                return converter(val)
        except Exception:
            pass
        print("Invalid input.")

"""

content = content.replace("def user_input", helper + "def user_input")

user_input_old = """def user_input(place_ship):
    if place_ship == True:
        while True:
            try: 
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try: 
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, orientation 
    else:
        while True:
            try: 
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column"""

user_input_new = """def user_input(place_ship):
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
        return row, column"""

content = content.replace(user_input_old, user_input_new)

with open('battleship.py', 'w') as f:
    f.write(content)
