import os
# Just get the current directory .
basedir = os.path.abspath(os.path.dirname(__file__))
# Get the database URL from the environment variable, if available
# otherwise give the database a default name 'app.db'
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False