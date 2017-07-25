
# Set the possible search strategies for the players to follow
STRATEGIES = [
    'greedy',
    'random',
    'aStar'
]

# Players
class Player(object):
    # 
    def __init__(self, type_player=STRATEGIES):
        """
        Initialize the Player to play a specific strategy
        """
        self.strategy = type_player
        pass

    def move(self, board):
        """
        Given a certain state of the board, perform the best action to take.
        """
        pass



class Isolation(object):

    def __init__(self):
        """
        Initialize the Game with two 
        """
        self.stone1 = 'O'
        self.stone2 = 'X'
        self.player1 = None
        self.player2 = None
        self.active_player = 1



    def display(self):
        """
        Visualizes the Gameboard to the player
        """
        print('Round 1 - Active Player {}'.format(self.active_player))
        for row in self.row_units:
            print('-'*len(row*4))
            print("|", " | ".join([self.board[box] for box in row]), '|')
            
            # print(" | ".join([self.board[box] for box in row]))
        print('-'*len(row*4))
            

    def setupBoard(self):
        """
        Given the dimensions of the board this function creates a representiaton and 
        exports the board as a dict with all values initialized as an empty dict.

        The keys are (A1 -> E7) and the values: {'A1': None} at the beginning
        When Player 1 takes a spot -> {'A2':'O'}
        Once a field has taken on a value it is no longer available to be chose in valid moves
        """
        # Helper Functions for Board Creation
        def cross(a,b):
            return [s+t for s in a for t in b]
        
        # Representing the board
        COLS = 'ABCDE'
        ROWS = '12345'

        boxes = cross(COLS, ROWS)
        # print(boxes)
        self.col_units = [[c+r for r in ROWS] for c in COLS]
        self.row_units = [[c+r for c in COLS] for r in ROWS]

        # Generate all possible diagonals across the field (To be able to draw diagonals for each field of the board)
        # From top-left over the cols
        self.diagonals_tl_c = [[c+r for c,r in zip(COLS[i:], ROWS[i:])] for i in range(len(COLS))]
        # From top-left over the rows
        self.diagonals_tl_r = [[c+r for c,r in zip(COLS[:j], ROWS[i:])] for i,j in zip(range(len(COLS)), range(len(COLS)+1)[::-1])] 
        # From bottom-left over the columns
        self.diagonals_bl_c = [[c+r for c,r in zip(COLS[j:], ROWS[::-1])] for i,j in zip(range(len(COLS)+1)[::-1], range(len(COLS)))]
        # From bottom-left over the rows
        self.diagonals_bl_r = [[c+r for c,r in zip(COLS[:i], ROWS[:i][::-1])] for i,j in zip(range(len(COLS)+1)[::-1], range(len(COLS)))]
        # self.diagonals_bl_u

        # Combine all possible units
        self.unitlist = self.col_units + self.row_units + self.diagonals_tl_c + self.diagonals_tl_r + self.diagonals_bl_c + self.diagonals_bl_r
        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in boxes)
        self.peers = dict((s, set(sum(self.units[s], []))-set([s])) for s in boxes)
        
        # Create the empty board dict
        board = {k:'.' for k in boxes }
        
        # Testprintouts
        # print(col_units)
        # print(row_units)
        # print(diagonals_main)
        # print(self.diagonals_tl_c)
        # print(self.diagonals_tl_r)
        # print(self.diagonals_bl_c)
        # print(self.diagonals_bl_r)

        # Save the board to the instance
        self.board = board

    def validMoves(self, position):
        """
        Given the current state of the board a list of valid moves for a given player is returned
        """

        # given the current location find get all peers
        possible_moves = self.peers[position]

        # restrict the moves given already taken positions

        return possible_moves

    def makeMove(self, position):
        """
        Given the current situation, it calculates the best possible action to take and updates the position
        of the player in the new state
        """
        # Calculate the best possible action given the current state

        # Mark the final position as taken
        self.board[position] = self.active_player.
        # Update the players current position to the new location
        self.active_player.position = position
        # Return the updated state


    def play(self, player1, player2, humanplayer=1, size=(7,7), startingPlayer=1):
        """
        The main function controlling the game
        """
        # Initialize the board
        self.setupBoard(size)
        # Check for players
        assert isinstance(player1, Player)
        assert isinstance(player2, Player)
        self.player1, self.player2 = player1, player2
        

        # Set the chosen starting Player as active
        self.active_player = player1 if startingPlayer==1 else player2

        # Start game!!
        while True:
            # If current player is human controlled
            if self.active_player == humanplayer:
                # Take input
                position = input('Choose your next location: ')
                # Make the move
                self.makeMove(position)



        # If no player yet active




Isolation = Isolation()
Isolation.setupBoard()
print(Isolation.validMoves('A5'))
# Isolation.display()