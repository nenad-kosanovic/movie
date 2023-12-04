from dataclasses import dataclass, field
from typing import List, Optional
from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from .. import db # from __init__.py


@dataclass
class Genre(db.Model):
    id: str
    name: str
    
    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    name         = db.Column(db.String(225), nullable=False)
 
@dataclass
class Movie(db.Model):
    id: str
    created: datetime
    updated: datetime
    name: str
    language: str
    runtime: int
    description: str
    
    # Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update
    
    # Input by User Fields:
    name         = db.Column(db.String(225), nullable=False)
    language     = db.Column(db.String(100))
    runtime      = db.Column(db.BigInteger)
    description  = db.Column(db.Text)

    genres = db.relationship("MovieGenre", back_populates='movie')   
    
class MovieGenre(db.Model)    :
    movie        = db.relationship("Movie", back_populates="genres")
    genre_id     = db.Column('genre_id', db.String, db.ForeignKey('genre.id'), primary_key=True)
    movie_id     = db.Column('movie_id', db.String, db.ForeignKey('movie.id'), primary_key=True)
