from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()


def create_app():
    app = Flask(__name__)

    # Local database on machine
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{os.getenv("PASSWORD")}@localhost/nbaapp'

    # External hosted database on render
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    CORS(app)

    return app 

app = create_app()
db = SQLAlchemy(app) 


@app.route('/')
def greet():
    return "Hello world"

import backend.util.rating_games as rating_games
@app.route('/games/<date>', methods=['GET'])
def rated_games(date): 
    return rating_games.get_games_data_with_rating(db, date)

@app.route('/games/top', methods=['GET'])
def top_games():
    return rating_games.get_top_rated_games(db)

if __name__ == '__main__':
    app.run()