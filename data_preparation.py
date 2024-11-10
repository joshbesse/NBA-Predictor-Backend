import pandas as pd 

def merge_home_away(season_df):
    # calculate if home or away team
    season_df['home_or_away'] = season_df['MATCHUP'].apply(lambda x: 'Home' if 'vs.' in x else 'Away')

    # create separate df for home teams and away teams 
    home_df = season_df[season_df['home_or_away'] == 'Home'].copy()
    away_df = season_df[season_df['home_or_away'] == 'Away'].copy()

    home_df = home_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP'])
    away_df = away_df.drop(columns=['Team_ID', 'home_or_away', 'MATCHUP', 'WL'])

    # merge home and away df so that 1 row represents 1 game with stats on both teams 
    merged_df = pd.merge(home_df, away_df, on=['Game_ID', 'Game_Date'], suffixes=('_home', '_away'))

    merged_df = merged_df.rename(columns={'WL': 'WL_home'})

    return merged_df

# load featured engineered data
df = pd.read_pickle('./feature.pkl')



# one row for every game for every team -> merge rows from same game for both teams into one row (row contains information on both teams for one game) 
#df = merge_home_away(df)