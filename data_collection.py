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

def calculate_game_context(df):
    # calculate rest days 
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    df = df.sort_values(by=['id', 'GAME_DATE'])
    df['Rest_Days'] = df.groupby('id')['GAME_DATE'].diff().dt.days
    df['Rest_Days'] = df['Rest_Days'].fillna(0)

    # calculate home court advantage
    df['Home_Court_Advantage'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)

    # calculate home win percentage and away win percentage
    df['home_games_count'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)
    df['home_wins_count'] = df.apply(lambda row: 1 if 'vs.' in row['MATCHUP'] and 'W' in row['WL'] else 0, axis=1)
    df['total_home_games'] = df['home_games_count'].cumsum()
    df['total_home_wins'] = df['home_wins_count'].cumsum()
    df['Home_Win_Pct'] = df['total_home_wins'] / df['total_home_games']

    df['away_games_count'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' not in x else 0)
    df['away_wins_count'] = df.apply(lambda row: 1 if 'vs.' not in row['MATCHUP'] and 'W' in row['WL'] else 0, axis=1)
    df['total_away_games'] = df['away_games_count'].cumsum()
    df['total_away_wins'] = df['away_wins_count'].cumsum()
    df['Away_Win_Pct'] = df['total_away_wins'] / df['total_away_games']

    df[['Home_Win_Pct', 'Away_Win_Pct']] = df[['Home_Win_Pct', 'Away_Win_Pct']].fillna(0).round(3)
    df = df.drop(columns=['home_games_count', 'home_wins_count', 'total_home_games', 'total_home_wins', 'away_games_count', 'away_wins_count', 'total_away_games', 'total_away_wins'])

    return df 

def drop_features(df):
    df = df.drop(columns=['W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'STL', 'BLK'])

    return df 

def merge_home_away(season_df):
    season_df['home_or_away'] = season_df['MATCHUP'].apply(lambda x: 'Home' if 'vs.' in x else 'Away')
    home_df = season_df[season_df['home_or_away'] == 'Home'].copy()
    away_df = season_df[season_df['home_or_away'] == 'Away'].copy()

    home_df = home_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])
    away_df = away_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])

    merged_df = pd.merge(home_df, away_df, on=['Game_ID', 'GAME_DATE'], suffixes=('_home', '_away'))

    return merged_df

# fetch team id and name for each team
#teams_df = fetch_team_data()

# fetch 2023-24 regular season game history for each team
#all_teams = teams_df['id']
#season_df = fetch_season_history(all_teams)

# merge teams_df and season_df (adding team full name to season history)
#df = pd.merge(teams_df, season_df, left_on='id', right_on='Team_ID')

# calculate and delete initial features
#df = calculate_game_context(df)
#df = drop_features(df)
#print(df)
#df.to_pickle('./temp.pkl')

# one row for every game for every team -> merge rows from same game for both teams into one row (row contains information on both teams for one game) 
#df = merge_home_away(df)


# ------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_pickle('./temp.pkl')

df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
df = df.sort_values(by=['id', 'GAME_DATE'])
# calculate ppg rolling average
#df['PPG_5GM_AVG'] = df.groupby('id')['PTS'].transform(lambda x: x.shift().rolling(5).mean())



# get individual player advanced statistics -> need to aggregate -> advanced team statistics & team recent performance  
#boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id='0022301188')
#advanced = boxscore.get_data_frames()[0]
#print(advanced[['OFF_RATING', 'DEF_RATING', 'NET_RATING']])

# key player information -> manually collect 