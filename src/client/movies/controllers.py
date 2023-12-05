from google.protobuf.json_format import MessageToJson
import requests

from pypkg.pb.movie_pb2 import MovieProto


def list_all_movies_controller():
    return requests.get("http://localhost:5000/movies").json()

def retrieve_movie_controller(movie_id):
    url = "http://localhost:5000/movies/{0}?format=protobuf".format(movie_id)
    response = requests.get(url, headers={'Content-Type': 'application/protobuf'})
    
    movie_proto = MovieProto()
    movie_proto.ParseFromString(response.content)
    
    return MessageToJson(movie_proto)
