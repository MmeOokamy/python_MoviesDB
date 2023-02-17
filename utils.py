from db import Database
from models.genre import Genre
from models.movie import Movie
from Api import API

api = API()


def detail(search_detail_entry):
    mdb_id = search_detail_entry.get()
    movie = api.get_movie(mdb_id)
    if movie:
        movie = api_get_movie_to_obj(movie)
        return movie
    else:
        print("Connais pô!")


def search(search_entry):
    entry = search_entry.get()
    movies = api.search_movies(entry)
    if movies:
        results = []
        for movie in movies:
            # print(movie)
            movie = api_search_movies_to_list(movie)
            results.append(movie)
        return results
    else:
        # print("Connais pô!")
        return "Connais pô!"


def update_genres_table():
    db = Database()
    # appele l'api des genres et met a jour la bdd.
    genres = api.get_genres()
    for genre in genres:
        genre_obj = Genre(genre['id'], None, genre['name'])
        if not genre_obj.exist():
            genre_obj.save()
    db.close_connection()


def convert_average(vote_average):
    average = int(float(vote_average) * 10)
    return average


def api_search_movies_to_list(movie):
    genres = []
    if "genre_ids" in movie:
        for genre in movie["genre_ids"]:
            genre_obj = Genre(genre_api_id=genre).get_genre_name()
            genres.append(genre_obj)

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
        "genres": genres,
    }
    return api_movie


def api_get_movie_to_obj(movie):
    genres = []
    if "genres" in movie:
        for genre in movie["genres"]:
            genre_obj = Genre(genre_api_id=genre["id"]).get_genre_name()
            genres.append(genre_obj)

    api_movie = {
        "movie_api_id": movie["id"],
        "movie_original_title": movie["original_title"],
        "movie_french_title": movie["title"],
        "movie_original_language": movie["original_language"],
        "movie_poster": movie["poster_path"],
        "movie_backdrop": movie["backdrop_path"],
        "movie_description": movie["overview"],
        "movie_tagline": movie["tagline"],
        "movie_rating": convert_average(movie['vote_average']),
        "movie_release_date": movie["release_date"],
        "genres": genres,
    }
    return api_movie
