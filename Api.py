import requests


# APIKEY = 'c3568fa2093e83bc9999ba366802f9c7'
# LANGUAGE = 'fr'
# ADULT = 'true'


# https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=
# https://api.themoviedb.org/3/search/genre?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=
# https://api.themoviedb.org/3/genre/movie/list?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr

class API:
    def __init__(self, include_adult=False):
        self.api_key = "c3568fa2093e83bc9999ba366802f9c7"
        self.language = "fr"
        self.include_adult = include_adult

    def get_genre_by_id(self, genre_id):
        genres = requests.get(
            f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language={self.language}"
        )
        for genre in genres:
            print(genre['id'])

    def api_movies_to_movies(self, movie):
        genres = []
        if "genre_ids" in movie:
            for g_id in movie["genre_ids"]:
                genre = self.get_genre_by_id(g_id)
                genres.append(genre)

        api_movie = {
            "movie_api_id": movie["id"],
            "movie_original_title": movie["original_title"],
            "movie_french_title": movie["title"],
            "movie_original_language": movie["original_language"],
            "movie_poster": movie["poster_path"],
            "movie_backdrop": movie["backdrop_path"],
            "movie_description": movie["overview"],
            "movie_rating": self.convert_average(movie['vote_average']),
            "movie_release_date": movie["release_date"],
            "genres": [genres],
        }
        return api_movie

    def convert_average(self, vote_average):
        average = int(float(vote_average) * 100)
        return average

    def api_movie_to_movie(self, movie):
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
            "movie_release_date": self.convert_average(movie['vote_average']),
            "genres": [genres],
        }
        return api_movie

    def search_movies(self, request):
        query = (
            f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&language={self.language}&page=1"
            f"&include_adult={self.include_adult}&query={request}"
        )
        response = requests.get(query)
        movies = []
        if response.status_code == 200:
            r_json = response.json()
            results = r_json["results"]
            for movie in r_json["results"]:
                movie_obj = self.api_movies_to_movies(movie)
            movies.append(movie_obj)
            return movies
        else:
            return response.status_code

    def get_movie(self, movie_api_id):
        query = f"https://api.themoviedb.org/3/movie/{movie_api_id}?api_key={self.api_key}&language={self.language}"
        response = requests.get(query)

        if response.status_code == 200:
            movie = response.json()
            movie = self.api_movie_to_movie(movie)
            return movie
        else:
            return response.status_code
