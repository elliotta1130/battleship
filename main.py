from random import randint

class Board:
    """This represents a board of the game"""
    def __init__(self, size):
        self.board = []
        for x in range(size):
            self.board.append(["O"] * size)
        self.ship_row = randint(0, len(self.board) - 1)
        self.ship_col = randint(0, len(self.board[0]) - 1)
    def print_board(self):
        for row in self.board:
            print " ".join(row)
    def print_ship_location(self):
        print self.ship_row, self.ship_col
    def is_hit(self, row, col):
        # TODO: complete this
        print 'todo'
    
    
print 'testing new boards'
b1 = Board(5)
b2 = Board(5)

b1.print_ship_location()
b2.print_ship_location()


print "Let's play Battleship!"

for turn in range(4):
    whosturn = turn % 2
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    board = None
    if whosturn == 1:
        board = b1
    else:
        board = b2

    board.is_hit(guess_row, guess_col)
    
    # TODO: move this code to is_hit
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0          
	or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            if turn == 3:
                print "Game Over"
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
        turn = turn + 0   
        print "turn {}".format(turn + 1)
        board.print_board()