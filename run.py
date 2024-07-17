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
player and computer guesses inputted and validated

player board and computer board updated
display board updated

game over functionn to check when won

'''

# constants
WATER = '~'
SHIP = 'S'
LETTERS = ['A' ,'B' , 'C', 'D', 'E', 'F', 'G', 'H']

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
    for row1, row2 in zip(board1.grid, board2.grid):
        print( ' '.join(row1) + '        ' + ' '.join(row2))

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

def main():
    '''
    main function for playing game.
    '''
    
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
    #prints player board and the display computer board
    print_boards_together(board_player, display_board_computer)

    '''
    testing
    '''
    #print(board_player.ship_locations)
    #print(board_computer.ship_locations)
    #print(display_board_computer.ship_locations)

main()