import requests


class API:
    def __init__(self, include_adult=False):
        self.api_key = "c3568fa2093e83bc9999ba366802f9c7"
        self.language = "fr"
        self.include_adult = include_adult

    def get_genres(self):
        # utilise pour mettre à jour la liste des genres en base
        response = requests.get(
            f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language={self.language}"
        )
        if response.status_code == 200:
            genres = response.json()
            return genres['genres']

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
            return results
        else:
            return response.status_code

    def get_movie(self, movie_api_id):
        query = f"https://api.themoviedb.org/3/movie/{movie_api_id}?api_key={self.api_key}&language={self.language}"
        response = requests.get(query)

        if response.status_code == 200:
            movie = response.json()
            return movie
        else:
            return response.status_code
