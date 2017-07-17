import numpy as np
class Test(object):

    def __init__(self):
        self.x = 'x'
        self.o = 'o'
        self.board = np.zeros((LENGTH, LENGTH))

    def draw_board(self):
        '''Print a drawn out version to the screen'''
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print(" ", end="")
                if self.board[i,j] == self.x:
                    print("x |", end=""),
                elif self.board[i,j] == self.o:
                    print('o |', end=""),
                else:
                    print(": |", end=""),
            print("")
        print("-------------")

LENGTH = 3
a = Test()
a.draw_board()