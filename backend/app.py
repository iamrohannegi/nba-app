from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv
    

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{os.getenv("PASSWORD")}@localhost/nbaapp'
db = SQLAlchemy(app) 
CORS(app)



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