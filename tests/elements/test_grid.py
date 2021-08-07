

from src.elements.grid import Grid


def test_place_field(empty_grid: Grid):
    grid = empty_grid.place_field(x = 1, y = 1, new_value = 1)
    assert grid.fields[0].value == 1