import random

# constants
WATER = '~'
SHIP = 'S'
HIT = 'H'
MISS = 'M'
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
grid_size = 6

'''
Legend
g = guess
p = player
c = computer
'''


class Board:
    '''
    6x6 grid will be created.
    axis will be added to the grid.
    battleships will be created and stored in ship_locations.
    '''
    def __init__(self):
        # initialises the grids for the boards
        self.grid_size = 6
        self.num_of_ships = 5
        self.grid = self.create_grid()
        self.add_axis_to_grid()
        self.ship_locs = []
        self.place_ships()

    def create_grid(self):
        # creates an 6x6 grid
        return [[WATER for i in range(self.grid_size)] for i in range(
            self.grid_size)]

    def add_axis_to_grid(self):
        # replace numbers at the top of grid to numbers
        self.grid[0] = [' '] + [str(i) for i in range(1, self.grid_size)]
        # replace first cell in each row with letters.
        for i in range(1, self.grid_size):
            self.grid[i][0] = LETTERS[i - 1]

    def place_ships(self):
        '''
        generates two random numbers for row and col,
        not including axis numbers.
        turns coordinate into a ship.
        adds coordinate to ship_locations.
        '''
        while len(self.ship_locs) < self.num_of_ships:
            row = random.randint(1, self.grid_size - 1)
            col = random.randint(1, self.grid_size - 1)
            if self.grid[row][col] != SHIP:
                self.grid[row][col] = SHIP
                self.ship_locs.append((row, col))


def title():
    print('******************************')
    print(' ---------Battleships---------')
    print('---The Computer has 5 ships---')
    print('---------Fire at Will!--------')
    print('******************************')


def print_boards_together(board1, board2):
    '''
    takes grid from both boards and prints them next to each other
    '''
    print("  -Player-          -Computer-")
    for row1, row2 in zip(board1.grid, board2.grid):
        print(' '.join(row1) + '        ' + ' '.join(row2))
    print('******************************')


def display_board(board):
    '''
    copies the inputted boards' grid
    replaces the ships with water to hide them
    '''
    display_grid = []
    for row in board.grid:
        display_row = []
        for i in row:
            if i == SHIP:
                display_row.append(WATER)
            else:
                display_row.append(i)
        display_grid.append(display_row)
    return display_grid


def get_p_g(grid_size):
    '''
    get player guess
    player inputs coordinate e.g. A1
    letter turned into number of index in LETTERS
    number changed from string to integer
    checks it is within the grid
    '''
    while True:
        # g = guess
        try:
            g = input("choose a coordinate to fire on (e.g A1): \n").upper()
            if len(g) != 2 or not g[0].isalpha() or not g[1].isdigit():
                raise ValueError("Not valid input")

            # changes letter to number and adjusts for axis
            g_row = LETTERS.index(g[0]) + 1
            # int not str
            g_col = int(g[1])

            if 1 <= g_row <= grid_size - 1 and 1 <= g_col <= grid_size - 1:
                print(f"You fired on {g}")
                return g_row, g_col
                break
            else:
                print(f"{g} is not on the grid")
        except ValueError:
            print(f"{g} is not on the grid")


def update_board(board, g_row, g_col, ship_locs):
    '''
    player guess is checked on the board.
    if it is a ship it becomes hit
    anything else it is a miss
    ship location removed from list
    '''
    if board[g_row][g_col] == SHIP:
        board[g_row][g_col] = HIT
        print("HIT!")
        print('******************************')
        ship_locs.remove((g_row, g_col))
    else:
        board[g_row][g_col] = MISS
        print("MISS!")
        print('******************************')


def validate_g(board, g_row, g_col):
    '''
    validate guess
    if the guess is WATER or SHIP it returns True
    if the guess is HIT or MISS returns False
    '''
    return board[g_row][g_col] not in [HIT, MISS]


def get_c_g(grid_size):
    '''
    get computer guess
    genterates random coordinate for the computer guess.
    '''
    g_row = random.randint(1, grid_size - 1)
    g_col = random.randint(1, grid_size - 1)
    return g_row, g_col


def convert_coordinates(row, col):
    # Convert row number to a letter (1 -> A, 2 -> B, etc.)
    row_letter = LETTERS[row - 1]
    # Combine row letter with column number
    coordinate = f"{row_letter}{col}"
    return coordinate


def check_game_over(p_ship_locs, c_ship_locs):
    if not c_ship_locs:
        print("You have sunk all of the computers ships. You Win!")
        return True

    if not p_ship_locs:
        print("The computer has sunk all of your ships. You lose!")
        return True


def main():
    '''
    creates player and computer board
    creates display board for computer
    changes the display computer board into a display version of computer board
    '''
    board_p = Board()
    board_c = Board()
    display_board_c = Board()
    # makes a hidden copy of the board_computer.grid
    display_board_c.grid = display_board(board_c)

    '''
    initial game start screen
    '''
    title()
    print_boards_together(board_p, display_board_c)

    '''
    game loop
    '''
    while True:
        while True:
            # player guess
            p_g_row, p_g_col = get_p_g(grid_size)
            if validate_g(board_c.grid, p_g_row, p_g_col):
                update_board(board_c.grid, p_g_row, p_g_col, board_c.ship_locs)
                break
            else:
                print("You have already guessed that location")

        while True:
            # computer guess
            c_g_row, c_g_col = get_c_g(grid_size)
            if validate_g(board_p.grid, c_g_row, c_g_col):
                c_g_coordinate = convert_coordinates(c_g_row, c_g_col)
                print(f"The computer fired on {c_g_coordinate}")
                update_board(board_p.grid, c_g_row, c_g_col, board_p.ship_locs)
                break

        # updates display board and reprints them
        display_board_c.grid = display_board(board_c)
        print_boards_together(board_p, display_board_c)
        print(' ')

        # checks for game over
        if check_game_over(board_p.ship_locs, board_c.ship_locs):
            break


main()