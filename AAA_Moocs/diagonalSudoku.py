

cols = '123456789'
rows = 'ABCDEFGHI'
digits = '123456789'
board = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'


def cross(a,b):
    return [s+t for s in a for t in b]

def grid_values(board):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in board:
        if c in digits:
            chars.append(c)
        else:
            chars.append(digits)
        
    assert len(chars) == 81
    return dict(zip(boxes, chars))


# Representing the Sudoku Board
boxes = cross(rows, cols)
values = grid_values(board)
row_units = [cross(row, cols) for row in rows]
col_units = [cross(rows, col) for col in cols]
square_units = [cross(rs, cs) for cs in ('123', '456', '789') for rs in ('ABC','BCD', 'DEF', 'GHI' )]
diagonal_units = [[r+c for r,c in zip(row_units, col_units)], [r+c for r,c in zip(row_units, col_units[::-1])]]
unit_list = row_units + col_units + square_units + diagonal_units
units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((box, [unit for unit in unit_list if box in unit]) for box in boxes )

# Helper Functions 
def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# Implemented Strategies for puzzle solving
def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values

def only_choice(values):
    """
    Check all units and check how often the value appears in all peer boxes.
    If it appears only once, eliminate the value from all other possible positions.
    """
    for unit in unit_list:
        for digit in digits:
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values




def naked_twins(values):
    """
    Identify identical pairs of possible numbers and remove their values from all their peer blocks.
    """
    for unit in unit_list:
        twin_candidates = [(box, values[box]) for box in unit if len(values[box]) == 2]
        if len(twin_candidates) > 2:
            twins_sorted = sorted(twin_candidates, key=itemgetter(1))
            pairs_sorted = groupby((twins_sorted), key=itemgetter(1))
            for digits, twin_candidates in pairs_sorted:
                boxes = [twin_candidates[0] for candidate in twin_candidates]
                if len(boxes) == 2:
                    for box in unit:
                        if box not in boxes:
                            for digit in digits:
                                if digit in values[box] and len(values[box]) > 1:
                                    assign_value(box, values[box].replace(digit, ''))

def reduce_puzzle(values):
    solved_puzzle = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box])==0]):
            return False
    return values



def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = reduce_puzzle(values)
    if values is False:
        return False #Failed earlier
    if all(len(values[s])== 1 for s in boxes):
        return values
    values = search(values)



def search(values):

    # reduce puzzle and check for solution
    if reduce_puzzle(values):
        return True

    # else we continue to branch
    # Create a dict, sorted by length of values to find the min branching factor
    branches = sorted({k:v for (k,v) in values.items() if len(v) > 1}, key=lambda box: len(branches[box]))
    
    # Perform the search
    for box in branches:
        for digit in values[box]:
            # Create a copy to save current stage
            new_puzzle = values.copy()
            # Initialize branch
            new_puzzle[box] = digit
            if search(new_puzzle):
                values = new_puzzle
                return True
    
    # Otherwise exit, as no solution can be found
    return False


diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
display(solve(diag_sudoku_grid))
