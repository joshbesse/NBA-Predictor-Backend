import pandas as pd 

def rename_columns(df):
    # rename columns for consistent naming
    df.rename(columns={
        'id': 'TEAM_ID',
        'full_name': 'TEAM_NAME',
        'Game_ID': 'GAME_ID',
        'TEAM_ID': 'team_id',
        'GAME_ID': 'game_id'
    }, inplace=True)

    # drop redundant columns
    df.drop(columns=['Team_ID', 'team_id', 'game_id'], inplace=True)

def add_features(df):
    df['FTA_RATE'] = (df['FTA'] / df['FGA']).round(3)
    df['FG3A_RATE'] = (df['FG3A'] / df['FGA']).round(3) 

def fix_types(df):
    # convert data types
    df['GAME_ID'] = df['GAME_ID'].astype(int)
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])

    # map WL
    df['WL'] = df['WL'].apply(lambda x: 1 if x == 'W' else 0)

def structure(df):
    # print num rows and cols
    rows, columns = df.shape

    print(f"DataFrame has {rows} rows.")
    print(f"DataFrame has {columns} columns.")

def missing_values(df):
    # print if any missing values
    if df.isna().values.any():
        print("DataFrame contains missing values.")
    else:
        print("DataFrame does not contain missing values.")

def duplicate_values(df):
    # print if any duplicate observations 
    if df.duplicated().any():
        print("DataFrame contains duplicate observations.")
    else:
        print("DataFrame does not contain duplicate observations.")

# load collected data (from data_collection.py)
df = pd.read_pickle('./Datasets/merged.pkl')

# clean up column names and redundant columns
rename_columns(df)

# add free throw rate and 3 point attempt rate columns 
add_features(df)

# fix data types
fix_types(df)

# check df structure
structure(df)

# check missing values
missing_values(df)

# check duplicate observations
duplicate_values(df)

# save checked data
print(df)
print(df.info())
df.to_pickle('./Datasets/checked.pkl')
print("Saved checked data.")
