class Game:
    def __init__(self, side_length):
        # 0 -> empty, 1 -> pawn, 2 -> knight, 3 -> bishop, 4 -> rook, 5 -> queen, 6 -> king
        self.lines = self.get_empty_board(side_length)

    def legal_moves(self):
        pass

    def get_empty_row(self, length):
        return [[]]

    def get_empty_board(self, side_length):
        board = [[]] * (side_length * 2 - 1)

        return board


game = Game(6)
