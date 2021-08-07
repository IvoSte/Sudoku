
from src.elements.field import Field
from src.elements.grid import Grid


def check_legal(grid: Grid, field: Field) -> bool:
    h = horizontal_rule(grid, field)
    v = vertical_rule(grid, field)
    b = block_rule(grid, field)
    #print(f"{h=} {v=} {b=}")
    return  h and v and b

def horizontal_rule(grid: Grid, field: Field) -> bool:
    for other_field in grid.get_horizontal(field.y):
        if other_field.x == field.x:
            continue                        # Don't compare to myself.
        if other_field.value == field.value:
            return False                    # No same values in the same row.
    return True

def vertical_rule(grid: Grid, field: Field) -> bool:
    for other_field in grid.get_vertical(field.x):
        if other_field.y == field.y:
            continue                        # Don't compare to myself.
        if other_field.value == field.value:
            return False                    # No same values in the same row.
    return True

def block_rule(grid: Grid, field: Field) -> bool:
    for other_field in grid.get_block(field.block):
        if other_field.x == field.x and other_field.y == field.y:
            continue
        if other_field.value == field.value:
            return False
    return True
