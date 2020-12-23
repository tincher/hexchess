from .piece import Piece


class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'b'

    def possible_moves(self):
        pass
