import json, requests

APIKEY = 'c3568fa2093e83bc9999ba366802f9c7'
LANGUAGE = 'fr'
ADULT = 'true'


# https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=


def get_api_movies_list(request):
    
    query = 'https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query='+ request
    movies_list = []
    response =  requests.get(query)

    if response.status_code==200: 
        movies_json = response.json()
        movies_json_results= movies_json['results'] 

        for movie in movies_json_results:
            movie_obj = {}
            movie_obj.update({'movie_id': movie['id']})
            movie_obj.update({'movie_original_title': movie['original_title']})
            movie_obj.update({'movie_french_title': movie['title']})
            movies_list.append(movie_obj)

        return movies_list
    else:
        print('error')

