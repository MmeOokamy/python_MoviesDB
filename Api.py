import json, requests

# APIKEY = 'c3568fa2093e83bc9999ba366802f9c7'
# LANGUAGE = 'fr'
# ADULT = 'true'

# https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=


class API:
    def __init__(
        self,
        api_key="c3568fa2093e83bc9999ba366802f9c7",
        language="fr",
        include_adult=False,
    ):
        self.api_key = api_key
        self.language = language
        self.include_adult = include_adult

    def search_movies(self, request):
        query = f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&language={self.language}&page=1&include_adult={self.include_adult}&query={request}"
        movies_list = []
        response = requests.get(query)

        if response.status_code == 200:
            movies_json = response.json()
            movies_json_results = movies_json["results"]

            for movie in movies_json_results:
                movie_obj = {}
                movie_obj.update({"movie_id": movie["id"]})
                movie_obj.update({"movie_original_title": movie["original_title"]})
                movie_obj.update({"movie_french_title": movie["title"]})
                movies_list.append(movie_obj)

            return movies_list
        else:
            return response.status_code

    def get_movie(self, movie_api_id):
        query= f"https://api.themoviedb.org/3/movie/{movie_api_id}?api_key={self.api_key}&language={self.language}"
        movie_api_detail = {}
        response = requests.get(query)

        if response.status_code == 200:
            movie = response.json()

            return movie
        else:
            return response.status_code
