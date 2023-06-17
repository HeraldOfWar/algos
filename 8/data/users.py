import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    """Модели записи"""
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    win = sqlalchemy.Column(sqlalchemy.String, default=0)
    loose = sqlalchemy.Column(sqlalchemy.String, default=0)

    def __repr__(self):
        return f'<User> {self.name}'