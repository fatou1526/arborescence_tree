"""Contient le preprocessing des donn�es."""
from utils import load_data
from utils import preprocessing_duplicates
from utils import preprocessing_null
from utils import preprocessing_outliers

data = load_data('data/raw/Crop_recommendation.csv')
print (data.head())

# Preprocessing data (duplicates, outliers, null )
data = preprocessing_duplicates(data)
data = preprocessing_outliers(data)
data = preprocessing_null(data)

data.to_csv("data/processed/processed_data.csv", index = False)
data.to_csv("data/cleaned/cleaned_data.csv", index = False)