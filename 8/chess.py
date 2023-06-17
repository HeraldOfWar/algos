from figures import Pawn, Knight, Bishop, Rook, Queen, King


def give_pieces_to_player(color: int, _list: list = []) -> list:
    for i in range(8):
        _list.append(Pawn(1 + 5 * color, i, color))
    _list.append(Rook(7 * color, 0, color))
    _list.append(Rook(7 * color, 7, color))
    _list.append(Knight(7 * color, 1, color))
    _list.append(Knight(7 * color, 6, color))
    _list.append(Bishop(7 * color, 2, color))
    _list.append(Bishop(7 * color, 5, color))
    _list.append(King(7 * color, 3 + color, color))
    _list.append(Queen(7 * color, 4 - color, color))
    return _list


class Player:
    def __init__(self, name: str, color: int):
        self.__name = name
        self.__color = color
        self.__pieces = give_pieces_to_player(self.__color)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pieces(self):
        return self.__pieces


class ChessBoard:
    def __init__(self, p1: Player, p2: Player):
        self.__p1 = p1
        self.__p2 = p2
        self.__board = []
        self.update_board()

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board

    def update_board(self):
        self.__board = [[0 for j in range(8)] for i in range(8)]
        for figure in self.__p1.pieces:
            row, col = figure.pos
            self.__board[row][col] = figure
        for figure in self.__p2.pieces:
            row, col = figure.pos
            self.__board[row][col] = figure

    def print_board(self):
        print(' \t' + '\t'.join([str(i) for i in range(1, 9)]))
        board = [[str(fig) for fig in row] for row in self.__board]
        for i, row in enumerate(board):
            print(str(i + 1), ' ', '\t'.join(row))

