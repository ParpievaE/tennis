from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional


class TournamentForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    year = IntegerField('Год проведения')
    place = StringField("Место проведения")
    number_of_p = IntegerField('Количество участников', validators=[Optional()])
    points = IntegerField('Баллы', validators=[Optional()])
    submit = SubmitField('Применить')