from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .models import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
