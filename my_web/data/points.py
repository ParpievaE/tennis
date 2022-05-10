import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Points(SqlAlchemyBase):
    __tablename__ = 'points'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_p = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('players.id_p'))
    id_t = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tournaments.id_t'))
    points = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    player = orm.relation('Player')
    tournament = orm.relation('Tournaments')
