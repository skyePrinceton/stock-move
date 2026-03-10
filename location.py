class Location:
    """A storage location that tracks its quantity from move entries.

    The quantity is always computed from moves -- never stored directly.
    This guarantees the quantity is always consistent with the move log.
    """

    def __init__(self, name, kind="stock"):
        self._name = name
        self._kind = kind
        self._moves = []

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def quantity(self):
        total = 0
        for move in self._moves:
            if move.to_location is self:
                total += move.qty
            elif move.from_location is self:
                total -= move.qty
        return total

    def _add_move(self, move):
        self._moves.append(move)

    def moves(self):
        return list(self._moves)

    def __repr__(self):
        return f"Location(name={self._name!r}, kind={self._kind!r})"
