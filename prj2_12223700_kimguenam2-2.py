import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor


def sort_dataset(dataset_df):
    sorted = dataset_df.sort_values(by='year')
    return sorted


def split_dataset(dataset_df):
    val = dataset_df.drop('salary',axis=1)
    sal = dataset_df['salary']
    sal = sal * 0.001
    X_train = val[:1718]
    X_test = val[1718:]
    Y_train = sal[:1718]
    Y_test = sal[1718:]
    return X_train, X_test, Y_train, Y_test


def extract_numerical_cols(dataset_df):
    extract = dataset_df[
        ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]
    return extract


def train_predict_decision_tree(X_train, Y_train, X_test):
    reg = DecisionTreeRegressor()
    reg.fit(X_train, Y_train)
    return reg.predict(X_test)


def train_predict_random_forest(X_train, Y_train, X_test):
    reg = RandomForestRegressor()
    reg.fit(X_train, Y_train)
    return reg.predict(X_test)


def train_predict_svm(X_train, Y_train, X_test):
    svm_pipe=make_pipeline(
        StandardScaler(),
        SVR()
    )

    svm_pipe.fit(X_train, Y_train)
    return svm_pipe.predict(X_test)


def calculate_RMSE(labels, predictions):
    return np.sqrt(np.mean((predictions - labels) ** 2))


if __name__ == '__main__':
    # DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
    print("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
    print("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
