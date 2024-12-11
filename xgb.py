import pandas as pd 
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# load data
df = pd.read_pickle('./final.pkl')

# split the data
train_split = int(len(df) * 0.80)

train_df = df[:train_split]
test_df = df[train_split:]

X_train, y_train = train_df.drop(columns=['Target']), train_df['Target']
X_test, y_test = test_df.drop(columns=['Target']), test_df['Target']

# initialize xgboost model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=3)

# cross-validation for hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 9],
    'learning_rate': [0.01, 0.1, 0.2, 0.3],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'gamma': [0, 0.1, 0.3, 0.5],
    'lambda': [0.01, 0.1, 1.0, 10.0],
    'alpha': [0, 0.1, 1.0],
}

grid_search = GridSearchCV(model, param_grid=param_grid, cv=5, scoring='accuracy', verbose=2, n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best Parameters: ", grid_search.best_params_)
print("Best Validation Accuracy: ", grid_search.best_score_)

best_model = grid_search.best_estimator_

# evaluate model on test set
y_test_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_test_pred)
print("Test Accuracy: ", accuracy)
class_report = classification_report(y_test, y_test_pred)
print(class_report)