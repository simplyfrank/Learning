import numpy as np

# SET VARIABLES
LENGTH = 3

def get_state_hash_and_winner(env, i=0, j=0):
    results = []

    for v in (0, env.x, env.o):
        env.board[i,j] = v
        if j == 2:
            # j goes back to 0, increse i, unless i == 2, then we are done
            if i == 2:
                #  the board is full, collect results and return
                state = env.get_state()
                ended = env.game_over(force_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_hash_and_winner(env, i+1, 0)
        else:
            # increment j, i stays the same
            results += get_state_hash_and_winner(env, i, j + 1)
    
    return results


def initialV_x(env, state_winner_triples):
    # initialize state values as follows
    # if x wins, V(s) = 1
    # if x loses or draw, V(s) = 0
    # otherwise, V(s) = 0.5
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.x:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V
    
def initialV_o(env, state_winner_triples):
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.o:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V

class Agent(object):
    def __init__(self, eps=0.1, alpha=0.5):
        self.eps = eps
        self.alpha = alpha
        self.verbose = False
        self.state_history = []

    def setV(self, V):
        '''initialize the value function'''
        self.V = V
    
    def set_symbol(self, sym):
        '''Set the symbol for the Agent to use'''
        self.sym = sym

    def set_verbose(self, v):
        '''prints more information is verbose==True'''
        self.verbose = v

    def reset_history(self):
        '''keep track of state history during an episode. After episode is done, 
           this is used to reset the agents history
        '''
        self.state_history = []

    def take_action(self, env):
        '''choose an action based on the epsilon-greedy strategy'''
        r = np.random.rand()
        best_state = None
        if r < self.eps:
            # take a random action based 
            if self.verbose:
                print("Taking a random action")
            
            possible_moves = []
            for i in range(LENGTH):
                for j in range(LENGTH):
                    if env.is_empty(i,j):
                        possible_moves.append((i,j))
            idx = np.random.choice(len(possible_moves))
            next_move = possible_moves[idx]
        else:
            pos2value = {} # for debugging
            next_move = None
            best_value = -1
            for i in range(LENGTH):
               for j in range(LENGTH):
                   if env.is_empty(i, j):
                       # Checking what the state would be if we made this move?
                       env.board[i,j] = self.sym
                       state = env.get_state()
                       # Changing it back to 0
                       env.board[i,j] = 0
                       pos2value[(i,j)] = self.V[state]
                       if self.V[state] > best_value:
                           best_value = self.V[state]
                           best_state = state
                           next_move = (i,j)
            # if verbose, draw the board w/ the values
            if self.verbose:
                print("Taking a greedy action")
                # print Board with Values
                for i in range(LENGTH):
                    print("-------------")
                    for j in range(LENGTH):
                        if env.is_empty(i, j):
                            print("%.2f |" % pos2value[(i,j)], end='')
                        else:
                            print(" ", end='')
                            if env.board[i,j] == env.x:
                                print("x |", end="")
                            elif env.board[i,j] == env.o:
                                print('o |', end='')
                            else:
                                print(' |', end='')
                    print("")
                print("-------------")
        # make the move
        env.board[next_move[0], next_move[1]] = self.sym

    def update_state_history(self, s):
        '''adds state to state history'''
        self.state_history.append(s)

    def update(self, env):
        '''queries environment for latest reward at the end of an episode'''
        reward = env.reward(self.sym)
        target = reward
        for prev in reversed(self.state_history):
            value = self.V[prev] + self.alpha*(target - self.V[prev])
            self.V[prev] = value
            target = value
        self.reset_history()

class Environment(object):
    def __init__(self):
        self.board = np.zeros((LENGTH, LENGTH))
        self.x = -1 # Represents an x on the board, Player 1
        self.o = 1 # Represents an o on the board, Player 2
        self.winner = None
        self.ended = False
        self.num_states = 3**(LENGTH*LENGTH)
    
    def is_empty(self, i, j):
        '''Checks if the board at position [i,j] is 0 '''
        return self.board[i,j] == 0
    
    def reward(self, sym):
        # No reward until the game is over
        if not self.game_over():
            return 0

        # if we get here game is over
        # sym will be self.x or self.o
        return 1 if self.winner == sym else 0
    
    def get_state(self):
        k = 0 
        h = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] ==self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2
                h += (3**k) * v
                k += 1
        return h
    
    def game_over(self, force_recalculate=False):
        if not force_recalculate and self.ended:
            return self.ended
        
        # Check rows
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
        
        # check columns
        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:, j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        # check diagnonals
        for player in (self.x, self.o):
            # top-left -> bottom-right diagonal
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            # top-right -> bottom-left diagonal
            if np.fliplr(self.board).trace() == player*LENGTH:
                self.winner = player
                self.ende = True
                return True
        
        if np.all((self.board == 0) == False):
            # winner stays None
            self.winner = None
            self.ended = True
            return True
        
        # game is not over
        self.winner = None
        return False
    
    def is_draw(self):
        return self.ended and self.winner is None

    def draw_board(self):
        '''Print a drawn out version to the screen'''
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("| ", end="")
                if self.board[i,j] == self.x:
                    print("x ", end=""),
                elif self.board[i,j] == self.o:
                    print('o ', end=""),
                else:
                    print("  ", end=""),
            print("")
        print("-------------")

