from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .models import db
from flask_migrate import Migrate

# Function to create and configure the Flask application


def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Load the configuration from the Config class
    app.config.from_object(Config)

    # Initialize the SQLAlchemy database instance with the Flask app
    db.init_app(app)

    # Initialize Flask-Migrate with the app and database
    migrate = Migrate(app, db)

    # Import the routes and create the database tables within the app context
    with app.app_context():
        from . import routes
        db.create_all()

    # Return the configured Flask app instance
    return app
