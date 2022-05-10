import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Tournaments(SqlAlchemyBase):
    __tablename__ = 'tournaments'

    id_t = sqlalchemy.Column(sqlalchemy.Integer,
                             primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    place = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    number_of_players = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    points = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id_u"))
    user = orm.relation('User')

    def __repr__(self):
        return ' '.join(
            ['<Tournaments>', str(self.id_t), self.title, str(self.year), self.place, str(self.number_of_players), str(self.points)])
