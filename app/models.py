from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Cinema(db.Model):
    __tablename__ = 'cinema'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(104))
    films = db.relationship(
        'Film', backref='cinema', lazy=True
    )

    def add_film(self, film):
        self.films.append(film)
        db.session.add(film)
        db.session.commit()

    def add_cinema(self):
        db.session.add(self)
        db.session.commit()

    def get_cinemas():
        return Cinema.query.all()

    def get_cinema(id):
        return Cinema.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(104))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(104))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def add_user(self):
        db.session.add(self)
        db.session.commit()
class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(104))
    repertoire = db.Column(db.String(1048))
    duration = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
    vote_count = db.Column(db.Integer)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))