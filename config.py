<<<<<<< HEAD
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = 'postgresql://patty:pos02@localhost:5432/fyyur_db'
=======
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

<<<<<<< HEAD

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
>>>>>>> 3891aaf (updated starter code into root from starter_code folder)
=======
SQLALCHEMY_DATABASE_URI = 'postgresql://patty:pos02@localhost:5432/fyyur_db'
>>>>>>> 5769ef4 (Edit app for real data, separation of concerns)
