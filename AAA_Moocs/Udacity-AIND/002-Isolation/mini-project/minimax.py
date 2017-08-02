from copy import deepcopy



class GameState(object):

    def __init__(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim

        # Represent the game
        self._board = [[0] * ylim for _ in range(xlim)]
        self._parity = 0
        self._player_locations = [None, None]

    def forecast_move(self, move):
        if move not in self.get_legal_moves():
            raise RuntimeError('Tried to forecast an illegal move')
        # Create a copy of the Board to be changed
        newBoard = deepcopy(self)
        # Mark the move on the new board
        newBoard._board[move[0]][move[1]] = 1
        # Update player location for the current player
        newBoard._player_locations[self._parity] = move
        # Change the parity to the other player
        newBoard._parity ^= 1
        # return the newBoard State
        return newBoard
    
    def get_legal_moves(self):
        loc =self._player_locations[self._parity]
        if not loc:
            return self._get_blank_spaces()
        moves = []
        rays = [(1,0), (1,-1), (0,1), (-1,1), (-1,0), (-1,1), (0,1), (1,1)]
        for dx, dy in rays:
            _x, _y = loc
            while 0 <= _x + dx < self.xlim and 0 <= _y + dy < self.ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]:
                    break
                moves.append((_x, _y))
        return moves

    
    def _get_blank_spaces(self):
        return [(x,y) for x in range(xlim) for y in range(ylim) if self._board[x][y] == 0 ]

    
    # Implement the MinMax Algorithm
    def terminal_test(self, game):
        return not bool(game.get_legal_moves())

    def min_value(self, game):
        if self.terminal_test(game):
            return 1
        min_v = float('inf')
        for m in game.get_legal_moves():
            min_v = min(min_v, self.max_value(game.forecast_move(m)))
        return min_v

    def max_value(self, game):
        if self.terminal_test(game):
            return -1
        max_v = float('-inf')
        for m in game.get_legal_moves():
            max_v = max(max_v, self.min_value(game.forecast_move(m)))
        return max_v
    

    def minmax(self, game):
        max_v, best_move = float('-inf'), None
        for m in game.get_legal_moves():
            if self.min_value(game.forecast_move(m)) > max_v:
                max_v = self.min_value(game.forecast_move(m))
                best_move = m
        return best_move



# Initiate the Game
xlim = 2
ylim = 3

g = GameState(xlim, ylim)
print('Testing the Forecasting Function')
print(g.forecast_move((0,1)).get_legal_moves())
print('Testing the min_value Function')
print(g.min_value(g))
print(g.max_value(g))

if g.min_value(g) == 1 and g.max_value(g) == -1:
    print('Max and Min Functions passed')
print('Testing the MinMax Decission Function')

best_moves = set([(0,0), (2,0), (0,1)])
rootNode = GameState(xlim, ylim)
minmax_node = rootNode.minmax(rootNode)

print('Best move choices: {}'.format(best_moves))
print('Move chosen: {}'.format(minmax_node))

if minmax_node in best_moves:
    print('Test passed')