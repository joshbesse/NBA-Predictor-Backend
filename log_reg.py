import pandas as pd 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns 

# load data
df = pd.read_pickle('./final.pkl')

# feature scaling
features = df.drop(columns=['Target'])
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
scaled_df = pd.DataFrame(scaled_features, columns=features.columns)
scaled_df['Target'] = df['Target']

# check correlation
corr_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', cbar=True)
plt.title("Feature Correlation Heatmap")
plt.show()
# rolling averages like ppg, fg_pct, off_rating, etc. are highly correlated with itself (ppg_home and fg_pct home) and with other team (ppg_away, reb_home)
# going to use ridge logistic regression (l2 regularization)

# split the data into training, validation, and testing sets
# need validation set for tuning regularization parameter
# need to split chronologically to avoid leaking future information into past predictions 
train_split = int(len(scaled_df) * 0.70)
val_split = int(len(scaled_df) * 0.85)

train_df = scaled_df[:train_split]
val_df = scaled_df[train_split:val_split]
test_df = scaled_df[val_split:]

X_train, y_train = train_df.drop(columns=['Target']), train_df['Target']
X_val, y_val = val_df.drop(columns=['Target']), val_df['Target']
X_test, y_test = test_df.drop(columns=['Target']), test_df['Target']