assignments = []

# Enumerate Board
rows = 'ABCDEFGHI'
cols = '123456789'
digits = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

boxes = cross(rows, cols)

# Indiivdual units
row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
# Create two lists for the diagonal cross in the gameboard
diagonal_units = [[r+c for r,c in zip(rows, cols)], [r+c for r,c in zip(rows, cols[::-1])]]

# Add the diagonal units
unitlist = row_units + col_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value): 
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Create a list of matching length valued boxes
    potential_twins = [box for box in values if len(values[box]) == 2]
    # Subset the potentials to those, who have a matching set of values
    naked_twins = [[b1,b2] for b1 in potential_twins for b2 in peers[b1] if set(values[b1])==set(values[b2])]
    
    # Iterate over all naked_twins useing an index to access the individual pairs
    for i,_ in enumerate(naked_twins):
        # split assign the paired boxes for comparison
        b1,b2 = naked_twins[i]
        # Generate a de-duplicated set of peer boxes to be checked for duplicated values
        peer_set = set(peers[b1]) & set(peers[b2]) # Solved using 'https://stackoverflow.com/questions/3697432/how-to-find-list-intersection'
        # Iterate over all peers to eliminate naked_twin values
        for peer in peer_set:
            # Only eliminate from boxes with more than 2 values (to exclude hitting the naked_twins themselfes)
            if len(values[peer])>=2:
                # Eliminate both values contained in twin_a
                for v in values[b1]:
                    assign_value(values, peer, values[peer].replace(v, ''))
                
    return values

def grid_values(grid): #<-- Course Solution
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
    for c in grid:
        if c in digits:
            chars.append(c)
        else:
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values): #<-- Course Solution
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
    print

def eliminate(values): #<-- Course Solution
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values): #<-- Course Solution
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values, dplaces[0], digit)

    return values

def reduce_puzzle(values): #<-- Course Solution
    """
    Iterate eliminate() and only_choice() and naked_twins(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        # Add the strategy for naked_twins
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # check if this iteration did bring improvement, if not quit
        stalled = solved_values_before == solved_values_after
        # Make sure we have not accidentially erased a value from the board, if so quit.
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values): #<-- Course Solution
    """
    Implements a search strategy using depth first search to solve ties in the game if necessary.
    """
    # Try solving the puzzle using the reduction strategy alone
    values = reduce_puzzle(values)
    # if this failed it returns False, break now
    if values is False:
        return False ## Failed earlier
    # If all values are singulare we are done, break now
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # We have not found a solution, branch out using the min(len) valued block to save on iterations
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # for each possible solution branch now
    for value in values[s]:
        # Create a copy to save state
        new_sudoku = values.copy()
        # Assign the next possible state to the top node in the tree
        new_sudoku[s] = value
        # Start a recurrent search with the given board state
        attempt = search(new_sudoku)
        # If the attempt succeeds it returns true, return!
        if attempt:
            return attempt


def solve(grid): #<-- Course Solution slightly changed
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = search(values)

    return values


if __name__ == '__main__':
    hard = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(hard))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')



grid = {"G7": "2345678", "G6": "1236789", "G5": "23456789", "G4": "345678",
"G3": "1234569", "G2": "12345678", "G1": "23456789", "G9": "24578",
"G8": "345678", "C9": "124578", "C8": "3456789", "C3": "1234569",
"C2": "1234568", "C1": "2345689", "C7": "2345678", "C6": "236789",
"C5": "23456789", "C4": "345678", "E5": "678", "E4": "2", "F1": "1",
"F2": "24", "F3": "24", "F4": "9", "F5": "37", "F6": "37", "F7": "58",
"F8": "58", "F9": "6", "B4": "345678", "B5": "23456789", "B6":
"236789", "B7": "2345678", "B1": "2345689", "B2": "1234568", "B3":
"1234569", "B8": "3456789", "B9": "124578", "I9": "9", "I8": "345678",
"I1": "2345678", "I3": "23456", "I2": "2345678", "I5": "2345678",
"I4": "345678", "I7": "1", "I6": "23678", "A1": "2345689", "A3": "7",
"A2": "234568", "E9": "3", "A4": "34568", "A7": "234568", "A6":
"23689", "A9": "2458", "A8": "345689", "E7": "9", "E6": "4", "E1":
"567", "E3": "56", "E2": "567", "E8": "1", "A5": "1", "H8": "345678",
"H9": "24578", "H2": "12345678", "H3": "1234569", "H1": "23456789",
"H6": "1236789", "H7": "2345678", "H4": "345678", "H5": "23456789",
"D8": "2", "D9": "47", "D6": "5", "D7": "47", "D4": "1", "D5": "36",
"D2": "9", "D3": "8", "D1": "36"}

display(naked_twins(grid))
display(search(grid))