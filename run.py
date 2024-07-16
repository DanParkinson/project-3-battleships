import random

# constants
WATER = '~'
SHIP = 'S'
LETTERS = ['A' ,'B' , 'C', 'D', 'E', 'F', 'G', 'H']

class Board:
    '''
    8x8 grid will be created
    axis will be added to the gird
    battleships will be created and stored in ship_locations
    '''
    def __init__(self):
        self.grid_size = 8
        self.grid = self.create_grid()
        self.add_axis_to_grid()
        self.place_ships()
    
    def create_grid(self):
        '''
        creates an 8x8 grid
        '''
        return [[WATER for i in range(self.grid_size)] for i in range(self.grid_size)]
        
    def print_grid(self):
        # used for testing until class game works
        for i in self.grid:
            print(' '.join(i))

    def add_axis_to_grid(self):
        # replace numbers at the top of grid to numbers
        self.grid[0] = [' '] +[str(i) for i in range(1, self.grid_size)]
        # replace first cell in each row with letters.
        for i in range(1, self.grid_size):
            self.grid[i][0] = LETTERS[i - 1]

    def place_ships(self):
        row = random.randint(1, self.grid_size - 1)
        col = random.randint(1, self.grid_size - 1)
        if self.grid[row][col] != SHIP:
            self.grid[row][col] = SHIP

    
class Game:
    '''
    create a hidden board used for only displaying
    print boards for user
    get user guess
    get computer guess
    validate guess'
    update player and computer boards
    update hidden board
    check for game over
    '''
    pass

def main():
    '''
    main function for playing game
    '''
    board = Board()
    board.print_grid() #used for testing

main()