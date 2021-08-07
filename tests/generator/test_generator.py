from src.generator.generator import idx_to_x_y

def test_idx_to_x_y():
    assert idx_to_x_y(3, 4) == (5, 1)
    assert idx_to_x_y(3, 9) == (1, 2)
    assert idx_to_x_y(3, 8) == (9, 1)
