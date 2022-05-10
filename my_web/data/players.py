import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class Player(SqlAlchemyBase):
    __tablename__ = 'players'

    id_p = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    gender = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    total_points = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("users.id_u"))
    user = orm.relation('User')


