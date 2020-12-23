from elements import *

rook = Rook(1, 1, 0)
knight = Knight(3, 2, 0)
queen = Queen(1, 1, 0)
king = King(1, 1, 0)
bishop = Bishop(1, 1, 0)
pawn = Pawn(1, 1, 0)

pieces = [rook, knight, queen, king, bishop, pawn]

for elem in pieces:
    print(elem)
