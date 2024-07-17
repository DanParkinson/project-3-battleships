import random

# constants
WATER = '~'
SHIP = 'S'
LETTERS = ['A' ,'B' , 'C', 'D', 'E', 'F', 'G', 'H']
grid_size = 5

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
    for row1, row2 in zip(board1, board2):
        print( ' '.join(row1) + '    ' + ' '.join(row2))

def main():
    '''
    main function for playing game.
    '''
    title()

    #creates player and computer boards
    board_player = Board()
    board_computer = Board()

    #prints player board
    #print_grid(board_player)
    #print(board_player.ship_locations)

    # prints computer board
    #print_grid(board_computer)
    #print(board_computer.ship_locations)

    '''
    testing.
    print boards together functions but wont pull grids out of class Board. 
    board1 and board2 are used for testing purposes. 
    '''
    board1 = [[WATER for i in range(grid_size)] for i in range(grid_size)]
    board2 = [[WATER for i in range(grid_size)] for i in range(grid_size)]
    print_boards_together(board1, board2)


main()