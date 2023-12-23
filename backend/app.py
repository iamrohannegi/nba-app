from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from util.rating_games import get_games_data_with_rating
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{os.getenv("PASSWORD")}@localhost/nbaapp'
db = SQLAlchemy(app) 

@app.route('/')
def greet():
    return "Hello world"

@app.route('/games/<date>', methods=['GET'])
def ratedGames(date): 
    return get_games_data_with_rating(date)

if __name__ == '__main__':
    app.run()