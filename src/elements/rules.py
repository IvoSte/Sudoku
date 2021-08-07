
def check_legal(puzzle, field):
    return horizontal_rule(puzzle, field) and vertical_rule(puzzle, field) and block_rule(puzzle, field)

def horizontal_rule(puzzle, field):
    for other_field in puzzle.grid.get_horizontal(field.y):
        if other_field.x == field.x:
            continue                        # Don't compare to myself.
        if other_field.value == field.value:
            return False                    # No same values in the same row.
    return True

def vertical_rule(puzzle, field):
    for other_field in puzzle.grid.get_vertical(field.x):
        if other_field.y == field.y:
            continue                        # Don't compare to myself.
        if other_field.value == field.value:
            return False                    # No same values in the same row.
    return True

def block_rule(puzzle, field):
    for other_field in puzzle.grid.get_block(field.block):
        if other_field.x == field.x and other_field.y == field.y:
            continue
        if other_field.value == field.value:
            return False
    return True
