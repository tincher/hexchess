from .piece import Piece


class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'n'

    def possible_moves(self):
        pass