class Human(object):
    def __init__(self):
        pass
    
    def set_symbol(self, sym):
        self.sym = sym
    
    def take_action(self, env):
        while True:
            # break if we make a legal move
            move = input("Enter coordinates i,j for your next move: ")
            i, j = move.split(',')
            i = int(i)-1
            j = int(j)-1
            if env.is_empty(i,j):
                env.board[i,j] = self.sym
                break
            else:
                print('This box is already taken, please choose another one: ')
    
    def update(self, env):
        pass
    
    def update_state_history(self, s):
        pass


def play_game(p1, p2, env, draw=False):
    # loops until the game is over
    current_player = None
    while not env.game_over():
        # alternate between players
        # p1 starts first
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

        # draw the board befor the user who wants to see it makes a move
        if draw:
            if draw == 1 and current_player == p1:
                env.draw_board()
            if draw == 2 and current_player == p2:
                env.draw_board()

        # current player makes his move
        current_player.take_action(env)

        # update state histories
        state = env.get_state()
        p1.update_state_history(state)
        p2.update_state_history(state)

    if draw:
        env.draw_board()
    
    # do the value function update
    p1.update(env)
    p2.update(env)

# The Main Function to train the AI
if __name__ == "__main__":
    # train the agent
    p1 = Agent()
    p2 = Agent()

    # set the initial V for p1 and p2
    env = Environment()
    state_winner_triples = get_state_hash_and_winner(env)

    Vx = initialV_x(env, state_winner_triples)
    p1.setV(Vx)
    Vo = initialV_o(env, state_winner_triples)
    p2.setV(Vo)

    # give each player their symbol
    p1.set_symbol(env.x)
    p2.set_symbol(env.o)

    # Now we play 10000 games to train the Agents
    T = 20000
    for t in range(T):
        if t % 200 == 0:
            print(t)
        play_game(p1, p2, Environment())


    # Playing the computer
    human = Human()
    human.set_symbol(env.o)
    while True:
        p1.set_verbose(True)
        play_game(human, p1, Environment(), draw=1)

        answer = input("Play again? [Y/n]:")
        if answer and answer.lower()[0] == 'n':
            break

# env = Environment()
# print(env.board)
# print(env.num_states)
# print(env.ended)
# print(env.winner)
# print(env.x)
# print(env.o)
# print(env.reward(env.o))
# print(env.get_state())
# print(env.game_over())

# p1 = Agent()
# p2 = Agent()
# play_game(p1, p2, env)