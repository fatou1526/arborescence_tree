"""
This module contains methods to preprocess the data
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data(filepath):
    # loading dataset
    df = pd.read_csv(filepath)
    return df

def preprocessing_duplicates(data_df):
    # This method help to drop duplicates
    if data_df.duplicated().sum() == 0:
        print("No duplicates")
        data_df_nd = data_df
    else:
        print("Remove duplicates")
        data_df_nd = data_df.drop_duplicates()
    return data_df_nd

def preprocessing_null(data_df):
    # This method help to drop NaN values
    data_nn = data_df.dropna()
    return data_nn

def preprocessing_outliers(data_df):
    # Here, the method helps to remove outliers
    col = data_df.columns.drop("label")
    for i in col:
        col_skew = data_df[i].skew()
        print(f"The skew for column {i} is {col_skew}")
        if (col_skew < -1) | (col_skew > 1):
            print(f"Column {i} has outliers")
            data_df[i] = np.where(data_df[i] < data_df[i].quantile(0.1), data_df[i].quantile(0.1), data_df[i])
            data_df[i] = np.where(data_df[i] > data_df[i].quantile(0.9), data_df[i].quantile(0.9), data_df[i])
            print(f" The skew for column {i} is now {data_df[i].skew()}")
        else:
            print(f"There are not outliers at column {i}")
    return data_df


def split_dataset(X, y):
    # This method helps to split the data to train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    return X_train, X_test, y_train, y_test 

# label encoder
def encoding(label):
    le= LabelEncoder()
    label =le.fit_transform(label)
    return label

# Normalization/Standardisation
def normalize(features):
    features = StandardScaler().fit_transform(features)
    return features

# Training
def training(X_train, y_train, X_test):    
    rfc = RandomForestClassifier(n_estimators=100, random_state=24)
    rfc.fit(X_train, y_train)
    y_pred = rfc.predict(X_test)
    return y_pred

# Evaluate model
def evaluate_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report


