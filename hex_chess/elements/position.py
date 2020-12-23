import string


class Position:
    # x == 0 -> a ; y == 0 -> 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.side_length = 6

    def change_side_length(self, side_length):
        self.side_length = side_length

    def __str__(self):
        return string.ascii_lowercase[self.x] + str(self.y + 1)
