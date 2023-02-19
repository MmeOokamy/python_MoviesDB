import unittest
from db import Database
from models.movie import Movie
from models.genre import Genre


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.movie = Movie(
            movie_api_id=1,
            movie_original_title='The Godfather',
            movie_french_title='Le Parrain',
            movie_original_language='en',
            movie_poster='/the_godfather/poster.jpg',
            movie_backdrop='/the_godfather/backdrop.jpg',
            movie_description='The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            movie_tagline='An offer you can\'t refuse.',
            movie_rating=9.2,
            movie_release_date='1972-03-14',
            genres=[Genre(genre_api_id=18, genre_name='Drama'), Genre(genre_api_id=80, genre_name='Crime')]
        )

    def tearDown(self):
        self.movie.delete()
        self.db.close_connection()
        

if __name__ == "__main__":
    unittest.main()
