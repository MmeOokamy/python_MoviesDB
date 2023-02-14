
from db import Database
from models import Genre, Movie
from Api import API
api = API()

def detail(search_detail_entry):
    mdb_id = search_detail_entry.get()
    movie = api.get_movie(mdb_id)
    if movie:
        print(movie)
    else:
        print("Connais pô!")

def search(search_entry):
    entry = search_entry.get()
    movies = api.search_movies(entry)
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("Connais pô!")


def update_genres_table():
    db = Database()
    # appele l'api des genres et met a jour la bdd.
    genres = api.get_genres()
    for genre in genres:
        genre_obj = Genre(genre['id'], None, genre['name'])
        if not genre_obj.exist():
            genre_obj.save()
    db.close_connection()
    print('base mise à jour')
    

def convert_average(self, vote_average):
    average = int(float(vote_average) * 100)
    return average

def api_search_movies_to_list(self, movie):
    genres = []
    if "genre_ids" in movie:
        for g_id in movie["genre_ids"]:
            genres.append(genre)

    api_movie = {
        "movie_api_id": movie["id"],
        "movie_original_title": movie["original_title"],
        "movie_french_title": movie["title"],
        "movie_original_language": movie["original_language"],
        "movie_poster": movie["poster_path"],
        "movie_backdrop": movie["backdrop_path"],
        "movie_description": movie["overview"],
        "movie_rating": convert_average(movie['vote_average']),
        "movie_release_date": movie["release_date"],
        "genres": [genres],
    }
    return api_movie

def api_get_movie_to_obj(self, movie):
    genres = []
    if "genres" in movie:
        for genre in movie["genres"]:
            g = {"genre_api_id": genre["id"], "genre_name": genre["name"]}
            genres.append(g)

    api_movie = {
        "movie_api_id": movie["id"],
        "movie_original_title": movie["original_title"],
        "movie_french_title": movie["title"],
        "movie_original_language": movie["original_language"],
        "movie_poster": movie["poster_path"],
        "movie_backdrop": movie["backdrop_path"],
        "movie_description": movie["overview"],
        "movie_tagline": movie["tagline"],
        "movie_rating": movie[""],
        "movie_release_date": convert_average(movie['vote_average']),
        "genres": [genres],
    }
    return api_movie