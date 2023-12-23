import requests
import bs4

# Returns stats for each player in both teams as well as team stats 
def get_boxscore_by_link(link):
    # Sets up userAgent and sends a request to 
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    data = requests.get(link, 
                        headers={'User-Agent': user_agent})
    data.raise_for_status()

    # Team Stats would be extracted from the boxscore html file and stored as an object
    team_stats = {}

    nba_soup = bs4.BeautifulSoup(data.text, 'html.parser')
    # There's two box scores for two teams
    boxscores = nba_soup.select('div.Boxscore div.ResponsiveTable')
    boxscores_title = nba_soup.select('div.Boxscore__Title')
        
    for boxscore_idx in range(len(boxscores)): 
        team_name = boxscores_title[boxscore_idx].text
        team_boxscore = boxscores[boxscore_idx]
        # Select the two tables in the box score 
        # (tables are divided into two parts: player names and statline)
        tables = team_boxscore.select('tbody.Table__TBODY')
        team_stats[team_name] = {}
        # The first row of stats table contain the type of stats each column has (eg: PTS, REB, AST)
        stats_type_table = tables[1].select_one(f'tr[data-idx="0"]').select('td')
        # Going through player names
        for row in tables[0].select('tr'):
            # Skip empty rows
            if ('starters' in row.text.lower() or 'bench' in row.text.lower() or not row.text):
                continue
            # Finding player stats from the other table by matching the data-idx values in both tables
            player_stats_table = tables[1].select_one(f'tr[data-idx="{row.get("data-idx")}"]').select('td')
            team_stats[team_name][row.text] = {}
            player = team_stats[team_name][row.text] 
            for idx in range(len(player_stats_table)):
                player[stats_type_table[idx].text] = player_stats_table[idx].text
    
    return team_stats

    