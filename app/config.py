import os

# Configuration class for the Flask application


class Config:
    # Secret key for securing sessions and cookies
    SECRET_KEY = os.urandom(24)

    # URI for the SQLite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # Disable modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
