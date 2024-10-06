import requests

def get_games_by_date(date):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    data = requests.get(f'https://site.api.espn.com/apis/v2/scoreboard/header?sport=basketball&league=nba&dates={date}', 
                    headers={'User-Agent': user_agent})

    data.raise_for_status()

    # Get all the events(games) on the day: 
    if 'events' not in data.json()['sports'][0]['leagues'][0]:
        return None

    events = data.json()['sports'][0]['leagues'][0]['events']

    return events

