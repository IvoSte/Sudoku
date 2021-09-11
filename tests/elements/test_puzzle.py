from src.elements.puzzle import coordinates_to_block

def test_coordinates_to_block():
    assert coordinates_to_block(x = 1, y = 1, root_size= 3) == 1
    assert coordinates_to_block(x = 4, y = 1, root_size= 3) == 2
    assert coordinates_to_block(x = 1, y = 4, root_size= 3) == 4
    assert coordinates_to_block(x = 9, y = 9, root_size= 3) == 9
