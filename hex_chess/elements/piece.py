from .hexagon import Hexagon
from .position import Position


class Piece(Hexagon):
    def __init__(self, x, y, color):
        self.position = Position(x, y)
        self.color = color
        self.char = None

    def is_occupied(self):
        return True

    def is_white(self):
        return self.color == 0

    def possible_moves(self):
        pass

    def __str__(self):
        char = self.char.capitalize() if self.is_white() else self.char
        return char + str(self.position)
