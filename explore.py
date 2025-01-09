import pandas as pd
import matplotlib.pyplot as plt

def summary_statistics(df):
    pd.set_option('display.max_columns', None)
    # numerical columns interested in
    sum_stats = df[['FG_PCT', 'FG3_PCT', 'FT_PCT','REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'PACE', 'EFF_FG_PCT', 'TS_PCT']]
    print(sum_stats.describe())

def distributions(df):
    # distributions of important features
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['PTS'], bins=20, color='indianred', edgecolor='black')
    axes[0].set_xlabel('PTS')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of PTS')
    axes[1].boxplot(df['PTS'], vert=True, patch_artist=True, boxprops={'facecolor': 'indianred'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('PTS Boxplot')
    axes[1].set_xlabel('PTS')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['FG_PCT'], bins=20, color='limegreen', edgecolor='black')
    axes[0].set_xlabel('FG_PCT')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of FG_PCT')
    axes[1].boxplot(df['FG_PCT'], vert=True, patch_artist=True, boxprops={'facecolor': 'limegreen'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('FG_PCT Boxplot')
    axes[1].set_xlabel('FG_PCT')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['FG3_PCT'], bins=20, color='orange', edgecolor='black')
    axes[0].set_xlabel('FG3_PCT')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of FG3_PCT')
    axes[1].boxplot(df['FG3_PCT'], vert=True, patch_artist=True, boxprops={'facecolor': 'orange'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('FG3_PCT Boxplot')
    axes[1].set_xlabel('FG3_PCT')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['NET_RATING'], bins=20, color='mediumpurple', edgecolor='black')
    axes[0].set_xlabel('NET_RATING')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of NET_RATING')
    axes[1].boxplot(df['NET_RATING'], vert=True, patch_artist=True, boxprops={'facecolor': 'mediumpurple'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('NET_RATING Boxplot')
    axes[1].set_xlabel('NET_RATING')
    plt.tight_layout()
    plt.show()

# load checked data (from data_cleaning.py)
df = pd.read_pickle('./Datasets/checked.pkl')

# summary statistics
summary_statistics(df)

print(df['WL'].value_counts())

# histograms of important features
distributions(df)

