import pandas as pd

def load_dataset(file_path):
    return pd.read_csv(file_path)

ratings = load_dataset("movie_ratings.csv")
# this will print the first five rows 
print(ratings.head())

# creating pivot tables using csv file
ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
print(ratings_matrix)

