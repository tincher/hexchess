from .piece import Piece


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'r'

    def possible_moves(self):
        pass
