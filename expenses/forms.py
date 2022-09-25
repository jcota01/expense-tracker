from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import InputRequired


class ExpenseForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    price = FloatField(validators=[InputRequired()])
    category = StringField(validators=[InputRequired()])
    submit = SubmitField()
