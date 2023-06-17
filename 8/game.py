from chess import Player, ChessBoard
from figures import ChessPiece
from exceptions import PieceNotFound, PieceCannotMoveError, ColorError, MoveToYourPieceError


class Game:
    def __init__(self, p1: Player, p2: Player):
        self.__p1 = p1
        self.__p2 = p2
        self.__chess_board = ChessBoard(self.__p1, self.__p2)
        self.__step = 0
        self.is_over = False

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    @property
    def chess_board(self):
        return self.__chess_board

    @chess_board.setter
    def chess_board(self, chess_board):
        self.__chess_board.board = chess_board

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        self.__step = step

    def new_step(self, row: int, col: int, row1: int, col1: int):
        piece1 = self.chess_board.board[row - 1][col - 1]
        piece1.move(row1 - 1, col1 - 1)
        piece2 = self.chess_board.board[row1 - 1][col1 - 1]
        if isinstance(piece2, ChessPiece):
            if piece1.color != piece2.color:
                print(f'{str(piece1)} съел {str(piece2)}!')
                if self.__p1.color == self.__step:
                    self.__p2.pieces.remove(piece2)
                    if not self.__p2.pieces:
                        self.is_over = True
                else:
                    self.__p1.pieces.remove(piece2)
                    if not self.__p1.pieces:
                        self.is_over = True
                del piece2
        self.__step = (self.__step + 1) % 2
        self.__chess_board.update_board()

    def check_move(self, row: int, col: int, row1: int, col1: int) -> bool:
        if 1 <= row <= 8 and 1 <= col <= 8 and 1 <= row1 <= 8 and 1 <= col1 <= 8:
            piece = self.chess_board.board[row - 1][col - 1]
            if isinstance(piece, ChessPiece):
                if piece.color == self.__step:
                    if piece.can_move(row1 - 1, col1 - 1):
                        piece1 = self.chess_board.board[row1 - 1][col1 - 1]
                        if isinstance(piece1, ChessPiece):
                            if piece.color != piece1.color:
                                return True
                            else:
                                raise MoveToYourPieceError
                        else:
                            return True
                    else:
                        raise PieceCannotMoveError
                else:
                    raise ColorError
            else:
                raise PieceNotFound