from ..elements.grid import Grid
from ..elements.rules import check_legal

def solve_sudoku(grid: Grid) -> Grid:
    while not check_solved(grid):
        # idea : Loop over all fields,
        #           Check for each value if it is legal -- add to virtual values
        #           If there is only one value possible, place it
        #           Loop until there is no change in an iteration
        #               Is this enough? Possibly tricks or heuristics are required. (e.g. solve for pairs)
        pass

def check_solved(grid: Grid) -> bool:
    for field in grid.fields:
        if field.value == None:
            return False
        if not check_legal(grid, field):
            return False
    return True