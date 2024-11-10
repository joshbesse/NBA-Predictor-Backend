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
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    df = df.sort_values(by=['id', 'GAME_DATE'])
    # calculate rest days 
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

def calculate_basic_team_stats(df):
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    df = df.sort_values(by=['id', 'GAME_DATE'])

    # calculate points per game rolling average
    df['PPG_5GM_AVG'] = df.groupby('id')['PTS'].transform(lambda x: x.shift().rolling(5).mean())

    # calculate field goal percentage rolling average 
    df['FG_PCT_5GM_AVG'] = df.groupby('id')['FG_PCT'].transform(lambda x: x.shift().rolling(5).mean())

    # calculate 3 point field goal percentage rolling average
    df['FG3_PCT_5GM_AVG'] = df.groupby('id')['FG3_PCT'].transform(lambda x: x.shift().rolling(5).mean())

    # calculate rebound rolling average
    df['REB_5GM_AVG'] = df.groupby('id')['REB'].transform(lambda x: x.shift().rolling(5).mean())
    
    # calculate assist rolling average
    df['AST_5GM_AVG'] = df.groupby('id')['AST'].transform(lambda x: x.shift().rolling(5).mean())

    # calculate turnover rolling average
    df['TOV_5GM_AVG'] = df.groupby('id')['TOV'].transform(lambda x: x.shift().rolling(5).mean())

    return df 

def convert_min_to_decimal(min_str):
    if pd.isna(min_str):
        return float('nan')
    else:
        minutes, seconds = min_str.split(':')
        new_min_format = f"{int(float(minutes))}.{seconds}"
        return float(new_min_format) 

def calculate_advance_team_stats(df):
    # df to store team advanced statistics for every team for every game 
    team_adv_stats = pd.DataFrame()

    # get list of all games for the regular season
    all_games = df['Game_ID'].unique()

    for game in all_games:
        # get individual player advanced statistics -> need to aggregate and calculate team advanced statistics
        adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id=game)
        adv_stats_df = adv_boxscore.get_data_frames()[0]

        # convert MIN format from MM:SS string to MM.SS float
        adv_stats_df['MIN'] = adv_stats_df['MIN'].apply(convert_min_to_decimal)
        adv_stats_df = adv_stats_df[adv_stats_df['MIN'] > 0]

        # calculate team advanced statistics for both teams 
        current_teams_adv_stats_df = adv_stats_df.groupby(['GAME_ID', 'TEAM_ID']).apply(
            lambda x: pd.Series({
                'Offensive_Rating': (x['OFF_RATING'] * x['MIN']).sum() / x['MIN'].sum(),
                'Defensive_Rating': (x['DEF_RATING'] * x['MIN']).sum() / x['MIN'].sum(),
                'Net_Rating': (x['NET_RATING'] * x['MIN']).sum() / x['MIN'].sum(),
                'Pace': (x['PACE'] * x['MIN']).sum() / x['MIN'].sum(),
                'Effective_FG_PCT': (x['EFG_PCT'] * x['MIN']).sum() / x['MIN'].sum(),
                'True_Shooting_PCT': (x['TS_PCT'] * x['MIN']).sum() / x['MIN'].sum()
            })
        ).reset_index()

        team_adv_stats = pd.concat([team_adv_stats, current_teams_adv_stats_df])
        time.sleep(10)

    df = df.merge(team_adv_stats, left_on=['Game_ID', 'Team_ID'], right_on=['GAME_ID', 'TEAM_ID'])

    return df
    
def calculate_key_player_stats(df):
    # manually collected stats on number of all star and all nba players
    key_players_df = pd.DataFrame({
        'team_name': ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers', 'Toronto Raptors',
                    'Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers', 'Milwaukee Bucks',
                    'Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic', 'Washington Wizards',
                    'Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 'Portland Trail Blazers', 'Utah Jazz',
                    'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns', 'Sacramento Kings',
                    'Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans', 'San Antonio Spurs'],
        'all_star_players': [2, 0, 2, 3, 1,
                            0, 1, 0, 1, 2,
                            1, 0, 1, 1, 0,
                            1, 2, 1, 0, 0,
                            1, 1, 2, 2, 0,
                            1, 0, 0, 0, 0],
        'all_nba_players': [1, 0, 1, 0, 0,
                            0, 0, 0, 1, 1,
                            0, 0, 0, 0, 0,
                            1, 1, 1, 0, 0,
                            1, 1, 2, 2, 1,
                            1, 0, 0, 0, 0]
    })

    df = df.merge(key_players_df, left_on='full_name', right_on='team_name')
    
    return df 

def calculate_recent_performance(df):
    # calculate win/loss streaks
    streaks = []
    current_streak = 0
    last_result = None

    for result in df['WL']:
        if result == last_result:
            if result == 'W':
                current_streak += 1
            else:
                current_streak -= 1
        else:
            if result == 'W':
                current_streak = 1
                last_result = result
            else:
                current_streak = -1
                last_result = result
        streaks.append(current_streak)

    df['Streak'] = streaks

    # calculate last 5 game win percentage
    df = df.sort_values(by=['Team_ID', 'GAME_DATE'])
    df['Win'] = df['WL'].map({'W': 1, 'L': 0})
    df['5GM_Win_Pct'] = df.groupby('Team_ID')['Win'].rolling(window=5, min_periods=1).mean().values

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

# calculate features
#df = calculate_game_context(df)
#df = calculate_basic_team_stats(df)
#df = calculate_advance_team_stats(df)
#df = calculate_key_player_stats(df)
#df = calculate_recent_performance(df)

# delete features
#df = drop_features(df)
#df.to_pickle('./temp.pkl')

# one row for every game for every team -> merge rows from same game for both teams into one row (row contains information on both teams for one game) 
#df = merge_home_away(df)


# ------------------------------------------------------------------------------------------------------------------------------------
df = pd.read_pickle('./temp.pkl')
df = calculate_key_player_stats(df)
print(df)
print(df.columns)
df = calculate_recent_performance(df)
print(df)
print(df.columns)





# key player information -> manually collect 