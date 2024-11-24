import pandas as pd 

def missing_values(df):
    print(df.info())
    print(df.isna().sum())
    
def merge_home_away(season_df):
    # calculate if home or away team
    season_df['home_or_away'] = season_df['MATCHUP'].apply(lambda x: 'Home' if 'vs.' in x else 'Away')

    # create separate df for home teams and away teams 
    home_df = season_df[season_df['home_or_away'] == 'Home'].copy()
    away_df = season_df[season_df['home_or_away'] == 'Away'].copy()

    home_df = home_df.drop(columns=['home_or_away', 'MATCHUP'])
    away_df = away_df.drop(columns=['home_or_away', 'MATCHUP', 'WL'])

    # merge home and away df so that 1 row represents 1 game with stats on both teams 
    merged_df = pd.merge(home_df, away_df, on=['Game_ID', 'Game_Date'], suffixes=('_home', '_away'))

    merged_df = merged_df.rename(columns={'WL': 'WL_home'})

    return merged_df

def calculate_comparative_features(df):
    df['PPG_DIFF'] = df['PPG_5GM_AVG_home'] - df['PPG_5GM_AVG_away']
    df['FG_PCT_DIFF'] = df['FG_PCT_5GM_AVG_home'] - df['FG_PCT_5GM_AVG_away']
    df['FG3_PCT_DIFF'] = df['FG3_PCT_5GM_AVG_home'] - df['FG3_PCT_5GM_AVG_away']
    df['REB_DIFF'] = df['REB_5GM_AVG_home'] - df['REB_5GM_AVG_away']
    df['AST_DIFF'] = df['AST_5GM_AVG_home'] - df['AST_5GM_AVG_away']
    df['TOV_DIFF'] = df['TOV_5GM_AVG_home'] - df['TOV_5GM_AVG_away']
    df['Off_Rating_DIFF'] = df['Off_Rating_5GM_AVG_home'] - df['Off_Rating_5GM_AVG_away']
    df['Def_Rating_DIFF'] = df['Def_Rating_5GM_AVG_home'] - df['Def_Rating_5GM_AVG_away']
    df['Net_Rating_DIFF'] = df['Net_Rating_5GM_AVG_home'] - df['Net_Rating_5GM_AVG_away']
    df['Pace_DIFF'] = df['Pace_5GM_AVG_home'] - df['Pace_5GM_AVG_away']
    df['Eff_FG_DIFF'] = df['Eff_FG_PCT_5GM_AVG_home'] - df['Eff_FG_PCT_5GM_AVG_away']
    df['TS_DIFF'] = df['TS_5GM_AVG_home'] - df['TS_5GM_AVG_away']
    df['Win_PCT_DIFF'] = df['5GM_Win_PCT_home'] - df['5GM_Win_PCT_away']

    return df 

def drop_features(df):
    df = df.drop(columns=['Away_Win_PCT_home', 'Home_Win_PCT_away', 'Home_Court_Advantage_away', 'Team_Name_home', 'Team_Name_away', 'Team_ID_home', 'Team_ID_away', 'Game_ID', 'Game_Date', 'WL_home'])

    return df 

def pipeline(df):
    # check missing values
    missing_values(df)

    # one row for every game for every team -> merge rows from same game for both teams into one row (row contains information on both teams for one game) 
    df = merge_home_away(df)

    # calculate comparative features
    df = calculate_comparative_features(df)

    # encode target variable -> 1 if home team win and 0 if away team win
    df['Target'] = df['WL_home'].map({'W': 1, 'L': 0})

    # drop redundant and game identification features
    df = drop_features(df)

    # check missing values
    missing_values(df)

    return df

# load featured engineered data
df = pd.read_pickle('./feature.pkl')

# apply preparation pipeline
df = pipeline(df)

# save prepared data
print(df)
print(df.columns)
df.to_pickle('./final.pkl')
print("Saved prepared data.")