import json, requests

APIKEY = 'c3568fa2093e83bc9999ba366802f9c7'
LANGUAGE = 'fr'
ADULT = 'true'


# https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=


def get_api_movies_list(request):
    query = 'https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=' + request
    movies_list = []
    response = requests.get(query)

    if response.status_code == 200:
        movies_json = response.json()
        movies_json_results = movies_json['results']

        for movie in movies_json_results:
            movie_obj = {}
            movie_obj.update({'movie_id': movie['id']})
            movie_obj.update({'movie_original_title': movie['original_title']})
            movie_obj.update({'movie_french_title': movie['title']})
            movies_list.append(movie_obj)

        return movies_list
    else:
        print(response)


# call moviedb for had more detail
# https://api.themoviedb.org/3/movie/348?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr
def get_api_movie(movie_api_id):
    api_url = 'https://api.themoviedb.org/3/movie/' + str(
        movie_api_id) + '?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr'
    movie_api_detail = {}
    resp = requests.get(api_url)
    if resp.status_code == 200:
        data = resp.json()
        movie_api_detail.update({'movie_api_id': data['id']})
        movie_api_detail.update({'movie_original_title': data['original_title']})
        movie_api_detail.update({'movie_french_title': data['title']})
        movie_api_detail.update({'movie_original_language': data['original_language']})
        movie_api_detail.update({'movie_img': data['poster_path']})
        movie_api_detail.update({'movie_description': data['overview']})
        movie_api_detail.update({'movie_rating': int(data['popularity'])})
        movie_api_detail.update({'movie_year': data['release_date']})
        return movie_api_detail
    else:
        print(resp.status_code)
