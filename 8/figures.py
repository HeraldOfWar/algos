colors = {0: 'w', 1: 'b'}


class ChessPiece:
    def __init__(self, row: int, col: int, color: int = 0):
        self.__pos = row, col
        self.__color = color

    @property
    def pos(self) -> tuple:
        return self.__pos

    @pos.setter
    def pos(self, row: int, col: int):
        self.__pos = row, col

    @property
    def color(self) -> int:
        return self.__color

    @color.setter
    def color(self, color: int):
        self.__color = color

    def can_move(self, x1: int, y1: int) -> bool:
        return True

    def move(self, row: int, col: int):
        print(f'Фигура {self.__repr__()} была успешно перемещена из'
              f' позиции {self.pos[0] + 1, self.pos[1] + 1} в позицию {row, col}!')
        self.__pos = row, col

    # def __eq__(self, other):
    #     if isinstance(self, other):
    #         return True
    #     return False
    #
    # def __ne__(self, other):
    #     if isinstance(self, other):
    #         return False
    #     return True

    def __repr__(self):
        return 'ChessPiece'

    def __str__(self):
        return self.__repr__()


class Pawn(ChessPiece):
    def __init__(self, row: int, col: int, color: int):
        super().__init__(row, col, color)

    def can_move(self, row1: int, col1: int) -> bool:
        row, col = self.pos
        if (row - 1 == row1 or row + 1 == row1) and col == col1:
            return True
        return False

    def __repr__(self):
        return f'{colors[self.color]}P'


class Knight(ChessPiece):
    def __init__(self, row: int, col: int, color: int):
        super().__init__(row, col, color)

    def can_move(self, row1: int, col1: int) -> bool:
        row, col = self.pos
        if abs(row - row1) == 2 and abs(col - col1) == 1 or abs(row - row1) == 1 and abs(col - col1) == 2:
            return True
        return False

    def __repr__(self):
        return f'{colors[self.color]}Kn'


class Bishop(ChessPiece):
    def __init__(self, row: int, col: int, color: int):
        super().__init__(row, col, color)

    def can_move(self, row1: int, col1: int) -> bool:
        row, col = self.pos
        if abs(row - row1) == abs(col - col1) > 0:
            return True
        return False

    def __repr__(self):
        return f'{colors[self.color]}B'


class Rook(ChessPiece):
    def __init__(self, row: int, col: int, color: int):
        super().__init__(row, col, color)

    def can_move(self, row1: int, col1: int) -> bool:
        row, col = self.pos
        if row != row1 and col == col1 or col != col1 and row == row1:
            return True
        return False

    def __repr__(self):
        return f'{colors[self.color]}R'


class Queen(Bishop, Rook):
    def __init__(self, row: int, col: int, color: int):
        super().__init__(row, col, color)

    def can_move(self, row1: int, col1: int) -> bool:
        if Bishop.can_move(self, row1, col1):
            return True
        if Rook.can_move(self, row1, col1):
            return True
        return False

    def __repr__(self):
        return f'{colors[self.color]}Q'


class King(ChessPiece):
    def __init__(self, row: int, col: int, color: int):
        super().__init__(row, col, color)

    def can_move(self, row1: int, col1: int) -> bool:
        row, col = self.pos
        if abs(row - row1) == 1 or abs(col - col1) == 1:
            return True
        return False

    def __repr__(self):
        return f'{colors[self.color]}K'
