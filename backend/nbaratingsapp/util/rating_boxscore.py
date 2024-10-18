import re

# League Average boxscore (Data taken on 22 December 2023)
LEAGUE_AVG = {
    '3PT': '12.7-34.9',
    'AST': '26.2',
    'BLK': '5.1',
    'DREB': '32.8',
    'FG': '42.1-89.3',
    'FTA': '23',
    'OREB': '11.0',
    'PF': '19.9',
    'PTS': '115',
    'REB': '43.8',
    'STL': '7.5',
    'TO': '14.1'
}

# List contains TOP 50 Players based on some online list (in no order)
STARS = ['D. DeRozan', 'J. Holiday', 'L. Markkanen', 'F. VanVleet', 'R. Gobert', 'P. Banchero', 'L. Ball', 'F. Wagner', 'D. Russell', 'M. Porter Jr.', 'J. Valančiūnas', 'E. Mobley', 'P. Siakam', 'J. Randle', 'M. Bridges', 'D. Murray', 'J. Butler', 'K. Leonard', 'K. Irving', 'J. Brown', 'S. Barnes', 'P. George', 'T. Harris', 'D. Booker', 'K. Porziņģis', 'Z. Williamson', 'A. Şengün', 'D. Mitchell', 'B. Ingram', 'C. Holmgren', 'B. Adebayo', 'J. Brunson', 'D. Lillard', 'A. Edwards', 'K. Towns', 'D. Fox', 'D. Sabonis', 'S. Curry', 'A. Davis', 'T. Young', 'L. Dončić', 'L. James', 'T. Maxey', 'J. Tatum', 'K. Durant', 'T. Haliburton', 'G. Antetokounmpo', 'J. Embiid', 'S. Gilgeous-Alexander', 'N. Jokić']

def get_score_differential_rating(scoreA, scoreB): 
    differential = abs(scoreA - scoreB)
    if differential <= 5: 
        return 5    
    elif differential <= 10:
        return 4    
    elif differential <= 15: 
        return 3
    elif differential <= 20:
        return 2
    else: 
        return 1

def get_high_scoring_rating(scoreA, scoreB):
    league_avg_pts = float(LEAGUE_AVG['PTS'])
    difference = league_avg_pts - ((scoreA + scoreB) / 2)
    if difference >= 10: #10+      AVG: 106 or less
        return 1
    elif difference >= 5: #5+       AVG: 110 or less
        return 2
    elif difference >= -3: #0+        AVG: 119 or less
        return 3
    elif difference >= -10:          #AVG: 125 or less
        return 4
    else:                          #AVG: Over 125
        return 5
    
def get_fouls_in_game_rating(fouls):
    league_avg_fouls = float(LEAGUE_AVG['PF'])
    difference = league_avg_fouls - (fouls / 2)
    if difference >= 10:
        return 5
    elif difference >= 5: 
        return 4
    elif difference >= 0: 
        return 3
    elif difference >= -5:
        return 2
    else:
        return 1
    
def get_fta_in_game_rating(ftas):
    league_avg_fts = float(LEAGUE_AVG['FTA'])
    difference = league_avg_fts - (ftas / 2)
    if difference >= 10:
        return 5
    elif difference >= 5: 
        return 4
    elif difference >= 0: 
        return 3
    elif difference >= -5:
        return 2
    else:
        return 1
    
# def get_slow_game_rating(ftas, pfs):
#     fta_rating = get_fta_in_game_rating(ftas)
#     fouls_rating = get_fouls_in_game_rating(pfs)
#     print('FTA RATING: ', fta_rating)
#     print('FOULS RATING: ', fouls_rating)
#     return int((fta_rating + fouls_rating) / 2)
     
def get_star_power_rating(players):
    stars = 0
    for player in players: 
        if player in STARS:
            stars += 1

    if stars > 3:
        return 5
    elif stars == 3:
        return 4
    elif stars == 2:
        return 3
    elif stars == 1:
        return 2
    else:  
        return 1
    


# Returns game rating from a boxscore based on different metrics  
def get_game_rating_by_boxscore(boxscore): 
    scores = []
    fouls = 0
    ftas = 0
    
    players = []
    for team_name in boxscore.keys():
        scores.append(int(boxscore[team_name]['team']['PTS']))
        fouls += int(boxscore[team_name]['team']['PF'])
        ftas += int(boxscore[team_name]['team']['FT'].partition('-')[-1])

        for player in boxscore[team_name].keys():
            if boxscore[team_name][player]['MIN'].startswith('DNP') or not boxscore[team_name][player]['MIN']:
                continue
            print(player)
            player_name = re.search('(.*?). (.*?)#', player)
            if not player_name:
                player_name = re.search('(.*?). (.*?) ', player)
            if not player_name:
                continue
            players.append(f'{player_name.group(1)}. {player_name.group(2)}')

    ratings = {
        'competitive': get_score_differential_rating(scores[0], scores[1]),
        'high_scoring': get_high_scoring_rating(scores[0], scores[1]),
        'less_ftas': get_fta_in_game_rating(ftas),
        'less_fouls': get_fouls_in_game_rating(fouls),
        'star_power': get_star_power_rating(players),    
    }

    # PRINTING RATINGS
    for k, v in ratings.items():
        print(f'{k}: {v}')
    overall_rating = 0
    for r in ratings.values():
        overall_rating += r

    overall_rating /= len(ratings)
    print('Overall Rating', overall_rating)
    ratings['overall_rating'] = overall_rating

    return ratings
