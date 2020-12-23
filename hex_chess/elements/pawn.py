from .piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'p'

    def possible_moves(self):
        pass
