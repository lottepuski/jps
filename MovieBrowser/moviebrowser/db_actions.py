#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movielens.db', echo=False)
Base = declarative_base()

def get_genre_by_tag(tag):
    """
    genre_tag is a number that is used to identify the genre in the
    Movielens dataset
    """
    genre = session.query(Genre).filter_by(genre_tag=tag).first()
    return genre

from db_defs import Genre, Movie

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_genre(genre, genre_id):
    curr_genre = Genre(genre, genre_id)
    session.add(curr_genre)

def add_movie(title, genre_list):
    curr_movie = Movie(title, genre_list)
    session.add(curr_movie)

def commit_database():
    session.commit()

def list_genres_from_database():
    genres = session.query(Genre).all()
    for genre in genres:
        print "Id: {}, name: {}, tag: {}".format(genre.id, genre.name,
                genre.genre_tag)
        print "--- has {} of movies".format(len(genre.movies))
