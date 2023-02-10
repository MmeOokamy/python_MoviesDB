class Movie:
    def __init__(self, movie_id, movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year):
        self.movie_id = movie_id
        self.movie_api_id = movie_api_id
        self.movie_original_title = movie_original_title
        self.movie_french_title = movie_french_title
        self.movie_original_language = movie_original_language
        self.movie_img = movie_img
        self.movie_description = movie_description
        self.movie_rating = movie_rating
        self.movie_year = movie_year

class Genre:
    def __init__(self, genre_id, genre_api_id, genre_name):
        self.genre_id = genre_id
        self.genre_api_id = genre_api_id
        self.genre_name = genre_name

class MovieGenre:
    def __init__(self, movie_id, genre_id):
        self.movie_id = movie_id
        self.genre_id = genre_id