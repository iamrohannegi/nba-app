from util.game_schedule import get_games_by_date
from util.boxscore import get_boxscore_by_link
from util.rating_boxscore import get_game_rating_by_boxscore

def get_games_data_with_rating(date):   
    games = {}

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
        boxscoreLink = f'{pre}boxscore{post}' 
        games[game_name]['boxscoreLink'] = boxscoreLink
        gameBoxscore = get_boxscore_by_link(boxscoreLink)
        games[game_name]['ratings'] = get_game_rating_by_boxscore(gameBoxscore) 
        # print('---------------------------------')

    return games