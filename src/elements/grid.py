from .field import Field

class Grid:

    def __init__(self, size):
        self.size = size                    # NOTE: Size is both the amout of fields per block width/height, 
                                            # And the amout of blocks per width/height. In traditional sudoku's, this is 3.
        self.fields = self.generate(size)

    def generate(self, size):
        fields = [Field(x, y, self.coordinates_to_block(x,y,size), None) \
            for x in (range(1,(size*size)+1)) \
            for y in (range(1,(size*size)+1))]
        return fields

    def coordinates_to_block(self, x, y, size):
        # Calculate blocks -- [size] amount per row and column. Start at 1. E.G. first row is 1, 2, 3. 
        block_x = x/size
        block_y = y/size
        block = ((block_y - 1) * size) + block_x
        return block

    def get_vertical(self, x):
        return [field for field in self.fields if field.x == x ]

    def get_horizontal(self, y):
        return [field for field in self.fields  if field.y == y]

    def get_block(self, block):
        return [field for field in self.fields in field.block == block]

    def _print(self):
        for n in range(self.size * self.size + 1):
            print("\n")
            row = self.get_horizontal(n)
            for field in row:
                field._print()