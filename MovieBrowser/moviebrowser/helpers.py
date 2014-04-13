import os.path as op

resources_dirname   = 'resources'
tests_dirname       = 'tests'
dataset_name        = 'ml-100k'
database_name       = 'movielens.db'

def get_src_directory():
    return op.dirname(op.realpath(__file__))

def get_base_directory():
    return op.dirname(get_src_directory())

def get_resources_directory():
    return op.join(get_base_directory(), resources_dirname)

def get_data_directory():
    return op.join(get_resources_directory(), dataset_name)

def get_tests_directory():
    return op.join(get_base_directory(), tests_dirname)

def get_db_filename():
    return op.join(get_src_directory(), database_name)
