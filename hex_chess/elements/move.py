class Move:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return str(self.origin) + str(self.destination)

    def __repr__(self):
        return repr(self.origin) + repr(self.destination)

    def __hash__(self):
        return hash((self.origin, self.destination))

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.origin == other.origin and self.destination == other.destination
        return False
