from ..elements import *
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.pawn = Pawn(1, 1, 0)
        self.game = Game()
        self.game.add_figure(self.pawn)

    def test_pawn_straight(self):
        possible_moves = self.game.possible_moves()
        predicted_moves = [Move(self.pawn.position, Position(self.pawn.position.x, self.pawn.position.y + 1)),
                           Move(self.pawn.position, Position(self.pawn.position.x, self.pawn.position.y + 2))]
        self.assertCountEqual(possible_moves, predicted_moves)

    def test_pawn_straight_has_moved(self):
        pass

    def test_pawn_straight_blocking(self):
        pass

    def test_pawn_capture(self):
        pass


if "__main__" == __name__:
    unittest.main()

    # todo testing for at least all movement possibilities
