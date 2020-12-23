from .piece import Piece


class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'q'

    def possible_moves(self):
        pass
