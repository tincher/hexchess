from .position import Position
from .pawn import Pawn
from .move import Move


class Game:
    def __init__(self):
        self.figures = []

    def add_figure(self, figure):
        self.figures.append(figure)

    def is_figure_at_position(self, x, y):
        return len([fig for fig in self.figures if fig.position.x == x and fig.position.y == y]) > 0

    def pawn_moves(self, pawn):
        result = []
        if not self.is_figure_at_position(pawn.position.x, pawn.position.y + 1):
            result.append(Move(pawn.position, Position(pawn.position.x, pawn.position.y + 1)))
        if not pawn.has_moved and not self.is_figure_at_position(pawn.position.x, pawn.position.y + 2):
            result.append(Move(pawn.position, Position(pawn.position.x, pawn.position.y + 2)))
        figures = self.figures
        # left side
        if pawn.position.x < 5:
            if self.pawn_can_capture_outside(pawn, figures):
                result.append(Move(pawn.position, Position(pawn.position.x - 1, pawn.position.y)))
            if self.pawn_can_capture_inside(pawn, figures):
                result.append(Move(pawn.position, Position(pawn.position.x + 1, pawn.position.y + 1)))
        # right side
        elif pawn.position.x > 5:
            mirrored_figures = self.mirrored_figures(figures)
            if self.pawn_can_capture_outside(pawn, mirrored_figures):
                # since we mirrored this is actually capturing to the right
                result.append(Move(pawn.position, Position(pawn.position.x + 1, pawn.position.y)))
            if self.pawn_can_capture_inside(pawn, mirrored_figures):
                # since we mirrored this is actually capturing to the left
                result.append(Move(pawn.position, Position(pawn.position.x - 1, pawn.position.y + 1)))
        # center lane
        else:
            mirrored_figures = self.mirrored_figures(figures)
            if self.pawn_can_capture_outside(pawn, figures):
                result.append(Move(pawn.position, Position(pawn.position.x - 1, pawn.position.y)))
            if self.pawn_can_capture_outside(pawn, mirrored_figures):
                result.append(Move(pawn.position, Position(pawn.position.x + 1, pawn.position.y)))

        return result

    def possible_moves(self):
        moves = []
        for pawn in filter(lambda x: isinstance(x, Pawn), self.figures):
            moves.extend(self.pawn_moves(pawn))
        return moves

    def __str__(self):
        result = 'GAME'
        for figure in self.figures:
            result += ' ' + str(figure)
        return result

    @staticmethod
    def mirrored_figures(figures):
        result = figures
        for figure in result:
            figure.position.x = 10 - figure.position.x
        return result

    @staticmethod
    def pawn_can_capture_outside(pawn, figures):
        return len([figure for figure in figures if
                    figure.position.x == pawn.position.x - 1 and figure.position.y == pawn.position.y]) > 0

    @staticmethod
    def pawn_can_capture_inside(pawn, figures):
        return len([figure for figure in figures if
                    figure.position.x == pawn.position.x + 1 and figure.position.y == pawn.position.y + 1]) > 0
