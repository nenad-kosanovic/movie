from flask import request, jsonify
import uuid

from .. import db
from .models import Movie
from sqlalchemy.orm import selectinload
# ----------------------------------------------- #


def list_all_movies_controller():
    movies = Movie.query.options(selectinload(Movie.genres)).all()
    return jsonify(movies)


def create_movie_controller():
    req_json = request.get_json()

    id = str(uuid.uuid4())
    new_movie = Movie(
        id=id,
        name=req_json["name"],
        language=req_json["language"],
        runtime=req_json["runtime"],
        description=req_json["description"],
    )
    db.session.add(new_movie)
    db.session.commit()

    return jsonify(Movie.query.get(id))


def retrieve_movie_controller(movie_id):
    return jsonify(Movie.query.get(movie_id))


def update_movie_controller(movie_id):
    req_json = request.get_json()
    movie = Movie.query.get(movie_id)

    movie.name = req_json["name"]
    movie.language = req_json["language"]
    movie.runtime = req_json["runtime"]
    movie.description = req_json["description"]
    db.session.commit()
    
    return jsonify(Movie.query.get(movie_id))


def delete_movie_controller(movie_id):
    Movie.query.filter_by(id=movie_id).delete()
    db.session.commit()

    return ('Movie with Id "{}" deleted successfully!').format(movie_id)
