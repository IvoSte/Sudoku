from .grid import Grid


class Puzzle:
    """Puzzle object ..."""
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.grid = Grid(size)

    def generate(self):
        self.generate_block_by_block()
        return self

    def generate_block_by_block(self):
        pass

    def _print(self):
        self.grid._print()

# generation strategies
    # fill in with random values, remove illegal, -- simulated annealing. Possible, horribly inefficient. 
    # Block by block. Random generation for one block, fit second, nescessary thrird. Kind of using solver.
    # Take known, and transform / mirror.
    # 