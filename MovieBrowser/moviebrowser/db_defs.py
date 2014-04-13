#!/usr/bin/python

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from db_actions import Base, get_genre_by_tag

association_table = Table('association', Base.metadata,
        Column('genre_id', Integer, ForeignKey('Genre.id')),
        Column('movie_id', Integer, ForeignKey('Movie.id')))

class Genre(Base):
    """
    """
    __tablename__ = "Genre"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre_tag = Column(Integer)
    movies = relationship("Movie",
            secondary=association_table,
            backref="genres")

    def __init__(self, name, genre_tag):
        """
        """
        self.name = name
        self.genre_tag = genre_tag[0]

class Movie(Base):
    """
    """
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None, genre_list=None):
        self.name = name
        count = 0
        for count in xrange(len(genre_list)):
            if genre_list[count]:
                genre_tag = count
                genre = get_genre_by_tag(genre_tag)
                self.genres.append(genre)
            count += 1

