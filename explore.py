import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def summary_statistics(df):
    pd.set_option('display.max_columns', None)
    # numerical columns interested in
    sum_stats = df[['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'EFG_PCT', 'TM_TOV_PCT', 'AST_TOV', 'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'FTA_RATE', 'FG3A_RATE']]
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

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['EFG_PCT'], bins=20, color='indianred', edgecolor='black')
    axes[0].set_xlabel('EFG_PCT')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of EFG_PCT')
    axes[1].boxplot(df['EFG_PCT'], vert=True, patch_artist=True, boxprops={'facecolor': 'indianred'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('EFG_PCT Boxplot')
    axes[1].set_xlabel('EFG_PCT')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['TM_TOV_PCT'], bins=20, color='limegreen', edgecolor='black')
    axes[0].set_xlabel('TOV_PCT')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of TOV_PCT')
    axes[1].boxplot(df['TM_TOV_PCT'], vert=True, patch_artist=True, boxprops={'facecolor': 'limegreen'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('TOV_PCT Boxplot')
    axes[1].set_xlabel('TOV_PCT')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['AST_TOV'], bins=20, color='orange', edgecolor='black')
    axes[0].set_xlabel('AST_TOV')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of AST_TOV')
    axes[1].boxplot(df['AST_TOV'], vert=True, patch_artist=True, boxprops={'facecolor': 'orange'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('AST_TOV Boxplot')
    axes[1].set_xlabel('AST_TOV')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['OREB_PCT'], bins=20, color='mediumpurple', edgecolor='black')
    axes[0].set_xlabel('OREB_PCT')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of OREB_PCT')
    axes[1].boxplot(df['OREB_PCT'], vert=True, patch_artist=True, boxprops={'facecolor': 'mediumpurple'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('OREB_PCT Boxplot')
    axes[1].set_xlabel('OREB_PCT')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['DREB_PCT'], bins=20, color='indianred', edgecolor='black')
    axes[0].set_xlabel('DREB_PCT')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of DREB_PCT')
    axes[1].boxplot(df['DREB_PCT'], vert=True, patch_artist=True, boxprops={'facecolor': 'indianred'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('DREB_PCT Boxplot')
    axes[1].set_xlabel('DREB_PCT')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['FTA_RATE'], bins=20, color='limegreen', edgecolor='black')
    axes[0].set_xlabel('FTA_RATE')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of FTA_RATE')
    axes[1].boxplot(df['FTA_RATE'], vert=True, patch_artist=True, boxprops={'facecolor': 'limegreen'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('FTA_RATE Boxplot')
    axes[1].set_xlabel('FTA_RATE')
    plt.tight_layout()
    plt.show()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axes[0].hist(df['FG3A_RATE'], bins=20, color='orange', edgecolor='black')
    axes[0].set_xlabel('FG3A_RATE')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of FG3A_RATE')
    axes[1].boxplot(df['FG3A_RATE'], vert=True, patch_artist=True, boxprops={'facecolor': 'orange'}, medianprops={'color': 'whitesmoke'})
    axes[1].set_title('FG3A_RATE Boxplot')
    axes[1].set_xlabel('FG3A_RATE')
    plt.tight_layout()
    plt.show()

def team_summary_statistics(df):
    team_sum_stats = df.groupby('TEAM_NAME').agg(
        PTS_AVG=('PTS', 'mean'),
        FGA_AVG=('FGA', 'mean'),
        FG_PCT_AVG=('FG_PCT', 'mean'),
        FG3A_AVG=('FG3A', 'mean'),
        FG3_PCT_AVG=('FG3_PCT', 'mean'),
        FTA_AVG=('FTA', 'mean'),
        FT_PCT_AVG=('FT_PCT', 'mean'),
        OREB_AVG=('OREB', 'mean'),
        DREB_AVG=('DREB', 'mean'),
        REB_AVG=('REB', 'mean'),
        AST_AVG=('AST', 'mean'),
        STL_AVG=('STL', 'mean'),
        BLK_AVG=('BLK', 'mean'),
        TOV_AVG=('TOV', 'mean'),
        OFF_RATING_AVG=('OFF_RATING', 'mean'),
        DEF_RATING_AVG=('DEF_RATING', 'mean'),
        NET_RATING_AVG=('NET_RATING', 'mean'),
        EFG_PCT_AVG=('EFG_PCT', 'mean'),
        TOV_PCT_AVG=('TM_TOV_PCT', 'mean'),
        AST_TOV_AVG=('AST_TOV', 'mean'),
        OREB_PCT_AVG=('OREB_PCT', 'mean'),
        DREB_PCT_AVG=('DREB_PCT', 'mean'),
        REB_PCT_AVG=('REB_PCT', 'mean'),
        FTA_RATE_AVG=('FTA_RATE', 'mean'),
        FG3A_RATE=('FG3A_RATE', 'mean')
    )
    team_records = df[['TEAM_NAME', 'W', 'L']].groupby('TEAM_NAME').head(1)
    team_sum_stats = pd.merge(team_records, team_sum_stats, on="TEAM_NAME").sort_values('W', ascending=False).reset_index(drop=True)

    return team_sum_stats

def scatter(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['PTS_AVG'], team_stats['W'], color='blue', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['PTS_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Points (PTS_AVG)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Points')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['NET_RATING_AVG'], team_stats['W'], color='red', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['NET_RATING_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Net Rating (NET_RATING_AVG)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Net Rating')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['EFG_PCT_AVG'], team_stats['W'], color='orange', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['EFG_PCT_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Effective Field Goal Percentage (EFG_PCT_AVG)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Effective Field Goal Percentage')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['TOV_PCT_AVG'], team_stats['W'], color='purple', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['TOV_PCT_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Turnover Percentage (TOV_PCT_AVG)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Turnover Percentage')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['AST_TOV_AVG'], team_stats['W'], color='yellow', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['AST_TOV_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Assist to Turnover Ratio (AST_TOV)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Assist to Turnover Ratio')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['OREB_PCT_AVG'], team_stats['W'], color='green', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['OREB_PCT_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Offensive Rebound Percentage (OREB_PCT)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Offensive Rebound Percentage')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['DREB_PCT_AVG'], team_stats['W'], color='blue', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['DREB_PCT_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Defensive Rebound Percentage (DREB_PCT)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Defensive Rebound Percentage')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['FTA_RATE_AVG'], team_stats['W'], color='red', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['FTA_RATE_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average Free Throw Rate (FTA_RATE_AVG)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average Free Throw Rate')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['FG3_PCT_AVG'], team_stats['W'], color='orange', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['FG3_PCT_AVG'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average 3 Point Field Goal Percentage (FG3_PCT_AVG)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average 3 Point Field Goal Percentage')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(team_stats['FG3A_RATE'], team_stats['W'], color='purple', alpha=0.7)
    for i, team in enumerate(team_stats['TEAM_NAME']):
        plt.text(team_stats['FG3A_RATE'][i], team_stats['W'][i], team, fontsize=7, ha='left', va='bottom')
    ax.set_xlabel('Average 3 Point Field Goal Attempt Rate (FG3A_RATE)')
    ax.set_ylabel('Wins (W)')
    ax.set_title('Wins vs. Average 3 Point Field Goal Attempt Rate')
    table_data = team_stats[['TEAM_NAME', 'W', 'L']].values.tolist()
    column_labels = ['Team', 'W', 'L']
    table = plt.table(cellText=table_data, colLabels=column_labels, colWidths=[0.3, 0.1, 0.1], cellLoc='center', bbox=[1.07, -0.05, 0.4, 1.1])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.subplots_adjust(right=0.7)
    plt.show()

def corr_matrix(df):
    corr_df = df[['WL', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'EFG_PCT', 'TM_TOV_PCT', 'AST_TOV', 'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'FTA_RATE', 'FG3A_RATE']]
    corr_matrix = corr_df.corr()
    plt.figure(figsize=(9, 7.5))
    sns.heatmap(corr_matrix, cmap='coolwarm')
    plt.title('Correlation Matrix', fontsize=16)
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.show()

# load checked data (from data_cleaning.py)
#df = pd.read_pickle('./Datasets/checked.pkl')
df = pd.read_pickle('./Datasets/test_checked.pkl')

# summary statistics
summary_statistics(df)

# histograms and boxplots of important features
distributions(df)

# team summary statistics
team_stats = team_summary_statistics(df)
pd.set_option('display.max_columns', None)
print(team_stats)

# team scatter plots
scatter(team_stats)

# correlation matrix
corr_matrix(df)
