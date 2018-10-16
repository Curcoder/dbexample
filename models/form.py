from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import InputRequired, Length, DataRequired


class SignupForm(FlaskForm):
    username = StringField('Username', [InputRequired(message='Fill username, dipshit!')])
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Submit')