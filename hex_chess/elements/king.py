from .piece import Piece


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'k'

    def possible_moves(self):
        pass
