


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
            try:
                return int(value[1:])
            except ValueError:
                ref_cell = value[1:]
                if ref_cell in self._cells:

                    if cell == self.get(value[:1] + value[2:]):
                        return "#Circular"

                    return self.evaluate(ref_cell)
                else:
                    return "#Error"
        try:
            return int(value)
        except ValueError:
            try:
                float(value)
                return "#Error"
            except ValueError:
                return value

