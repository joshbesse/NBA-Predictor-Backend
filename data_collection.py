from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog, boxscoreadvancedv2
import pandas as pd 
import time 

def fetch_team_data():
    teams_list = teams.get_teams()
    teams_df = pd.DataFrame(teams_list)[['id', 'full_name']]
    
    return teams_df 

def fetch_season_history(teams):
    season_df = pd.DataFrame()
    for team_id in teams:
        season_history = teamgamelog.TeamGameLog(season='2023-24', season_type_all_star='Regular Season', team_id=team_id).get_data_frames()[0]
        season_df = pd.concat([season_df, season_history])
        # add delay to requests to nba_api otherwise error 
        time.sleep(10)

    return season_df

def merge_home_away(season_df):
    season_df['home_or_away'] = season_df['MATCHUP'].apply(lambda x: 'Home' if 'vs.' in x else 'Away')
    home_df = season_df[season_df['home_or_away'] == 'Home'].copy()
    away_df = season_df[season_df['home_or_away'] == 'Away'].copy()

    home_df = home_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])
    away_df = away_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])

    merged_df = pd.merge(home_df, away_df, on=['Game_ID', 'GAME_DATE'], suffixes=('_home', '_away'))

    return merged_df

# fetch team id and name for each team
teams_df = fetch_team_data()

# fetch 2023-24 regular season game history for each team
all_teams = teams_df['id']
season_df = fetch_season_history(all_teams)

# merge teams_df and season_df (adding team full name to season history)
df = pd.merge(teams_df, season_df, left_on='id', right_on='Team_ID')

# one row for every game for every team -> merge rows from same game for both teams into one row (row contains information on both teams for one game) 
#df = merge_home_away(df)
#print(df)

# ------------------------------------------------------------------------------------------------------------------------------------

# one row for every game for every team -> merge rows from same game for both teams into one row (row contains information on both teams for one game) 
season_df = pd.read_pickle('./season.pkl')
season_df['home_or_away'] = season_df['MATCHUP'].apply(lambda x: 'Home' if 'vs.' in x else 'Away')
home_df = season_df[season_df['home_or_away'] == 'Home'].copy()
away_df = season_df[season_df['home_or_away'] == 'Away'].copy()

home_df = home_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])
away_df = away_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])

merged_df = pd.merge(home_df, away_df, on=['Game_ID', 'GAME_DATE'], suffixes=('_home', '_away'))


# get individual player advanced statistics -> need to aggregate -> advanced team statistics & team recent performance  
#boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id='0022301188')
#advanced = boxscore.get_data_frames()[0]
#print(advanced[['OFF_RATING', 'DEF_RATING', 'NET_RATING']])

# key player information -> manually collect 