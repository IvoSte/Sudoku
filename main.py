from src.elements.puzzle import Puzzle
from src.view.view import view_grid

def main():
    sudoku = Puzzle("hello", 3)
    sudoku.generate()
    view_grid(sudoku.grid)

if __name__ == "__main__":
    main()
