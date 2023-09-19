import pandas as pd
from utils import load_data
from utils import split_dataset
from utils import encoding
from utils import normalize
from utils import training
from utils import evaluate_model

# Loading cleaned data
data = load_data("C:/Users/USER/Documents/Master2 DIT/Outil versioning/branche1/arborescence_tree/data/cleaned/cleaned_data.csv")

# Splitting data
y = data['label']
X = data.drop('label', axis=1)
X_train, X_test, y_train, y_test = split_dataset(X, y)

# y Label encoding
y_train = encoding(y_train)
y_test = encoding(y_test)

# Normalize X features
X_train = normalize(X_train)
X_test = normalize(X_test)

# Training
y_pred = training(X_train, y_train, X_test)

# Evaluate model
accuracy, report = evaluate_model(y_test, y_pred)
print(f"The accuracy is {accuracy}")
print(f"The report is \n {report}")