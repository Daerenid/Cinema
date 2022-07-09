from app import db

class Cinema(db.Model):
    __tablename__ = 'cinema'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(104))
    films = db.relationship(
        'Film', backref='cinema', lazy=True
    )

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(104))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(104))

class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(104))
    repertoire = db.Column(db.String(1048))
    duration = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
    vote_count = db.Integer(db.Column(db.Integer))
    release_date = db.Column(db.Date)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))