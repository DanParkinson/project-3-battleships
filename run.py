# constants
WATER = '~'

class Board:
    '''
    8x8 grid will be created
    axis will be added to the gird
    battleships will be created and stored in ship_locations
    '''
    def __init__(self):
        self.grid_size = 8
        self.grid = self.create_grid()
    
    def create_grid(self):
        '''
        creates an 8x8 grid
        '''
        grid = [[WATER for i in range(self.grid_size)] for i in range(self.grid_size)]
    
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
    pass

main()