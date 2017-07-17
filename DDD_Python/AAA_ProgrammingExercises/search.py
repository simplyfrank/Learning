grid = [[0,0,0,0,0,1],
        [1,1,0,0,0,1],
        [0,0,0,1,0,0],
        [0,1,1,0,0,1],
        [0,1,0,0,1,0],
        [0,1,0,0,0,2]
]

walls = ((0,5), (1,0), (1,1), (1,5), (2,3), (3,1), (3,2), (3,5), (4,1), (4,4), (5,1))

def search(x,y):
    '''Accepts coordinates of a cell to explore, it performs a goal check.
    If it hits a wall or an already visited cell it returns False'''
    # Goal test
    if grid[x][y] == 2:
        print('We found the Exit')
        return True
    # Check if available
    elif grid[x][y] == 1:
        print('wall at %d, %d' % (x,y))
        return False
    # Check if visited already
    elif grid[x][y] == 3:
        print('Visited at %d %d' % (x,y))
        return False

    print('visiting %d %d' % (x,y))
    
    # marking as visited
    grid[x][y] = 3

    # Explore adjacent fields
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search (x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True
    return False

# search(0,0)
import heapq

class Cell(object):
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

class AStar(object):
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid_height = 6
        self.grid_width = 6
        self.stepcost = 10

    def init_grid(self):
        walls = ((0,5), (1,0), (1,1), (1,5), (2,3), (3,1), (3,2), (3,5), (4,1), (4,4), (5,1))

        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x,y) in walls:
                    reachable = False
                else:
                    reachable = True
                self.cells.append(Cell(x,y,reachable))
        
        self.start = self.get_cell(0,0)
        self.end = self.get_cell(5,5)

    
    def get_heuristic(self, cell):
        '''
       Compute the heuristic value H for a cell:
       Distance from the Goal multiplied by the stepcost 
        '''
        return self.stepcost * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_cell(self, x,y):
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        cells = []
        # get the right cell
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        # Append the lower cell
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        # Append the left cell
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        # Append the top cell
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))
            return cells

    def display_path(self):
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            print('path: cell: %d,%d' %(cell.x, cell.y))

    def update_cell(self, adj, cell):
        """
        Update the adjacent cell
        """
        adj.g = cell.g + self.stepcost
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g
    
    def process(self):
        """
        Main Method implementing the AStartSearch Algorithm
        """
        # add starting cell to open queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list 
            self.closed.add(cell)
            # if ending cell, display path
            if cell is self.end:
                self.display_path()
                break
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # If it is in the frontier, check if value is better than current best pathh
                        if ajd_cell.g > cell.g + self.stepcost:
                            self.update_cell(adj_cell, cell)
                        else:
                            self.update_cell(ajd_cell, cell)
                            # add adj cell to open list
                            heapq.heappush(self.opened, (adj_cell.f, adj_cell))


a = AStar()
a.init_grid()
a.process()
