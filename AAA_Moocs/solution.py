
class Sudoku(object):

w



class SudokuSolver(object):

    # Constructor
    def __init__(self, is_diag_sudoku=False, from_string=None, from_dict=None):
        '''
        Build and init the board using either a string or a dict

        Parameters
        ----------
        is_diag_sudoku : bool, set to True for Diagonal Sudoku, set to False for regular Sudoku
        from_string : str[81], string with initial values from top left corner to bottom right corner.
            e.g., '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        from_dict : dict, dictionary with box coordinate as key (e.g. 'A1') and a digit or '.' as value.
        '''


        self.boxes = self.cross(Sudoku.ROWS, Sudoku.COLS)

        self.values = self.grid_values(from_string, from_dict)

        self.row_units = [self.cross(row, Sudoku.COLS) for row in Sudoku.ROWS]

        self.col_units = [self.cross(Sudoku.ROWS, col) for col in Sudoku.COLS]

        self.square_units = [self.cross(square_row, square_col) for square_row in Sudoku. SQUARE_ROWS for square_col in Sudoku. SQUARE_COLS]

        self.all_units = self.row_units + self.col_units + self.square_units

        if is_diag_sudoku==True:
            self.diag_units = [[y+x for y,x in zip(Sudoku.ROWS, Sudoku.COLS)], [y+x for y,x in zip(Sudoku.ROWS, Sudoku.COLS[::-1])]]
            self.all_units += self.diag_units

        self.units = dict((box, [unit for unit in self.all_units if box in unit]) for box in self.boxes)

        self.peers = dict((box, set(sum(self.units[box], [])) - set([box])) for box in self.boxes)
    

    def cross(A, B):
        "Cross product of elements in A and elements in B."
        return [s+t for s in A for t in B]

    def reduce_puzzle(self, use_strategy1=True, use_strategy2=True, use_strategy3=True):
            '''
            Reduce Sudoku puzzle until the grid doesn't change using three strategies:
            1 - Iterate over all the boxes and for each box with a single value, remove its value from all its peers.
            2 - If there is only one box in a unit which would allow a certain digit, then that box must be assigned that digit.
            3 - Identify naked twins (two boxes in the same unit having the same two digits) and remove their individual digits from unit peers.

            Parameters
            ----------
            use_strategy1 : if True, apply eliminate()
            use_strategy2 : if True, apply only_choice()
            use_strategy3 : if True, apply naked_twins()

            Returns
            -------
            solved: bool, True if solved, False otherwise
            '''

            while True:
                old_grid = self.values.copy()

                if use_strategy1 is True:
                    self.eliminate()

                if use_strategy2 is True:
                    self.only_choice()

                if use_strategy3 is True:
                    self.naked_twins()

                if old_grid == self.values:
                    break

            return self.is_solved()

    def eliminate(self):
        '''
        Iterate over all the boxes and for each box with a single value, remove its value from all its peers
        '''

        for box in self.boxes:
            if len(self.values[box]) == 1: # if self.values[box] in Sudoku.DIGITS:
                for peer in self.peers[box]:
                    if self.values[box] in self.values[peer] and len(self.values[peer]) > 1:
                        self.assign_value(peer,self.values[peer].replace(self.values[box], ''))

    def only_choice(self):
        '''
        If there is only one box in a unit which would allow a certain digit, then that box must be assigned that digit.
        '''

        for unit in self.all_units:
            for box_idx in range(len(unit)):
                if len(self.values[unit[box_idx]]) > 1:  # more than one digit possible at this loc
                    for digit in self.values[unit[box_idx]]:
                        isUniqueToThisBox = True
                        for other_box_idx in range(len(unit)):
                            if other_box_idx != box_idx and digit in self.values[unit[other_box_idx]]: # don't compare it to itself...
                                isUniqueToThisBox = False
                                break
                        if isUniqueToThisBox == True:
                            self.assign_value(unit[box_idx], digit)
    
    def naked_twins(self):
        '''
        Identify naked twins and remove their individual digits from unit peers.
        '''

        for unit in self.all_units:
            candidates = [(box, self.values[box]) for box in unit if len(self.values[box]) == 2]
            if len(candidates) >= 2:
                sorted_candidates = sorted(candidates, key=itemgetter(1))
                paired_candidates = groupby(sorted_candidates, key=itemgetter(1))
                for digits, candidates in paired_candidates:
                    boxes = [candidate[0] for candidate in candidates]
                    if len(boxes) == 2:
                        for box in unit:
                            if box not in boxes:
                                for digit in digits:
                                    if digit in self.values[box] and len(self.values[box]) > 1:
                                        self.assign_value(box, self.values[box].replace(digit, ''))



    def search(self):
        '''
        Search for a solution using depth-first search
        Search branches are built by splitting boxes with the smallest number of possible values

        Returns
        -------
        result: bool, set to False if a solution hasn't been found, True otherwise
        '''

        # First, apply elimination and check if we have a solution
        if self.reduce_puzzle() == True:
            # We can't branch down any further, but our solution may not be valid, so check!
            return self.is_valid()

        # We need to branch further down, but there's no point in doing so if we went down an invalid branch
        if self.is_valid() == False:
            return False

        # Build the list of boxes to split, ordered by increasing number of options
        splittable_boxes = {k:v for (k,v) in self.values.items() if len(v)>1}
        splittable_boxes = sorted(splittable_boxes, key=lambda box: len(splittable_boxes[box]))

        # There is absolutely NO REASONABLE EXPLANATION for the following hack to make a difference, but if you go
        # through the shortest boxes in LEXICAL ORDER, then this code solves the example provided much, much faster.
        # Could this just be an artifact of the way the puzzle itself was created?
        idx_start = idx_end = 0
        ordered_splittable_boxes = []
        while idx_end < len(splittable_boxes) - 1:
            while len(self.values[splittable_boxes[idx_start]]) == len(self.values[splittable_boxes[idx_end]]) and idx_end < len(splittable_boxes) - 1:
                idx_end += 1
            ordered_splittable_boxes.extend(sorted(splittable_boxes[idx_start:idx_end]))
            idx_start = idx_end

        # Perform the search
        for box in ordered_splittable_boxes:
            for digit in self.values[box]:
                new_grid = self.values.copy()
                new_grid[box] = digit
                new_sudoku = Sudoku(from_dict=new_grid)
                if new_sudoku.search() == True:
                    self.values = new_sudoku.values
                    return True

        # This sudoku has no solution
        return False


grid ="2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3"

a = SudokuSolver(is_diag_sudoku=True, from_string=grid)
print(a.reduce_puzzle())
