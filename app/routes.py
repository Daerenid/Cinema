from app import app
from app.models import Film, Cinema
from flask_login import login_user, current_user, logout_user
import json
from flask import request, url_for

@app.route('/cinemas')
def cinemas():
    return json.dumps(Cinema.get_cinemas())

@app.route('/movies/<cinema_id>')
def movies(cinema_id):
    cinema = Cinema.get_cinema(cinema_id)
    if(cinema == None):
        return json.dumps({'error': 'Cinema not found'})
    return json.dumps(cinema.films)

@app.route('/movies_upvote/<id>')
def upvote_movie(id):
    film = Film.get_film(id)
    if(film == None):
        return json.dumps({'error': 'Film not found'})
    film.upp_vote()
    return json.dumps(film) 

@app.route('/addmovie')
def add_film():
    content = request.json
    cinema = Cinema.get_cinema(content['cinema_id'])
    film = Film(name = content['name'], 
    description = content['description'], 
    posterurl = content['posterurl'], 
    movieurl = content['movieurl'], 
    cinema_id = int(content['cinema_id']))
    cinema.add_film(film)
    return json.dumps(film)

@app.route('/addcinema')
def add_cinema():
    content = request.json
    cinema = Cinema(name = content['name'])
    cinema.add_cinema()
    return json.dumps(cinema)