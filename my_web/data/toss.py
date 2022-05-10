import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Toss(SqlAlchemyBase):
    __tablename__ = 'toss'

    id_toss = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    pair_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    id_p_1 = sqlalchemy.Column(sqlalchemy.Integer)
    id_p_2 = sqlalchemy.Column(sqlalchemy.Integer)
    id_t = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('tournaments.id_t'))

    # player = orm.relation('Player')
    tournament = orm.relation('Tournaments')
