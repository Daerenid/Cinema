from app import app
from app.models import Film, Cinema
from flask import request
from flask import jsonify
import json

@app.route('/cinemas', methods=['POST', 'GET'])
def cinemas():
    json_cinemas = [
        cinema.to_Json() for cinema in Cinema.get_cinemas()
    ]
    return jsonify(json_cinemas)

@app.route('/movies/<cinema_id>', methods=['POST', 'GET'])
def movies(cinema_id):
    cinema = Cinema.get_cinema(cinema_id)
    json_films = [
        film.to_Json() for film in cinema.films
    ]  
    if cinema == None:
        return jsonify({'error': 'Cinema not found'})
    return jsonify(json_films)

@app.route('/movies_upvote/<id>',  methods=['POST', 'GET'] )
def upvote_movie(id):
    film = Film.get_film(id)
    if film == None:
        return jsonify({'error': 'Film not found'})
    film.upp_vote()
    return jsonify(film.to_Json()) 

@app.route('/addmovie', methods=['POST'] )
def add_film():
    content = request.json
    cinema = Cinema.get_cinema(content['cinema_id'])
    if cinema == None:
        return jsonify({'error' : 'Cinema not found'})
    film = Film(
        name = content['name'], 
        year = content['year'],
        description = content['description'],
        posterurl = content['posterurl'], 
        movieurl = content['movieurl'], 
        cinema_id = int(content['cinema_id'])
    )
    cinema.add_film(film)

    return jsonify({'status': 'success'})

@app.route('/addcinema',  methods=['POST'] )
def add_cinema():
    content = request.json
    cinema = Cinema(name = content['name'])
    cinema.add_cinema()

    return jsonify({'status': 'success'})
