import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
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

# initialize random forest model
rf_model = RandomForestClassifier(random_state=3)

# cross-validation for hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None],
    'bootstrap': [True, False]
}

rf_cv = GridSearchCV(rf_model, param_grid=param_grid, cv=5, scoring='accuracy', verbose=2, n_jobs=-1)
rf_cv.fit(X_train, y_train)

print("Best Parameters: ", rf_cv.best_params_)
print("Best Validation Accuracy: ", rf_cv.best_score_)

best_model = rf_cv.best_estimator_

# evaluate model on test set
y_test_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_test_pred)
print("Test Accuracy: ", accuracy)
class_report = classification_report(y_test, y_test_pred)
print(class_report)