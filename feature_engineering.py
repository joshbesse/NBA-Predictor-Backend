import pandas as pd 

def calculate_game_context(df):
    # sort by team and game date 
    df = df.sort_values(['TEAM_NAME', 'GAME_DATE']).reset_index(drop=True)

    # rest days in between games
    df['REST_DAYS'] = df.groupby('TEAM_NAME')['GAME_DATE'].diff().dt.days
    df['REST_DAYS'] = df['REST_DAYS'].fillna(0)   

    # home court advantage
    df['HOME_ADVANTAGE'] = df['MATCHUP'].apply(lambda x: 1 if 'vs.' in x else 0)

    # winning percentage rolling average and season to date average
    df['WIN_PCT'] = df.groupby('TEAM_NAME')['WL'].transform(lambda x: x.shift().expanding().mean().round(3))
    df['WIN_PCT_3GM'] = df.groupby('TEAM_NAME')['WL'].transform(lambda x: x.shift().rolling(3).mean().round(3))

    return df

def calculate_basic_stats(df):
    # points rolling average and season to date average
    df['PTS_AVG'] = df.groupby('TEAM_NAME')['PTS'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['PTS_3GM_AVG'] = df.groupby('TEAM_NAME')['PTS'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # field goals made rolling average and season to date average
    df['FGM_AVG'] = df.groupby('TEAM_NAME')['FGM'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FGM_3GM_AVG'] = df.groupby('TEAM_NAME')['FGM'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # field goals attempted rolling average and season to date average
    df['FGA_AVG'] = df.groupby('TEAM_NAME')['FGA'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FGA_3GM_AVG'] = df.groupby('TEAM_NAME')['FGA'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # field goal percentage rolling average and season to date average
    df['FG_PCT_AVG'] = df.groupby('TEAM_NAME')['FG_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FG_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['FG_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # 3 point field goals made rolling average and season to date average
    df['FG3M_AVG'] = df.groupby('TEAM_NAME')['FG3M'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FG3M_3GM_AVG'] = df.groupby('TEAM_NAME')['FG3M'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # 3 point field goals attempted rolling average and season to date average
    df['FG3A_AVG'] = df.groupby('TEAM_NAME')['FG3A'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FG3A_3GM_AVG'] = df.groupby('TEAM_NAME')['FG3A'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # 3 point field goal percentage rolling average and season to date average
    df['FG3_PCT_AVG'] = df.groupby('TEAM_NAME')['FG3_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FG3_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['FG3_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # free throws made rolling average and season to date average
    df['FTM_AVG'] = df.groupby('TEAM_NAME')['FTM'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FTM_3GM_AVG'] = df.groupby('TEAM_NAME')['FTM'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # free throws attempted rolling average and season to date average
    df['FTA_AVG'] = df.groupby('TEAM_NAME')['FTA'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FTA_3GM_AVG'] = df.groupby('TEAM_NAME')['FTA'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # free throw percentage rolling average and season to date average
    df['FT_PCT_AVG'] = df.groupby('TEAM_NAME')['FT_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FT_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['FT_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # offensive rebounds rolling average and season to date average
    df['OREB_AVG'] = df.groupby('TEAM_NAME')['OREB'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['OREB_3GM_AVG'] = df.groupby('TEAM_NAME')['OREB'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # defensive rebounds rolling average and season to date average
    df['DREB_AVG'] = df.groupby('TEAM_NAME')['DREB'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['DREB_3GM_AVG'] = df.groupby('TEAM_NAME')['DREB'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # rebounds rolling average and season to date average
    df['REB_AVG'] = df.groupby('TEAM_NAME')['REB'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['REB_3GM_AVG'] = df.groupby('TEAM_NAME')['REB'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # assists rolling average and season to date average
    df['AST_AVG'] = df.groupby('TEAM_NAME')['AST'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['AST_3GM_AVG'] = df.groupby('TEAM_NAME')['AST'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # steals rolling average and season to date average
    df['STL_AVG'] = df.groupby('TEAM_NAME')['STL'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['STL_3GM_AVG'] = df.groupby('TEAM_NAME')['STL'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # blocks rolling average and season to date average
    df['BLK_AVG'] = df.groupby('TEAM_NAME')['BLK'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['BLK_3GM_AVG'] = df.groupby('TEAM_NAME')['BLK'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # turnovers rolling average and season to date average
    df['TOV_AVG'] = df.groupby('TEAM_NAME')['TOV'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['TOV_3GM_AVG'] = df.groupby('TEAM_NAME')['TOV'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # personal fouls rolling average and season to date average
    df['PF_AVG'] = df.groupby('TEAM_NAME')['PF'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['PF_3GM_AVG'] = df.groupby('TEAM_NAME')['PF'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    return df

def calculate_advanced_stats(df):
    # offensive rating rolling average and season to date average
    df['OFF_RATING_AVG'] = df.groupby('TEAM_NAME')['OFF_RATING'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['OFF_RATING_3GM_AVG'] = df.groupby('TEAM_NAME')['OFF_RATING'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # defensive rating rolling average and season to date average
    df['DEF_RATING_AVG'] = df.groupby('TEAM_NAME')['DEF_RATING'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['DEF_RATING_3GM_AVG'] = df.groupby('TEAM_NAME')['DEF_RATING'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # net rating rolling average and season to date average
    df['NET_RATING_AVG'] = df.groupby('TEAM_NAME')['NET_RATING'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['NET_RATING_3GM_AVG'] = df.groupby('TEAM_NAME')['NET_RATING'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # efficient field goal percentage rolling average and season to date average
    df['EFG_PCT_AVG'] = df.groupby('TEAM_NAME')['EFG_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['EFG_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['EFG_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # turnover percentage rolling average and season to date average
    df['TOV_PCT_AVG'] = df.groupby('TEAM_NAME')['TM_TOV_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['TOV_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['TM_TOV_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # assist to turnover ratio rolling average and season to date average
    df['AST_TOV_AVG'] = df.groupby('TEAM_NAME')['AST_TOV'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['AST_TOV_3GM_AVG'] = df.groupby('TEAM_NAME')['AST_TOV'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # offensive rebound percentage rolling average and season to date average
    df['OREB_PCT_AVG'] = df.groupby('TEAM_NAME')['OREB_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['OREB_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['OREB_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # defensive rebound percentage rolling average and season to date average
    df['DREB_PCT_AVG'] = df.groupby('TEAM_NAME')['DREB_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['DREB_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['DREB_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # rebound percentage rolling average and season to date average
    df['REB_PCT_AVG'] = df.groupby('TEAM_NAME')['REB_PCT'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['REB_PCT_3GM_AVG'] = df.groupby('TEAM_NAME')['REB_PCT'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # free throws attempted rate rolling average and season to date average
    df['FTA_RATE_AVG'] = df.groupby('TEAM_NAME')['FTA_RATE'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FTA_RATE_3GM_AVG'] = df.groupby('TEAM_NAME')['FTA_RATE'].transform(lambda x: x.shift().rolling(3).mean().round(2))

    # 3 point field goal attempted rate rolling average and season to date average
    df['FG3A_RATE_AVG'] = df.groupby('TEAM_NAME')['FG3A_RATE'].transform(lambda x: x.shift().expanding().mean().round(2))
    df['FG3A_RATE_3GM_AVG'] = df.groupby('TEAM_NAME')['FG3A_RATE'].transform(lambda x: x.shift().rolling(3).mean().round(2))

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
        'ALL_STAR_PLAYERS': [2, 0, 2, 3, 1,
                            0, 1, 0, 1, 2,
                            1, 0, 1, 1, 0,
                            1, 2, 1, 0, 0,
                            1, 1, 2, 2, 0,
                            1, 0, 0, 0, 0],
        'ALL_NBA_PLAYERS': [1, 0, 1, 0, 0,
                            0, 0, 0, 1, 1,
                            0, 0, 0, 0, 0,
                            1, 1, 1, 0, 0,
                            1, 1, 2, 2, 1,
                            1, 0, 0, 0, 0]
    })

    df = pd.merge(df, key_players_df, left_on='TEAM_NAME', right_on='team_name')
    
    return df

def drop_features(df):
    # drop unwanted features
    df = df.drop(columns=['W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'EFG_PCT', 'TM_TOV_PCT', 'AST_TOV', 'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'FTA_RATE', 'FG3A_RATE'])

    return df

def merge_home_away(df):
    # calculate if team is home or away
    df['home_or_away'] = df['MATCHUP'].apply(lambda x: 'Home' if 'vs.' in x else 'Away')

    # create separate DataFrames for home and away teams
    home_df = df[df['home_or_away'] == 'Home'].copy()
    away_df = df[df['home_or_away'] == 'Away'].copy()

    home_df = home_df.drop(columns=['home_or_away', 'MATCHUP'])
    away_df = away_df.drop(columns=['home_or_away', 'MATCHUP', 'WL'])

    # merge home and away DataFrames resulting in one game per row
    merged_df = pd.merge(home_df, away_df, on=['GAME_ID', 'GAME_DATE'], suffixes=('_HOME', '_AWAY'))

    return merged_df


# load explored data
df = pd.read_pickle('./Datasets/checked.pkl')

# calculate game context
df = calculate_game_context(df)

# calculate basic stats
df = calculate_basic_stats(df)

# calculate advanced stats
df = calculate_advanced_stats(df)

# calculate key player stats
#df = calculate_key_player_stats(df)

# drop columns 
df = drop_features(df)

# transform DataFrame into one game per row
df = merge_home_away(df)