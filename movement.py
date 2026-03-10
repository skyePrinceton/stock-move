class Move:
    """A stock movement entry linking two locations."""

    def __init__(self, from_location, to_location, qty, ref=""):
        self._id = 0
        self._from_location = from_location
        self._to_location = to_location
        self._qty = qty
        self._ref = ref

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def from_location(self):
        return self._from_location

    @property
    def to_location(self):
        return self._to_location

    @property
    def qty(self):
        return self._qty

    @property
    def ref(self):
        return self._ref

    def __repr__(self):
        return (f"Move(id={self._id}, from={self._from_location.name!r}, "
                f"to={self._to_location.name!r}, qty={self._qty})")


class MoveLog:
    """Append-only log of stock movements."""

    def __init__(self):
        self._moves = []
        self._counter = 0

    def record(self, move):
        self._counter += 1
        move.id = self._counter
        self._moves.append(move)
        move.from_location._add_move(move)
        move.to_location._add_move(move)
        return move

    def moves(self):
        return list(self._moves)
