from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class SignupForm(FlaskForm):
    username = StringField('Username', [InputRequired(message="Fill it out dumb fuck!")])
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Submit')