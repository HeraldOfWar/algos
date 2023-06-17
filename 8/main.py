from data import db_session
from data.users import User
from threading import Thread, Timer
from game import Game
from chess import Player
from exceptions import PieceNotFound, PieceCannotMoveError, ColorError, MoveToYourPieceError


def add_user(p: Player):
    user = db_sess.query(User).filter(User.name == p.name).first()
    if not user:
        user = User(name=p.name)
        db_sess.add(user)
        db_sess.commit()


def get_coffee():
    print('\nЧто-то игра затягивается... Хотите кофе?')


p1 = Player(input('Игрок №1, представьтесь: '), 0)
p2 = Player(input('Игрок №2, представьтесь: '), 1)
game = Game(p1, p2)
game.chess_board.print_board()
db_session.global_init("db/chess_users.db")
db_sess = db_session.create_session()
t1, t2 = Thread(target=add_user(p1)), Thread(target=add_user(p2))
t1.start()
t2.start()

while not game.is_over:
    timer = Timer(15.0, get_coffee)
    timer.start()
    try:
        if game.step == 0:
            s = p1.name
        else:
            s = p2.name
        row, col = [int(i) for i in input(f'{s}! Введите через пробел координаты фигуры, которую переместить: ').split()]
        row1, col1 = [int(i) for i in
                      input('Введите через пробел координаты поля, куда хотите переместить фигуру: ').split()]
        game.check_move(row, col, row1, col1)
        game.new_step(row, col, row1, col1)
        game.chess_board.print_board()
        print()
    except ValueError:
        print('Координаты введены некорректно!')
    except PieceNotFound:
        print('В этой клетке нет вашей фигуры! Выберите клетку, на которой находится ваша фигура.')
    except ColorError:
        print('Эта чужая фигура! Пожалуйста, выберите свою.')
    except PieceCannotMoveError:
        print('Ваша фигура не умеет так ходить! Выберите другую клетку, в которую хотите переместиться.')
    except MoveToYourPieceError:
        print('В клетке, на которую вы хотите переместиться, уже стоит ваша фигура! Выберите другую клетку.')


if game.step == p1.color:
    print(f'Победил {p2.name}!')
else:
    print(f'Победил {p1.name}!')
