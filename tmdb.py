import requests
import json
import pandas as pd

TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NDkwMTRkNDZkZTA2NzExYzBlZjFkMDcxNGYzMTJhNiIsInN1YiI6IjY0YjliYzViMDZmOTg0MDBjNGYxNjNlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SDYMlf3llBJluXwtPuBUX9b8CBFVNwx2DzKzU07yEyo"
TMDB_API_KEY = "449014d46de06711c0ef1d0714f312a6"

headers = {
    "accept": "application/json",
    # "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"
}

def add_genres(movie):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie['Name']}&primary_release_year={movie['Year']}"
    response = requests.get(url, headers=headers)
    tmdb_movie = json.loads(response.text)
    
    if (tmdb_movie["total_results"] == 0):
        return f"{movie['Name']} is a TV show"
    
    genre_ids = tmdb_movie["results"][0]["genre_ids"][0:3]
    return genre_ids

# small_ratings = pd.read_csv("data/small_ratings.csv")
# small_ratings["genres"] = small_ratings.apply(add_genres, axis='columns')
# print(small_ratings)

letterboxd_ratings = pd.read_csv("data/letterboxd_ratings.csv")
letterboxd_ratings["Genres"] = letterboxd_ratings.apply(add_genres, axis='columns')
print(letterboxd_ratings)
letterboxd_ratings.to_csv("data/letterboxd_ratings_with_genres.csv")