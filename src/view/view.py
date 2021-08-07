from src.elements.field import Field
from src.elements.grid import Grid

def print_row(row: list[Field], delim=" "):
    print(delim.join(map(str, row)))


def view_grid(grid: Grid):
    for row in grid.get_rows():
        print_row(row)
