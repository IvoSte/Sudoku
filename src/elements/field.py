
class Field:

    def __init__(self, x, y, block, value):
        self.x = x
        self.y = y
        self.block = block
        self.value = value
        # self.show = False

    def _print(self):
        print(f"{self.x} {self.y} {self.value}")
