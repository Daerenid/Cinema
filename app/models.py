from app import db
from werkzeug.security import generate_password_hash, check_password_hash

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

    def to_Json(self):
        return {
            "id": self.id, 
            "name": self.name
        }

class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(104))
    year = db.Column(db.Integer)
    description = db.Column(db.String(1048))
    vote_count = db.Column(db.Integer, default=0)
    posterurl = db.Column(db.Text())
    movieurl = db.Column(db.String(1048))
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))

    def add_film(self):
        db.session.add(self)
        db.session.commit()

    def get_film(id):
        return Film.query.get(int(id))

    def upp_vote(self):
        self.vote_count += 1
        db.session.commit()

    def to_Json(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "description": self.description, 
            "vote_count": self.vote_count, 
            "movieurl": self.movieurl,
            "posterurl": self.posterurl,
            "cinema_id" : self.cinema_id,
            "year" : self.year
        }