import pandas as pd 

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
    # drop unwanted features
    df = df.drop(columns=['id', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 
                        'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                        'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS',
                        'GAME_ID', 'TEAM_ID', 'team_name', 'Win'])
    
    # rename columns
    columns = ['Team_Name', 'Team_ID', 'Game_ID', 'Game_Date', 'MATCHUP', 'WL', 'Rest_Days',
            'Home_Court_Advantage', 'Home_Win_PCT', 'Away_Win_PCT', 'PPG_5GM_AVG',
            'FG_PCT_5GM_AVG', 'FG3_PCT_5GM_AVG', 'REB_5GM_AVG', 'AST_5GM_AVG',
            'TOV_5GM_AVG', 'Offensive_Rating', 'Defensive_Rating', 'Net_Rating',
            'Pace', 'Effective_FG_PCT', 'True_Shooting_PCT', 'All_Star_Players',
            'All_NBA_Players', 'Win/Loss_Streak', '5GM_Win_PCT']
    df.columns = columns

    return df 

# load collected data
df = pd.read_pickle('./data.pkl')

# calculate new features
df = calculate_game_context(df)
df = calculate_basic_team_stats(df)
df = calculate_key_player_stats(df)
df = calculate_recent_performance(df)

# delete unwanted features and rename columns 
df = drop_features(df)
print(df)
df.to_pickle('./feature.pkl')
print("Saved feature engineered data.")