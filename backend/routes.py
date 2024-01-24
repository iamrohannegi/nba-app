from flask import Blueprint

from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def greet():
    return "Hello world"

from .util import rating_games
@main.route('/games/<date>', methods=['GET'])
def rated_games(date): 
    return rating_games.get_games_data_with_rating(db, date)

@main.route('/games/top', methods=['GET'])
def top_games():
    return rating_games.get_top_rated_games(db)