import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id_u = sqlalchemy.Column(sqlalchemy.Integer,
                             primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    tournaments = orm.relation("Tournaments", back_populates='user')
    players = orm.relation("Player", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def get_id(self):
        return self.id_u

    def __repr__(self):
        return ' '.join(['<User>', str(self.id_u), self.name, self.email])
