import time
from dataclasses import replace
from src.view.view import view_grid
from src.elements.field import Field
from ..elements.grid import Grid
import numpy as np
from ..elements.rules import check_legal


def idx_to_x_y(root_size: int, idx: int) -> tuple[int, int]:
    x = (idx) % (root_size * root_size) + 1
    y = (idx) // (root_size * root_size) + 1
    return x, y

def generate_sudoku(grid: Grid) -> Grid:
    return generate_row_by_row(grid)

def generate_row_by_row(grid: Grid) -> Grid:
    numbers_range = range(1,grid.root_size*grid.root_size + 1)
    bag_of_numbers = []
    for idx, field in enumerate(grid.fields):
        if len(bag_of_numbers) == 0:
            bag_of_numbers = list(numbers_range)

        x, y = idx_to_x_y(grid.root_size, idx)
        grid = grid.place_field(x, y, np.random.choice(bag_of_numbers))
        while not check_legal(grid, grid.fields[idx]):
            grid = grid.place_field(x, y, np.random.choice(bag_of_numbers))

        view_grid(grid)
        bag_of_numbers.remove(grid.fields[idx].value)

    return grid


def generate_block_by_block(grid: Grid) -> Grid:
    blocks_remaining = grid.root_size * grid.root_size
    while blocks_remaining > 0: 
        np.array(range(1,grid.root_size*grid.root_size))
    return grid