from nose.tools import *
from moviebrowser.moviebrowser import *

def setup():
    print "SETUP"

def teardown():
    print "TEARDOWN!!!"

def test_basic():
    assert 1==1

def test_python_version():
    import sys
    print sys.version_info
    assert sys.version_info > (2,6)

def test_class_exists():
    browser = MovieBrowser()

def test_imports():
    from moviebrowser.moviebrowser import MovieBrowser
    from collections import OrderedDict
    from collections import defaultdict
    import copy
    import json
    import sqlalchemy

def test_sqlalchemy_version():
    import sqlalchemy
    print "SQLAlchemy version {:}".format(sqlalchemy.__version__)
    assert map(int, sqlalchemy.__version__.split(".")) > [0, 7, 8]

def test_database():
    pass
