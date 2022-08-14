import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

MYSQL_HOST = "db"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "test"
MYSQL_PORT = 3306
MYSQL_CURSORCLASS = 'DictCursor'