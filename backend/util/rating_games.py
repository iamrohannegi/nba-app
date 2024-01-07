from util.game_schedule import get_games_by_date
from util.boxscore import get_boxscore_by_link
from util.rating_boxscore import get_game_rating_by_boxscore
from datetime import datetime
import models 


def format_rating(entries):
    result = {}
    for entry in entries:
        result[entry.game_name] = {
            'id': entry.id,
            'link': f'https://www.espn.com/nba/game/_/gameId/{entry.id}',
            'boxscore_link': f'https://www.espn.com/nba/boxscore/_/gameId/{entry.id}',
            'ratings': {
                'fta_rating': entry.fta_rating,
                'fouls_rating': entry.fouls_rating,
                'competitive_rating': entry.competitive_rating, 
                'highscoring_rating': entry.highscoring_rating,
                'star_power_rating': entry.star_power_rating,
                'overall_rating': entry.overall_rating,
            }
        }
    return result

def get_games_data_with_rating(db, date):   
    games = {}

    game_date = datetime.strptime(date, '%Y%m%d')
    if db.session.query(models.Rating).filter_by(game_date=game_date).first():
        entries = db.session.query(models.Rating).filter_by(game_date=game_date).all()
        return format_rating(entries)
    else: 
        all_games = get_games_by_date(date)

        for game in all_games:
            game_name = game['name']
            games[game_name] = {
                'id': game['competitionId'],
                'link': game['link']
            }

            print('---Teams--')
            # winner = None
            games[game_name]['teams'] = {}
            for team in game['competitors']:
                games[game_name]['teams'][team['displayName']] = {
                    'record': team['record'],
                    'score': team['score']
                }
                # winner = team['displayName'] if team['winner'] else None
            # differential = abs(int(game['competitors'][0]['score']) - int(game['competitors'][1]['score']))
            # print(f'{winner} won by {differential} points.')

            # print('----------Game Rating--------')
            pre, partition, post = game['link'].partition('game')
            boxscore_link = f'{pre}boxscore{post}' 
            games[game_name]['boxscore_link'] = boxscore_link
            gameBoxscore = get_boxscore_by_link(boxscore_link)
            games[game_name]['ratings'] = get_game_rating_by_boxscore(gameBoxscore) 
            
            game_data = {
                'game_name':game_name,
                'game_date':game_date, 
            }
            game_rating = models.Rating(games[game_name]['id'], game_data, games[game_name]['ratings'])
            db.session.add(game_rating)
            db.session.commit()
            # print('---------------------------------')

        return games