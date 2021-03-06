from flask import Flask
from flask import render_template, redirect, make_response, request, session, abort
from data import db_session
from data.players import Player
import datetime
from data.tournaments import Tournaments
from data.users import User
from data.points import Points
from data.toss import Toss
from forms.user import RegisterForm
from forms.user import LoginForm
from forms.tournaments import TournamentForm
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/tennis_w.db")
    db_sess = db_session.create_session()

    # points = Points()
    # points.id_p = 1
    # points.id_t = 1
    # points.points = 100
    # db_sess.add(points)
    # db_sess.commit()

    # toss = Toss()
    # toss.pair_number = 1
    # toss.id_p_1 = 1
    # toss.id_p_2 = 2
    # toss.id_t = 1
    # db_sess.add(toss)
    # db_sess.commit()

    # tournament = Tournaments()
    # tournament.title = "Турнир 2"
    # tournament.year = 2022
    # tournament.place = "Вологда"
    # tournament.user_id = 1
    # db_sess.add(tournament)
    # db_sess.commit()

    # player = Player()
    # player.name = "Вася"
    # player.gender = "м"
    # player.age = 14
    # player.user_id = 1
    # db_sess.add(player)
    # db_sess.commit()

    # user = User()
    # user.name = "Пользователь 3"
    # user.email = "email3@email.ru"
    # user.set_password('456')
    #
    # db_sess.add(user)
    # db_sess.commit()

    # @app.route("/")
    # def index():
    #     db_sess = db_session.create_session()
    #
    #     if current_user.is_authenticated:
    #         news = db_sess.query(News).filter(
    #             (News.user == current_user) | (News.is_private != True))
    #     else:
    #         news = db_sess.query(News).filter(News.is_private != True)
    #
    #     return render_template("index.html", news=news)

    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    tourn = db_sess.query(Tournaments).all()
    # print(tourn)
    return render_template("index1.html", tourn=tourn)

    # for user in db_sess.query(User).all():
    #     print(user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/new_tournament', methods=['GET', 'POST'])
@login_required
def new_tournament():
    form = TournamentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        tournaments = Tournaments()
        tournaments.title = form.title.data
        tournaments.year = form.year.data
        tournaments.place = form.place.data
        tournaments.number_of_players = form.number_of_p.data
        tournaments.points = form.points.data
        current_user.tournaments.append(tournaments)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('new_tournament.html', title='Добавление турнира',
                           form=form)


if __name__ == '__main__':
    main()
