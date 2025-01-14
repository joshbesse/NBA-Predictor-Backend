import pandas as pd
from sklearn.metrics import accuracy_score

# load finalized data
df = pd.read_pickle('./Datasets/final.pkl')

# baseline 1: predict team with better win percentage to date (if tie then home team)
baseline1 = df.copy()
baseline1['PRED'] = baseline1.apply(lambda row: 1 if row['WIN_PCT_HOME'] >= row['WIN_PCT_AWAY'] else 0, axis=1)

b1_y_true = baseline1['HOME_WIN']
b1_y_pred = baseline1['PRED']
b1_accuracy = round(accuracy_score(b1_y_true, b1_y_pred) * 100, 2)
print(f"Baseline 1 Accuracy: {b1_accuracy}%")
print(f"Predicting the team with higher win percentage is correct {b1_accuracy}% of the time.")

# baseline 2: predict team with higher average net rating to date (if tie then home team)
baseline2 = df.copy()
baseline2['PRED'] = baseline1.apply(lambda row: 1 if row['NET_RATING_AVG_HOME'] >= row['NET_RATING_AVG_AWAY'] else 0, axis=1)

b2_y_true = baseline2['HOME_WIN']
b2_y_pred = baseline2['PRED']
b2_accuracy = round(accuracy_score(b2_y_true, b2_y_pred) * 100, 2)
print(f"Baseline 2 Accuracy: {b2_accuracy}%")
print(f"Predicting the team with higher average net rating is correct {b2_accuracy}% of the time.")
