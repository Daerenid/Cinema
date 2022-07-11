from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm, NewFilm, NewCinema
from app.models import User, Film, Cinema
from flask_login import login_user, current_user, logout_user
import json

@app.route('/', methods=['GET', 'POST'])
def homepage():

    cinemas = Cinema.get_cinemas()
    return render_template('index.html',
    cinemas=cinemas)


@app.route('/admin', methods=['GET', 'POST'])
@app.route('/admin/id=<id>', methods=['GET', 'POST'])
def admin(id=None):
    login_form = LoginForm()
    register_form = RegistrationForm()
    film_form = NewFilm()
    cinema_form = NewCinema()
    
    if login_form.submit_login.data and login_form.validate_on_submit():
        username_login = login_form.username_login.data
        password_login = login_form.password_login.data
        user = User.query.filter_by(username=username_login).first()
        if user is None or not user.check_password(password_login):
            flash('Niepoprawny login lub hasło')
            return redirect(url_for('admin'))
        login_user(user)

    if register_form.submit_register.data and register_form.validate_on_submit():
        username_register = register_form.username_register.data
        password_register = register_form.password_register.data
        email_register = register_form.email_register.data
        user = User(username=username_register, email=email_register)
        user.set_password(password_register)
        user.add_user()
        return redirect(url_for('admin'))

    if cinema_form.validate_on_submit() and cinema_form.submit.data:
        name = cinema_form.name_cinema.data
        cinema = Cinema(name=name)
        cinema.add_cinema()
        return redirect(url_for('admin'))

    elif film_form.validate_on_submit() and film_form.submit.data:
        print('jestem w film')
        name = film_form.name_film.data
        repertoire = film_form.repertoire.data
        duration = film_form.duration.data
        status = False
        vote_count = 0
        cinema = Cinema.get_cinema(id)
        film = Film(name=name, repertoire=repertoire, duration=duration, status=status, vote_count=vote_count, cinema_id=id)
        cinema.add_film(film)
        return redirect(url_for('admin'))

    cinemas = Cinema.get_cinemas()

    return render_template('admin.html',
    login_form=login_form,
    register_form=register_form,
    film_form=film_form,
    cinema_form=cinema_form,
    cinemas=cinemas
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

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
    if(film.vote_count == None):
        film.vote_count = 0;
    film.vote_count += 1;
    db.session.commit()
    return json.dumps(film)