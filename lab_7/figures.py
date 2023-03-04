class ChessFigure:
    def __init__(self, x: int, y: int):
        self.__pos_x = x
        self.__pos_y = y
        self.__moves = []
        self.add_move(*self.get_pos())

    def get_pos(self) -> tuple:
        return self.__pos_x, self.__pos_y

    def set_pos(self, x1: int, y1: int) -> None:
        self.__pos_x, self.__pos_y = x1, y1

    def can_move(self, x1: int, y1: int) -> bool:
        return True

    def add_move(self, x1: int, y1: int) -> None:
        if self.can_move(x1, y1):
            if f'{x1}{y1}' not in self.get_moves():
                self.__moves.append(f'{x1}{y1}')

    def get_moves(self) -> list:
        return self.__moves


class Pawn(ChessFigure):
    def can_move(self, x1: int, y1: int) -> bool:
        x, y = self.get_pos()
        if x - 1 == x1 and y == y1:
            return True
        return False


class Knight(ChessFigure):
    def can_move(self, x1: int, y1: int) -> bool:
        x, y = self.get_pos()
        if abs(x - x1) == 2 and abs(y - y1) == 1 or abs(x - x1) == 1 and abs(y - y1) == 2:
            return True
        return False


class Bishop(ChessFigure):
    def can_move(self, x1: int, y1: int) -> bool:
        x, y = self.get_pos()
        if abs(x - x1) == abs(y - y1) != 0:
            return True
        return False


class Rook(ChessFigure):
    def can_move(self, x1: int, y1: int) -> bool:
        x, y = self.get_pos()
        if abs(x - x1) > 0 and y - y1 == 0 or abs(y - y1) > 0 and x - x1 == 0:
            return True
        return False


class Queen(ChessFigure):
    def can_move(self, x1: int, y1: int) -> bool:
        x, y = self.get_pos()
        if abs(x - x1) > 0 and y - y1 == 0 or abs(y - y1) > 0 and x - x1 == 0:
            return True
        if abs(x - x1) == abs(y - y1) != 0:
            return True
        return False


class King(ChessFigure):
    def can_move(self, x1: int, y1: int) -> bool:
        x, y = self.get_pos()
        if abs(x - x1) == 1 or abs(y - y1) == 1:
            return True
        return False
