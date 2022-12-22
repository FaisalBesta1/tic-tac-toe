import os

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("""
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \\
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___                                                 
""")

# Input player names

player_1 = input("Hello, welcome to my Noughts and Crosses multiplayer game.\nPlease enter player 1's (Crosses') "
                 "name: ")
player_2 = input("\nPlease enter player 2's (Noughts') name: ")

# Shows the current grid


def show():
    game = f' {grid[0]} | {grid[1]} | {grid[2]} \n' \
           f'-----------\n' \
           f' {grid[3]} | {grid[4]} | {grid[5]} \n' \
           f'-----------\n' \
           f' {grid[6]} | {grid[7]} | {grid[8]} \n'
    print(game)


print("\n")
show()

game_is_on = True

""" 
Function to check if input is a valid number
"""


def check_is_number(placement: str) -> int:
    valid_input = False
    while not valid_input:
        try:
            placement = int(placement) - 1
            valid_input = True
        except ValueError:
            valid_input = False
            placement = input("Wrong value type was inputted. Please enter a number: ")

    return placement


def x_placement():
    placement = input("Where do you want to place x? ")
    placement = check_is_number(placement)

    while placement > 8 or placement < 0:
        placement = input("Invalid space entered. Please enter a number between 1 and 9: ")
        placement = check_is_number(placement)
    while grid[placement] == "x" or grid[placement] == "o":
        placement = input("Space occupied, where do you want to place x? ")
        placement = check_is_number(placement)
    else:
        grid[placement] = "x"


def o_placement():
    placement = input("Where do you want to place o? ")
    placement = check_is_number(placement)

    while placement > 8 or placement < 0:
        placement = input("Invalid space entered. Please enter a number between 1 and 9: ")
        placement = check_is_number(placement)
    while grid[placement] == "x" or grid[placement] == "o":
        placement = input("Space occupied, where do you want to place o? ")
        placement = check_is_number(placement)
    else:
        grid[placement] = "o"


"""
Function to check if there is a winning row/column in the grid, returns False if winning condition is met
"""


def check():
    win_cons = {
        "line1": (grid[0], grid[1], grid[2]),
        "line2": (grid[3], grid[4], grid[5]),
        "line3": (grid[6], grid[7], grid[8]),
        "line4": (grid[0], grid[3], grid[6]),
        "line5": (grid[1], grid[4], grid[7]),
        "line6": (grid[2], grid[5], grid[8]),
        "line7": (grid[0], grid[4], grid[8]),
        "line8": (grid[2], grid[4], grid[6]),
    }
    for i in range(1, 9):
        if win_cons[f"line{i}"] == ("x", "x", "x") or win_cons[f"line{i}"] == ("o", "o", "o"):
            if win_cons[f"line{i}"] == ("x", "x", "x"):
                print(player_1 + " wins!")
            elif win_cons[f"line{i}"] == ("o", "o", "o"):
                print(player_2 + " wins!")
            return False
    return True


def draw():
    if all(isinstance(i, str) for i in grid):
        return False
    else:
        return True


# While loop that runs the game, breaks out while loop once check() returns False or the grid is full.


while game_is_on:
    x_placement()
    os.system('cls||clear')
    show()
    if not check():
        game_is_on = False
        break
    if not draw():
        game_is_on = False
        print("It is a draw.")
        break
    o_placement()
    os.system('cls||clear')
    show()
    if not check():
        game_is_on = False
        break
