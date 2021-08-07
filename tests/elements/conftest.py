from src.elements.field import Field
from src.elements.grid import Grid
import pytest
from src.elements.puzzle import coordinates_to_block


@pytest.fixture
def empty_grid() -> Grid:
    root_size = 3
    return Grid(
        root_size,
        fields=[
            Field(x, y, coordinates_to_block(x,y,root_size), None)
            for x in (range(1,(root_size*root_size)+1))
            for y in (range(1,(root_size*root_size)+1))
        ]
    )
