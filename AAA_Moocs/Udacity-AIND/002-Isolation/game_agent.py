"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """The best implementation



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
    return custom_score_2(game, player)


def custom_score_2(game, player):
    """Implements a proportional of the moves available to the player 
    given the overall number of possible moves. 
    
    Goal:
    => Maximize steps that maximize the possible difference in abbility
    to move while minimizing the opponents possibilities, while keeping
    as close as possible to the central positions

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
    # Check if game is won or lost 
    if game.is_winner(player) or game.is_loser(player):
        return game.utility(player) 

    # Maximize the centrality
    centrality = centrality(game, player)
    # Maximize owns proportion of available moves
    prop_moves = float(numberMoves(game, player) / openMoves)
    
    # Calculate a weighted combination of prop moves and centrality
    score = float(prop_moves + centrality)
    print(score)
    return score

def custom_score_3(game, player):
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
    if game.is_loser() or game.is_winner():
        return game.utility(player)

    return centrality(game, player)
    

# Different Scoring Mechanisms
def openMoves(game, player):
    """
    Basic evaluation function counting the number of available moves for the 
    player on the board
        """

    return float(len(game.get_legal_moves(player)))
    

def centrality(game, player, closeness=10):
    """
    Calculates the difference in centrality a given move will result in
    """
    
    # Calculate the positions
    center_x, center_y = int(game.height/2), int(game.widht/2)
    player_x, player_y = game.get_player_location(player)
    opponent_x, opponent_y = game.get_player_location(game.get_opponent(player))

    # Calculate Distance
    player_dist = abs(player_x - center_x) + abs(player_y - center_y)
    opponent_dist = abs(opponent_x - center_x) + abs(opponent_y - center_y)

    return float(player_dist - opponent_dist*closeness)

def numberMoves(game, player, closeness=1):
    """
    A weighted difference function evaluating the difference in available number of moves for both
    players given the current state of the game.
    """
    # Calculate the available moves to both parties
    numMyMoves = len(game.get_legal_moves())
    numOpMoves = len(game.get_legal_moves(game.get_opponent(player)))

    # return a weighted difference based on the amount of closeness we want to introduce
    return float(numMyMoves - closeness * numOpMoves)

def propMoves(game, player):
    """
    Calculates a weighted
    """


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

    def get_move(self, game, time_left):
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

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            best_move = self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth, maxplayer=True):
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

        # Get the legal moves
        legal_moves = game.get_legal_moves()

        # Check if we still have moves available
        if not legal_moves:
            if maxplayer:
                return (-1,-1)
            else:
                return (-1,-1)


        # Initialize the values
        best_move = (-1,-1)
        min_score, max_score = float("inf"), float("-inf")


        # Check if we reached max_iterative depth
        if depth == 1:
            # Iterate over all possibilities
            if maxplayer:
                for move in legal_moves:
                    # score the move
                    score = self.score(game.forecast_move(move), self)
                    # Check if better move has been found
                    if score > max_score:
                        max_score, best_move = score, move
                return best_move

            else:
                for move in legal_moves:
                    # Score the move
                    score = self.score(game.forecast_move(move), self)
                    # Check if better move has been found
                    if score < min_score:
                        min_score, best_move = score, move
                return best_move

        # Else keep going
        if maxplayer:
            for move in legal_moves:
                score,_ = self.minimax(game.forecast_move(move), depth-1, maxplayer=False)

                if score == float("inf"):
                    # We found a winning branch
                    return score, move
                # Check if this one is an improvement
                if score > max_score:
                    max_score, best_move = score, move
            return  best_move
        
        else:
            for move in legal_moves:
                score,_ = self.minimax(game.forecast_move(move), depth-1, maxplayer=True)

                if score == float("-inf"):
                    # We found a surely loosing branch!
                    return score, move
                # Check if its a negative improvement
                if score < min_score:
                    min_score, best_move = score, move
            return  best_move
            

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

        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return (-1,-1)
        return legal_moves[0]
             
        

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



