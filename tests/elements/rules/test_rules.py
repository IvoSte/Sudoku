from dataclasses import replace
from src.elements.rules import block_rule, horizontal_rule, vertical_rule
from src.elements.puzzle import coordinates_to_block
from src.elements.field import Field
from src.elements.grid import Grid
import pytest

# empty grid imported from conftest

def test_horizontal_rule_empty_grid(empty_grid: Grid):
    assert horizontal_rule(empty_grid, Field(x=1, y=1, block=1, value=1)) == True


def test_vertical_rule_empty_grid(empty_grid: Grid):
    assert vertical_rule(empty_grid, Field(x=1, y=1, block=1, value=1)) == True


def test_block_rule_empty_grid(empty_grid: Grid):
    assert block_rule(empty_grid, Field(x=1, y=1, block=1, value=1)) == True


@pytest.fixture
def grid_one_field(empty_grid: Grid) -> Grid:
    new_fields = [Field(x=1, y=1, block=1, value=1)] + empty_grid.fields[:1]
    return replace(empty_grid, fields=new_fields)


def test_horizontal_rule_one_field(grid_one_field: Grid):
    horizontal_rule(grid_one_field, Field(x=1, y=1, block=1, value=1)) == True


@pytest.fixture
def grid_two_fields(empty_grid: Grid) -> Grid:
    new_fields = [Field(x=1, y=1, block=1, value=1), Field(x=2, y=1, block=1, value=1)] + empty_grid.fields[:2]
    return replace(empty_grid, fields=new_fields)


def test_horizontal_rule_two_fields(grid_two_fields: Grid):
    horizontal_rule(grid_two_fields, Field(x=2, y=1, block=1, value=1)) == False
    horizontal_rule(grid_two_fields, Field(x=2, y=1, block=1, value=2)) == True