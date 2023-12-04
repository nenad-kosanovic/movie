from flask import jsonify
import requests


def list_all_movies_controller():
    return requests.get("http://localhost:5000/movies").json()
