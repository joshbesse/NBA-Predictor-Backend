import pandas as pd

# load finalized data
df = pd.read_pickle('./Datasets/final.pkl')

# sort data by date
df = df.sort_values('GAME_DATE').reset_index(drop=True)
