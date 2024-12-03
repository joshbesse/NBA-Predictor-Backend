import pandas as pd 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns   
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

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
train_split = int(len(scaled_df) * 0.80)

train_df = scaled_df[:train_split]
test_df = scaled_df[train_split:]

X_train, y_train = train_df.drop(columns=['Target']), train_df['Target']
X_test, y_test = test_df.drop(columns=['Target']), test_df['Target']

# perform cross-validation to find optimal regularization parameter
model = LogisticRegression(penalty='l2', solver='liblinear')

param_grid = {'C': [0.01, 0.1, 1, 10, 50, 75, 100, 110, 125, 150]}
ridge_cv = GridSearchCV(model, param_grid=param_grid, cv=5, scoring='accuracy')
ridge_cv.fit(X_train, y_train)

print("Best Regularization Parameter (C): ", ridge_cv.best_params_)
print("Validation Accuracy: ", ridge_cv.best_score_)

best_model = ridge_cv.best_estimator_

results = pd.DataFrame(ridge_cv.cv_results_)
plt.plot(results['param_C'], results['mean_test_score'])
plt.xscale('log')
plt.xlabel('Regularization Parameter (C)')
plt.ylabel('Validation Accuracy')
plt.title('Validation Accuracy vs. Regularization')
plt.show()

# evaluate model on test set
y_test_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_test_pred)
print("Test Accuracy: ", accuracy)
class_report = classification_report(y_test, y_test_pred)
print(class_report)