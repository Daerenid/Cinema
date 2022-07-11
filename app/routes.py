from app import app
from app.models import Film, Cinema
from flask_login import login_user, current_user, logout_user
import json
from flask import request, url_for

@app.route('/cinemas', methods=['POST', 'GET'])
def cinemas():
    json_cinemas = [
        cinema.to_Json() for cinema in Cinema.get_cinemas()
    ]
    return json.dumps(json_cinemas)

@app.route('/movies/<cinema_id>', methods=['POST', 'GET'])
def movies(cinema_id):
    cinema = Cinema.get_cinema(cinema_id)
    json_films = [
        film.to_Json() for film in cinema.films
    ]
    if(cinema == None):
        return json.dumps({'error': 'Cinema not found'})
    return json.dumps(json_films)

@app.route('/movies_upvote/<id>',  methods=['POST', 'GET'] )
def upvote_movie(id):
    film = Film.get_film(id)
    if(film == None):
        return json.dumps({'error': 'Film not found'})
    film.upp_vote()
    return json.dumps(film.to_Json()) 

@app.route('/addmovie', methods=['POST'] )
def add_film():
    content = request.json
    cinema = Cinema.get_cinema(content['cinema_id'])
    film = Film(
        name = content['name'], 
        year = content['year'],
        description = content['description'], 
        vote_count = content['vote_count'],
        posterurl = content['posterurl'], 
        movieurl = content['movieurl'], 
        cinema_id = int(content['cinema_id'])
    )
    cinema.add_film(film)

    return json.dumps({'status': 'success'})

@app.route('/addcinema',  methods=['POST'] )
def add_cinema():
    content = request.json
    cinema = Cinema(name = content['name'])
    cinema.add_cinema()

    return json.dumps({'status': 'success'})
