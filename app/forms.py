from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email
from app.models import User

class LoginForm(FlaskForm):
    username_login = StringField('Username', validators=[DataRequired('Pole wymagane!')])
    password_login = PasswordField('Password', validators=[DataRequired('Pole wymagane!')])
    submit_login = SubmitField('Sign In')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Podana nazwa użytkownika nie istnieje')

class RegistrationForm(FlaskForm):
    username_register = StringField('Username', validators=[DataRequired('Pole wymagane!')])
    email_register = StringField('Email Address', validators=[DataRequired('Pole wymagane!'), Email('Niepoprawny adres email')])
    password_register = PasswordField('Password', [
        validators.DataRequired('Pole wymagane!')])
    submit_register = SubmitField('Dodaj')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Wybrana nazwa użytkownika jest zajęta')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Wybrany adres email jest już zajęty')

class NewCinema(FlaskForm):
    name_cinema = StringField('Nazwa', validators=[DataRequired()])
    submit = SubmitField('Dodaj')
class NewFilm(FlaskForm):
    name_film = StringField('Nazwa', validators=[DataRequired()])
    repertoire = StringField('Repertuar')
    duration = StringField('Czas trwania')
    submit = SubmitField('Dodaj')
