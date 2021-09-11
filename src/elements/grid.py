from dataclasses import dataclass, replace
from .field import Field


@dataclass(frozen=True)
class Grid:

    
    root_size: int                    # NOTE: Size is both the amout of fields per block width/height, 
                                            # And the amout of blocks per width/height. In traditional sudoku's, this is 3.
    fields: list[Field]

    def get_field_at_x_y(self, x, y):
        return [field for field in self.fields if field.x == x and field.y == y][0] #NOTE how can I do this better?

    def get_vertical(self, x):
        return [field for field in self.fields if field.x == x ]

    def get_horizontal(self, y):
        return [field for field in self.fields if field.y == y]

    def get_block(self, block):
        return [field for field in self.fields if field.block == block]

    def get_rows(self):
        return [
            self.get_horizontal(n) for n in range(self.root_size * self.root_size + 1)
        ]

    def place_field(self, x: int, y: int, new_value: int) -> "Grid":
        return Grid(
            root_size=self.root_size,
            fields=[
                replace(field, value = new_value)
                if (field.x == x and field.y == y) else field
                for field in self.fields
            ],
        )