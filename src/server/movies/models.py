from dataclasses import dataclass, field
from typing import List, Optional
from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from .. import db # from __init__.py


@dataclass
class Genre(db.Model):
    id: str = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    name: str = db.Column(db.String(225), nullable=False)
    
@dataclass
class Movie(db.Model):
    id: str = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created: datetime = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated: datetime = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    name: str = db.Column(db.String(225), nullable=False)
    language: str = db.Column(db.String(100))
    runtime: int = db.Column(db.BigInteger)
    description: str = db.Column(db.Text)
    
    genres = db.relationship("MovieGenre", back_populates='movie')   
    
class MovieGenre(db.Model)    :
    movie        = db.relationship("Movie", back_populates="genres")
    genre_id     = db.Column('genre_id', db.String, db.ForeignKey('genre.id'), primary_key=True)
    movie_id     = db.Column('movie_id', db.String, db.ForeignKey('movie.id'), primary_key=True)
