
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
        value = self.get(cell)
        if value.startswith("='") and value.endswith("'"):
            return value[2:-1]
        elif value.startswith("'"):
            return "#Error"
        elif value.startswith("="):
            return value[1:]
        try:
            return int(value)
        except ValueError:
            try:
                float(value)
                return "#Error"
            except ValueError:
                return value

