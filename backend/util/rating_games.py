from .game_schedule import get_games_by_date
from .boxscore import get_boxscore_by_link
from .rating_boxscore import get_game_rating_by_boxscore
from datetime import datetime
from ..models import models


def format_rating(entries):
    result = {}
    for idx, entry in enumerate(entries):
        result[idx] = {
            'name': entry.game_name,
            'id': entry.id,
            'link': f'https://www.espn.com/nba/game/_/gameId/{entry.id}',
            'boxscore_link': f'https://www.espn.com/nba/boxscore/_/gameId/{entry.id}',
            'ratings': {   
                'competitive': entry.competitive_rating, 
                'high_scoring': entry.highscoring_rating,
                'less_ftas': entry.fta_rating,
                'less_fouls': entry.fouls_rating,
                'star_power': entry.star_power_rating,
            },
            'teams': {
                'winner': {
                    'team': entry.winning_team,
                    'record': entry.winning_team_record,
                    'score': entry.winner_score
                },
                'loser': {
                    'team': entry.losing_team,
                    'record': entry.losing_team_record,
                    'score': entry.loser_score
                }
            },
            'overall_rating': entry.overall_rating,
        }
    return result

def get_games_data_with_rating(db, date):   
    games = {}

    game_date = datetime.strptime(date, '%Y%m%d')
    if db.session.query(models.Rating).filter_by(game_date=game_date).first():
        entries = db.session.query(models.Rating).filter_by(game_date=game_date).order_by(models.Rating.overall_rating.desc()).all()
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
            winner_team = game['competitors'][0] if int(game['competitors'][0]['score']) > int(game['competitors'][1]['score']) else game['competitors'][1]
            loser_team = game['competitors'][0] if int(game['competitors'][0]['score']) < int(game['competitors'][1]['score']) else game['competitors'][1]
            # games[game_name]['teams'] = {}
            # for team in game['competitors']:
            #     games[game_name]['teams'][team['displayName']] = {
            #         'record': team['record'],
            #         'score': team['score']
            #     }
            winner = {
                'team': winner_team['displayName'],
                'record': winner_team['record'],
                'score': winner_team['score'],
            }
            loser = {
                'team': loser_team['displayName'],
                'record': loser_team['record'],
                'score': loser_team['score'],
            }

            games[game_name]['teams'] = {
                'winner': winner,
                'loser': loser
            }

        
    
            # winner = team['displayName'] if team['winner'] else None
            # differential = abs(int(game['competitors'][0]['score']) - int(game['competitors'][1]['score']))
            # print(f'{winner} won by {differential} points.')

            # print('----------Game Rating--------')
            pre, partition, post = game['link'].partition('game')
            boxscore_link = f'{pre}boxscore{post}' 
            games[game_name]['boxscore_link'] = boxscore_link
            gameBoxscore = get_boxscore_by_link(boxscore_link)
            
            ratings = get_game_rating_by_boxscore(gameBoxscore) 
            games[game_name]['ratings'] = ratings
            
            overall_rating = 0
            for r in ratings.values():
                overall_rating += r

            overall_rating /= len(ratings)
            
            games[game_name]['overall_rating'] = overall_rating

            game_data = {
                'game_name':game_name,
                'game_date':game_date, 
                'winner': winner,
                'loser': loser,
                'overall_rating': overall_rating,
            }

            game_rating = models.Rating(games[game_name]['id'], game_data, ratings)
            db.session.add(game_rating)
            db.session.commit()
            # print('---------------------------------')

        return games