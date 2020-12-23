import string


class Position:
    # x == 0 -> a ; y == 0 -> 1
    # from numbers to position: https://upload.wikimedia.org/wikipedia/de/9/94/HexagonalschachFelder.svg
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return string.ascii_lowercase[self.x] + str(self.y + 1)

    def __repr__(self):
        return str(self)
