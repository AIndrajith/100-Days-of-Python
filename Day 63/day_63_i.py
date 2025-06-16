# Building the Recommendation System

import pandas as pd

def load_dataset(file_path):
    return pd.read_csv(file_path)

ratings = load_dataset("movie_ratings.csv")
# this will print the first five rows 
print(ratings.head())