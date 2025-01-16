import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def time_series_cv(df, pipeline):
    # store accuracy for each fold
    accuracies = []

    # define features
    features = [col for col in df.columns if col not in ['HOME_WIN', 'GAME_DATE', 'GAME_ID', 'TEAM_ID_HOME', 'TEAM_NAME_HOME', 'TEAM_ID_AWAY', 'TEAM_NAME_AWAY']]

    # define (5) folds 
    train_folds = [0.1666, 0.3332, 0.4998, 0.6664, 0.833]
    test_folds = [0.3332, 0.4998, 0.6664, 0.8330, 1.0]

    # looping for each fold
    for i in range(len(train_folds)):
        # define train and test split indices
        train_split = int(len(df) * train_folds[i])
        test_split = int(len(df) * test_folds[i])

        # slice the data chronologically
        X_train = df.iloc[:train_split][features]
        y_train = df.iloc[:train_split]['HOME_WIN']
        X_test = df.iloc[train_split:test_split][features]
        y_test = df.iloc[train_split:test_split]['HOME_WIN']

        # train model
        pipeline.fit(X_train, y_train)

        # test model
        y_pred = pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)

    return np.mean(accuracies)

def hyperparameter_tuning(df):
    # define parameter grid
    param_grid = {
        'C': [0.01, 0.1, 1.0, 10.0],
        'solver': ['lbfgs', 'saga', 'liblinear']
    }

    best_score = -1
    best_params = None

    for c in param_grid['C']:
        for solver in param_grid['solver']:
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('logreg', LogisticRegression(max_iter=1000, C=c, solver=solver))
            ])

            score = time_series_cv(df, pipeline)

            print(f"C={c}, solver={solver}, CV Score={score:.4f}")
            if score > best_score:
                best_score = score
                best_params = (c, solver)
    
    print(f'Best hyperparameters: {best_params}')
    print(f'Best CV score:{best_score}')
    
    return best_params

# load finalized data
training_df = pd.read_pickle('./Datasets/final.pkl')

# sort data by date
training_df = training_df.sort_values('GAME_DATE').reset_index(drop=True)

# perform hyperparameter tuning using time series cross-validation
hyperparameters = hyperparameter_tuning(training_df)

# train best model on full dataset
features = [col for col in training_df.columns if col not in ['HOME_WIN', 'GAME_DATE', 'GAME_ID', 'TEAM_ID_HOME', 'TEAM_NAME_HOME', 'TEAM_ID_AWAY', 'TEAM_NAME_AWAY']]
X_train = training_df[features]
y_train = training_df['HOME_WIN']

model = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(max_iter=1000, C=hyperparameters[0], solver=hyperparameters[1]))
]) 

model.fit(X_train, y_train)

# use current season data as hold out set
test_df = pd.read_pickle('./Datasets/test_final.pkl')
test_df = test_df.sort_values('GAME_DATE').reset_index(drop=True)

X_test = test_df[features]
y_test = test_df['HOME_WIN']

y_pred = model.predict(X_test)
print(f'Hold-Out Accuracy: {accuracy_score(y_test, y_pred)}')
print(f'Classification Report: \n {classification_report(y_test, y_pred)}')
