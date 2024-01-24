from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv

from .extensions import db
from .routes import main

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Local database on machine
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{os.getenv("PASSWORD")}@localhost/nbaapp'

    # External hosted database on render
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    CORS(app)   

    db.init_app(app)

    app.register_blueprint(main)
    return app 


if __name__ == '__main__':
    app = create_app()
    app.run()