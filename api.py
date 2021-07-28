import json, requests, csv, os

APIKEY = 'c3568fa2093e83bc9999ba366802f9c7'
LANGUAGE = 'fr'
ADULT = 'true'


# https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=


def get_data(request):
    query = 'https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query='+ request
    movie_list = []

    response =  requests.get(query)
    if response.status_code==200: 
        resp = response.json()
        text = json.dumps(resp)
        # print(len(resp['results']))
        cible = resp['results'] 
        i=0
        for movie in cible:
            movie_obj = {}
            movie_obj.update({'movie_id': movie['id']})
            movie_obj.update({'movie_original_title': movie['original_title']})
            movie_obj.update({'movie_french_title': movie['title']})
            # movie_list.update({i: movie_obj})
            movie_list.append(movie_obj)
            i+=1
        # print(movie_list)
        return movie_list
        # create new obj
        # movie_list = {
        #     'movie_id': "",
        #     'movie_original_title': "",
        #     'movie_french_title': "",
        # }

    else:
        print('error')

