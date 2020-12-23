from .piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.char = 'p'
        self.has_moved = False

    def move(self, new_x, new_y):
        self.has_moved = True
        super().move(new_x, new_y)
