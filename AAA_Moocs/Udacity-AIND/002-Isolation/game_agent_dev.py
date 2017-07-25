"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return custom_score2(game, player, 1)
    # score =  self.heuristic_centrality(game, player)

def custom_score2(game, player, opCloseness=1):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Check if game is already won or lost at this stage
    if game.is_winner(player) or game.is_loser:
        return game.utility(player)

    # If not yet closed, evaluate the possible moves for the opponents
    myMoves = len(game.get_legal_moves(player))
    opMoves = len(game.get_legal_moves(game.get_opponent(player)))
    # Return the difference weighted by the amount of aggressiveness we want to apply
    score =  float(myMoves - opCloseness * opMoves )
    print(score)
    return score




def heuristic_centrality(game, player):
    """Calculate the distance the next possible move takes the player away from the 
    Center of the board

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Check if game is already won or lost at this stage
    if game.is_winner(player) or game.is_loser:
        return game.utility(player)

    # Retrieve the current location for the player
    r,c = game.get_player_location(player)
    # Calculate the distance to the center square (3,3)
    return sum(abs(r-3), abs(c-3))
    


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left, iterativeDeepening=False):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        # Check if we have moves left
        if not game.get_legal_moves():
            return (-1,-1)

        # Use iterative deepening / normal minmax to search the best move
        try:
            if iterativeDeepening:
                iterative_depth = 1
                while True:
                    best_score, best_move = self.minimax(game, iterative_depth)
                    if best_score == float("inf") or best_score == float("-inf"):
                        break
                    iterative_depth += 1
                return best_move
            else:
                _, best_move = self.minimax(game, self.search_depth)

        except SearchTimeout:

            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        
        return best_move

    def minimax(self, game, depth, maxPlayer=True):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()


        # Check for all available moves
        legal_moves = game.get_legal_moves()
        print(legal_moves)

        # Check if there are still moves available
        if not legal_moves:
           if maxPlayer:
               return float("-inf")
           else:
               return float("inf")

        # If there are moves available initialize the search for best action
        min_score, max_score = float("inf"), float("-inf")
        best_move = (-1, -1)

        # If we reached the last iteration of search

        if depth == 1:
            print('Entering the last Evaluation Step at depth {}'.format(depth))
            print(legal_moves)

            # Implement strategy to maximize Utility
            if maxPlayer:
                print("i am playing as maximiging player {}".format(maxPlayer))
                for move in legal_moves:
                    # Create a deep copy of the board with the move applied, and score it
                    score = self.score(game.forecast_move(move), self)
                    if score == float('inf'):
                        return score, move
                    # If the current move is better than the best we saw so far, store it
                    if score > max_score:
                        max_score, best_move = score, move
                print(best_move)
                return max_score, best_move
            
            # We are simulating opponents move (Trying to minimize the resulting Utility)
            else:
                # Iterate over all possible legal moves for the given state
                for move in legal_moves:
                    # Create a deep copy of the board with the move applied, and score it
                    score = self.score(game.forecast_move(move), self)
                    if score == float("-inf"):
                        return score, move
                    # If the move is less than the current min_score keep it
                    if score < min_score:
                        min_score, best_move = score, move
                print(best_move)
                return min_score, best_move 


        # We have not yet reached our final search depth -> Search all available moves from the 
        # Current State
        if maxPlayer:
            for move in legal_moves:
                # For each possible move we search the 
                print("Playing maximing Player at depth {}".format(depth))
                score,_ = self.minimax(game.forecast_move(move), depth-1, maxPlayer=False)
                # Check if we found a winner
                if score == float('inf'):
                    return score, move
                # Else check if it is the best option so far
                if score > max_score:
                    max_score, best_move = score, move
            return max_score, best_move

        else:
            # We iterate over the all possible moves as the opponent
            for move in legal_moves:
                print("Playing minimizing Player at depth {}".format(depth))
                score,_ = self.minimax(game.forecast_move(move), depth-1, maxPlayer=True)
                if score == float("-inf"):
                    return move
                if score < min_score:
                    min_score, best_move = score, move
            return min_score, best_move



class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        return 

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        raise NotImplementedError




from isolation import Board
from sample_players import GreedyPlayer
from sample_players import RandomPlayer

# create an isolation board (by default 7x7)
player1 = MinimaxPlayer()
player2 = RandomPlayer()
game = Board(player1, player2)

# place player 1 on the board at row 2, column 3, then place player 2 on
# the board at row 0, column 5; display the resulting board state.  Note
# that the .apply_move() method changes the calling object in-place.
game.apply_move((2, 3))
game.apply_move((0, 5))
print(game.to_string())

# players take turns moving on the board, so player1 should be next to move
assert(player1 == game.active_player)

# get a list of the legal moves available to the active player
print(game.get_legal_moves())

# get a successor of the current state by making a copy of the board and
# applying a move. Notice that this does NOT change the calling object
# (unlike .apply_move()).
new_game = game.forecast_move((1, 1))
assert(new_game.to_string() != game.to_string())
print("\nOld state:\n{}".format(game.to_string()))
print("\nNew state:\n{}".format(new_game.to_string()))

# play the remainder of the game automatically -- outcome can be "illegal
# move", "timeout", or "forfeit"
winner, history, outcome = game.play()
print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
print(game.to_string())
print("Move history:\n{!s}".format(history))