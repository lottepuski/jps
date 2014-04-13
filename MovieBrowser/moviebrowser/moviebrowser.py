from helpers import (get_data_directory, get_resources_directory,
            get_db_filename)
import os.path as op

from db_actions import (add_genre, add_movie, commit_database,
            list_genres_from_database)

class MovieBrowser(object):
    """
    Creates the database
    """
    def __init__(self):
        self.database_exists = False
        self.check_if_database_exists()

    def check_if_database_exists(self):
        # Done : 24/3/2014
        db_filename = get_db_filename()
        if op.isfile(db_filename):
            print "{} : DataBase Exists".format(__file__)
            self.database_exists = True

    def list_genres(self):
        genres = Reader('u.genre').read()
        return genres

    def list_movies(self):
        movies = MovielistReader('u.item20').read()
        return movies

    def add_genres(self):
        genres = self.list_genres()
        print genres
        for (genre, genre_id) in genres.iteritems():
            add_genre(genre, genre_id)

    def add_movies(self):
        movies = self.list_movies()
        print movies
        for (title, genre_list) in movies.iteritems():
            add_movie(title, genre_list)

    def finalize_db(self):
        commit_database()
        self.database_exists = True

    def init_database(self):
        self.database_exists = False
        self.add_genres()
        self.add_movies()
        self.finalize_db()

    def list_available_genres(self):
        if not(self.database_exists):
            print "No genres exist. Please initialize database"
            return
        list_genres_from_database()

class Reader(object):
    """
    Read Files from Movielens dataset
    """
    def __init__(self, filename):
        data_dir = get_data_directory()
        self.filename = op.join(data_dir, filename)
        self.fh = open(self.filename, 'r')

    def read(self):
        elements = dict()
        for line in self.fh:
            attribs = line.strip().split('|')
            if len(attribs) >= 2:
                print attribs
                elements[attribs[0]] = map(int, attribs[1:])
        return elements

class MovielistReader(Reader):
    """
    Read Files from Movielens dataset
    """
    def __init__(self, filename):
        super(MovielistReader, self).__init__(filename)

    def read(self):
        elements = dict()
        for line in self.fh:
            attribs = line.strip().split('|')
            if len(attribs) >= 2:
                print attribs
                elements[attribs[1]] = map(int, attribs[5:])
        return elements




