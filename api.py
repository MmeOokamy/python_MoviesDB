import json, requests, csv, os

APIKEY = 'c3568fa2093e83bc9999ba366802f9c7'
LANGUAGE = 'fr'
ADULT = 'true'


# https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query=


def get_data(request):
    query = 'https://api.themoviedb.org/3/search/movie?api_key=c3568fa2093e83bc9999ba366802f9c7&language=fr&page=1&include_adult=false&query='+ request
             
    response =  requests.get(query)
    if response.status_code==200: 
    
        resp = response.json()
        text = json.dumps(resp)
        for movie in resp['results']:
            print(movie['title'])
        # print(resp['results'][1]['title'])
    else:
        print('error')

get_data('alien')