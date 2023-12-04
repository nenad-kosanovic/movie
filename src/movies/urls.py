from flask import request

from src.movies.controllers import create_movie_controller, delete_movie_controller, list_all_movies_controller, retrieve_movie_controller, update_movie_controller

from ..app import app

@app.route("/movies", methods=['GET', 'POST'])
def list_create_movies():
    if request.method == 'GET': return list_all_movies_controller()
    if request.method == 'POST': return create_movie_controller()
    else: return 'Method is Not Allowed'
    

@app.route("/movies/<movie_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_movies(movie_id):
    if request.method == 'GET': return retrieve_movie_controller(movie_id)
    if request.method == 'PUT': return update_movie_controller(movie_id)
    if request.method == 'DELETE': return delete_movie_controller(movie_id)
    else: return 'Method is Not Allowed'    