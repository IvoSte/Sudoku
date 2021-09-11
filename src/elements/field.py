from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Field:
    x: int
    y: int
    block: int
    value: Optional[int]
    # self.show = False

    def __str__(self) -> str:
        return str(self.value)
    
    def print_(self):
        print(f"{self.x} {self.y} {self.value}")

