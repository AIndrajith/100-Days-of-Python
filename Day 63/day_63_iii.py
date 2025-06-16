import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset(file_path):
    return pd.read_csv(file_path)

ratings = load_dataset("movie_ratings.csv")

ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)

def recommend_movies(user_id, ratings_matrix, user_similarity):
    similar_users = user_similarity[user_id].sort_values(ascending=False).index[1:]
    recommend_movies = {}

    for similar_user in similar_users:
        watched_movies = ratings_matrix.loc[similar_user][ratings_matrix.loc[similar_user]> 0]
        for movie, rating in watched_movies.items():
            if ratings_matrix.loc[user_id, movie] == 0:
                if movie not in recommend_movies:
                    recommend_movies[movie] = rating
                else:
                    recommend_movies[movie] += rating
    return sorted(recommend_movies.items(), key=lambda x:x[1], reverse=True)

def calculate_similarity(matrix):
    similarity = cosine_similarity(matrix)
    return pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

user_similarity = calculate_similarity(ratings_matrix)
recommendations = recommend_movies(1, ratings_matrix, user_similarity)
print("Recommendations for user 1: ", recommendations)