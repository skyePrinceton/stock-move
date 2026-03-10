from location import Location
from movement import Move, MoveLog


class Store:
    """Inventory store for tracking stock movements between locations.

    Every stock movement transfers quantity from one location to another.
    Stock locations (kind='stock') cannot hold negative quantities.
    """

    def __init__(self):
        self._locations = {}
        self._log = MoveLog()

    def create_location(self, name, kind="stock"):
        if name in self._locations:
            raise ValueError(f"location {name!r} already exists")
        loc = Location(name, kind)
        self._locations[name] = loc
        return loc

    def get_location(self, name):
        return self._locations[name]

    def locations(self):
        return list(self._locations.values())

    def move(self, from_name, to_name, qty, ref=""):
        if qty <= 0:
            raise ValueError("qty must be positive")
        from_loc = self._locations[from_name]
        to_loc = self._locations[to_name]
        entry = Move(from_loc, to_loc, qty, ref)
        self._log.record(entry)
        return entry

    def move_log(self):
        return self._log.moves()

    def stock_check(self):
        total_in = 0
        total_out = 0
        for m in self._log.moves():
            total_in += m.qty
            total_out += m.qty
        return total_in, total_out
