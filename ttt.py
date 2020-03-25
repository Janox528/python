'''''''''''''''''''''''''''
    A simple Tic Tac Toe
'''''''''''''''''''''''''''

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [ [' ' for x in range(0,self.size)] for y in range(0,self.size) ]

    def displayBoard(self):
        for row in self.grid:
            row_temp = ""
            for symbol in row:
                if symbol == " ":
                    row_temp += "_ "
                else:
                    row_temp += symbol + " "
            print(row_temp)

def checkWinCondition(board):
    # Check rows
    
    won = False

    if ['X']*board.size in board.grid or ['O']*board.size in board.grid:
        won = True
    

    # Check columns
    
    for j in range(board.size):
        if [board.grid[i][j] for i in range(board.size)] in [['X']*board.size,['O']*board.size]:
            won = True

    # Check diagonal \
    
    if [board.grid[i][i] for i in range(board.size)] in [['X']*board.size,['O']*board.size] or [board.grid[board.size-1-i][i] for i in range(board.size)] in [['X']*board.size,['O']*board.size]:
        won = True

    # Check diagonal /
    
    m = 0
    n = board.size - 1
    matches = 0
    symbol = board.grid[0][board.size - 1]
    while (m < board.size and n >= 0):
        if (symbol == board.grid[m][n] and symbol != ' '):
            matches += 1
        if matches >= board.size:
            print('You won')
            print('diagonal /')
            won = True
        m += 1
        n -= 1

def displayMenu():
    pass

def main():
    board = Board(3)
    #board.grid[0][0] = 'X'
    board.grid[0][1] = 'X'
    board.grid[0][2] = 'O'
    #board.grid[2][1] = 'X'
    board.grid[1][1] = 'O'
    board.grid[2][2] = 'X'
    board.grid[2][0] = 'O'
    board.displayBoard()
    checkWinCondition(board)

if __name__ == '__main__':
    main()
