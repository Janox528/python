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

    def checkWinCondition(self,player):
        # Check rows
        # player = 'X' oder 'O'

        if [player]*self.size in self.grid:
            return True
        

        # Check columns
        for j in range(self.size):
            if [self.grid[i][j] for i in range(self.size)] == [player]*self.size:
                return True

        # Check diagonal \
        if [self.grid[i][i] for i in range(self.size)] == [[player]*self.size] or \
            [self.grid[self.size-1-i][i] for i in range(self.size)] == [[player]*self.size]:
            return True
        
        return False



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
    print(board.checkWinCondition('O'))

if __name__ == '__main__':
    main()
