import random


class GameGrid:
    def __init__(self, grid):
        self.grid = grid

    def get_letters_to_numbers_list_list():
        letters_to_numbers_list = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
        }
        return letters_to_numbers_list

    def print_grid(self):
        print(
            """

    ------------------------------------------------------
         _ __        _   _   _           _     _   
        |  _ \      | | | | | |         | |   (_) 
        | |_)/  __ _| |_| |_| | ___  ___| |__  _ _ __   
        |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
        | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
        |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                                | |  
                                                |_| 
    ------------------------------------------------------

                    H O W  T O  P L A Y:

    1. Your computer will randomly generate 5 Battleships,
    across the grid.
    2. You will have 30 guesses per game.
    3. The player must select a row (1, 2, 3...),
    and then a column (A, B, C...),
    in order to guess the coordinates.
    4. The player must try and sink the entire fleet,
    before they run out of guesses.
    5. Sunken ships are marked with an "X."
    6. Missed ships are marked with a "0."

        B  A  T  T  L  E   S  T  A  T  I  O  N  S  ! !
    """
        )
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_num = 1
        for row in self.grid:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class Battleship:
    def __init__(self, grid):
        self.grid = grid

    def generate_ships(self):
        for i in range(5):
            x_col, y_row = random.randint(0, 7), random.randint(0, 7)
            while self.grid[x_col][y_row] == "X":
                x_col, y_row = random.randint(0, 7), random.randint(0, 7)
            self.grid[x_col][y_row] = "X"
        return self.grid

    def get_player_input(self):
        try:
            x_col = input("Enter Ship Row:\n")
            while x_col not in "12345678":
                print("ERROR - please select a valid row")
                x_col = input("Enter Ship Row:\n")

            y_row = input("Enter Ship Column:\n").upper()
            while y_row not in "ABCDEFGH":
                print("ERROR - please select a valid column")
                y_row = input("Enter Ship Column:\n").upper()
            return (
                int(x_col) - 1,
                GameGrid.get_letters_to_numbers_list_list()[y_row],
            )
        except ValueError and KeyError:
            print("ERROR - Invalid Input")
            return self.get_player_input()

    def count_ship_hits(self):
        ship_hits = 0
        for row in self.grid:
            for column in row:
                if column == "X":
                    ship_hits += 1
        return ship_hits


def StartGame():
    computer_grid = GameGrid([[" "] * 8 for i in range(8)])
    player_guess_grid = GameGrid([[" "] * 8 for i in range(8)])
    Battleship.generate_ships(computer_grid)
    # starts the game's 30 goes.
    goes = 30
    while goes > 0:
        GameGrid.print_grid(player_guess_grid)
        # gets the user input
        user_x_col, user_y_row = Battleship.get_player_input(object)
        # check if guess is a duplicate of the previous guess.
        while (
            player_guess_grid.grid[user_x_col][user_y_row] == "0"
            or player_guess_grid.grid[user_x_col][user_y_row] == "X"
        ):
            print("You already guessed those coordinates!")
            user_x_col, user_y_row = Battleship.get_player_input(object)
        # checks if ship is hit or missed.
        if computer_grid.grid[user_x_col][user_y_row] == "X":
            print("You sunk my Battleship!")
            player_guess_grid.grid[user_x_col][user_y_row] = "X"
        else:
            print("You missed my Battleship!")
            player_guess_grid.grid[user_x_col][user_y_row] = "0"
        # checks if the user has won the game or not.
        if Battleship.count_ship_hits(player_guess_grid) == 5:
            print("You sunk my entire Fleet!!")
            break
        else:
            goes -= 1
            print(f"{goes} guesses remaining")
            if goes == 0:
                print("You ran out of guesses!!")
                GameGrid.print_grid(player_guess_grid)
                break


if __name__ == "__main__":
    StartGame()
