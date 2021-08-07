from src.generator.generator import generate_sudoku
from src.elements.field import Field
from .grid import Grid

def coordinates_to_block(x: int, y: int, root_size: int):
    # Calculate blocks -- [root_size] amount per row and column. Start at 1. E.G. first row is 1, 2, 3. 
    block_x = x/root_size
    block_y = y/root_size
    block = ((block_y - 1) * root_size) + block_x
    return block


class Puzzle:
    """Puzzle object ..."""
    def __init__(self, name, root_size):
        self.name = name
        self.root_size = root_size
        self.grid = self.generate_grid(root_size)

    def generate(self):
        self.grid = generate_sudoku(self.grid)

    def generate_grid(self, root_size):
        return Grid(
            root_size=root_size,
            fields=[
                Field(x, y, coordinates_to_block(x,y,root_size), None)
                for y in (range(1,(root_size*root_size)+1))
                for x in (range(1,(root_size*root_size)+1))
            ]
        )
        

    def print_(self):
        self.grid.print_()

# generation strategies
    # fill in with random values, remove illegal, -- simulated annealing. Possible, horribly inefficient. 
    # Block by block. Random generation for one block, fit second, nescessary thrird. Kind of using solver.
    # Take known, and transform / mirror.
    # 