from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Pole wymagane!')])
    password = PasswordField('Password', validators=[DataRequired('Pole wymagane!')])
    submit = SubmitField('Sign In')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Podana nazwa użytkownika nie istnieje')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Pole wymagane!')])
    email = StringField('Email Address', validators=[DataRequired('Pole wymagane!'), Email('Niepoprawny adres email')])
    password = PasswordField('Password', [
        validators.DataRequired('Pole wymagane!')])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Wybrana nazwa użytkownika jest zajęta')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Wybrany adres email jest już zajęty')

class NewFilm(FlaskForm):
    name = StringField('Nazwa', validators=[DataRequired()])
    repertoire = StringField('Repertuar')
    

class NewCinema(FlaskForm):
    name = StringField('Nazwa', validators=[DataRequired()])