from flask import request

from .controllers import  list_all_movies_controller

from ..app import app

@app.route("/movies", methods=['GET'])
def list_create_movies():
    if request.method == 'GET': return list_all_movies_controller()
    else: return 'Method is Not Allowed'