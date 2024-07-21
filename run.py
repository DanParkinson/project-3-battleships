import random

'''
board_player and board_computer is created.
display_board_computer is given board_computers grid

player will guess a coordinate
player guess will be checked and validated against board_computer
board_computer will be updated with players guess
display_board will be updated with updated board_computer
print updated display_board_computer

computer will guess a coordinate.
computer guess will be checked and validated against board_player 
board_player updated and printed

jobs 
game over function to check when won

'''

# constants
WATER = '~'
SHIP = 'S'
HIT = 'H'
MISS = 'M'
LETTERS = ['A' ,'B' , 'C', 'D', 'E', 'F', 'G', 'H']
grid_size = 6

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
        self.ship_locations = [] # stores ship locations
        self.place_ships()
    
    def create_grid(self):
        # creates an 6x6 grid
        return [[WATER for i in range(self.grid_size)] for i in range(self.grid_size)]

    def add_axis_to_grid(self):
        # replace numbers at the top of grid to numbers
        self.grid[0] = [' '] +[str(i) for i in range(1, self.grid_size)]
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
        while len(self.ship_locations) < self.num_of_ships:
            row = random.randint(1, self.grid_size - 1)
            col = random.randint(1, self.grid_size - 1)
            if self.grid[row][col] != SHIP:
                self.grid[row][col] = SHIP
                self.ship_locations.append((row, col))

class Game:
    '''
    create a hidden board used for only displaying.
    print boards for user.
    get user guess.
    get computer guess.
    validate guess'.
    update player and computer boards.
    update hidden board.
    check for game over.
    '''
    pass

def print_grid(board):
    # used for testing until class game works
    for i in board.grid:
        print(' '.join(i))

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
        print( ' '.join(row1) + '        ' + ' '.join(row2))
    print('******************************')
    
def display_board(board):
    '''
    copies the inputed boards' grid
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

def get_player_guess(grid_size):
    '''
    player inputs coordinate e.g. A1
    letter turned into number of index in LETTERS
    number changed from string to integer
    checks it is within the grid
    '''
    while True:
        try:
            guess = input("choose a coordinate to fire on (e.g A1): ").upper()
            if len(guess) != 2 or not guess[0].isalpha() or not guess[1].isdigit():
                raise ValueError ("Not valid input")
            
            guess_row = LETTERS.index(guess[0]) + 1 # changes letter to number and adjusts for axis
            guess_col = int(guess[1]) # int not str

            if 1 <= guess_row <= grid_size - 1 and 1 <= guess_col <= grid_size - 1:
                print(f"You fired on {guess}")
                return guess_row, guess_col
                break
            else: 
                print(f"{guess} is not on the grid")
        except ValueError:
            print(f"{guess} is not on the grid")

def update_board(board, guess_row, guess_col, ship_locations):
    '''
    player guess is checked on the board.
    if it is a ship it becomes hit
    anything else it is a miss
    ship location removed from list
    '''
    if board[guess_row][guess_col] == SHIP:
        board[guess_row][guess_col] = HIT
        print("HIT!")
        print('******************************')
        ship_locations.remove((guess_row, guess_col))
    else:
        board[guess_row][guess_col] = MISS
        print("MISS!")
        print('******************************')

def validate_guess(board, guess_row, guess_col):
    '''
    if the guess is WATER or SHIP it returns True
    if the guess is HIT or MISS returns False
    '''
    return board[guess_row][guess_col] not in [HIT, MISS]

def get_computer_guess(grid_size):
    '''
    genterates random coordinate for the computer guess. 
    '''
    guess_row = random.randint(1, grid_size - 1)
    guess_col = random.randint(1, grid_size - 1)
    return guess_row, guess_col

def convert_coordinates(row, col):
    # Convert row number to a letter (1 -> A, 2 -> B, etc.)
    row_letter = LETTERS[row - 1]
    # Combine row letter with column number
    coordinate = f"{row_letter}{col}"
    return coordinate

def check_game_over(player_ship_locations, computer_ship_locations):
    if not computer_ship_locations:
        print("You have sunk all of the computers ships. You Win!")
        return True # game over

    if not player_ship_locations:
        print("The computer has sunk all of your ships. You lose!")
        return True # game over

def main():
    '''
    creates player and computer board 
    creates display board for computer 
    changes the display computers board into a display version of computer board
    '''
    board_player = Board()
    board_computer = Board()
    display_board_computer = Board()
    # makes a hidden copy of the board_computer.grid
    display_board_computer.grid = display_board(board_computer)

    '''
    initial game start screen
    '''
    title()
    print_boards_together(board_player, display_board_computer)
    print(board_computer.ship_locations)

    '''
    game loop
    '''
    while True:
        while True:
            #player guess
            player_guess_row, player_guess_col = get_player_guess(grid_size)
            if validate_guess(board_computer.grid, player_guess_row, player_guess_col): #checks True False
                update_board(board_computer.grid, player_guess_row, player_guess_col, board_computer.ship_locations)
                break
            else:
                print("You have already guessed that location")
            
        while True:
            # computer guess
            computer_guess_row, computer_guess_col = get_computer_guess(grid_size)
            if validate_guess(board_player.grid, computer_guess_row, computer_guess_col): #checks True False
                computer_guess_coordinate = convert_coordinates(computer_guess_row, computer_guess_col)
                print(f"The computer fired on {computer_guess_coordinate}")
                update_board(board_player.grid, computer_guess_row, computer_guess_col, board_player.ship_locations)
                break

        # updates display board and reprints them
        display_board_computer.grid = display_board(board_computer)
        print_boards_together(board_player, display_board_computer)

        # checks for game over
        if check_game_over(board_player.ship_locations, board_computer.ship_locations):
            break
        
main()