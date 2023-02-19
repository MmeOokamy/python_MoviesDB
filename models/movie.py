import re
from db import Database
from models.genre import Genre

class MovieGenre:
    def __init__(self, movie_id, genre_id):
        pass
    
class Movie:
    def __init__(
            self,
            movie_api_id: int,
            movie_original_title: str,
            id=None,
            movie_french_title: str = None,
            movie_original_language: str = None,
            movie_poster: str = None,
            movie_backdrop: str = None,
            movie_description: str = None,
            movie_tagline: str = None,
            movie_rating: float = 0.0,
            movie_release_date: str = '1895-12-28',
            genres: list[Genre] = [],
    ):
        assert isinstance(
            movie_api_id, int
        ), "L'attribut 'movie_api_id' doit être un entier."
        assert (
                isinstance(movie_original_title, str) and len(movie_original_title) <= 255
        ), "L'attribut 'movie_original_title' doit être une chaîne de caractères."
        assert (
                isinstance(movie_french_title, str)
                and len(movie_french_title) <= 255
                or movie_french_title is None
        ), "L'attribut 'movie_french_title' doit être une chaîne de caractères ou None."
        assert (
                isinstance(movie_original_language, str)
                and len(movie_original_language) <= 255
                or movie_original_language is None
        ), "L'attribut 'movie_original_language' doit être une chaîne de caractères ou None."
        assert (
                isinstance(movie_poster, str)
                and len(movie_poster) <= 255 or movie_poster is None
        ), "L'attribut 'movie_poster' doit être une chaîne de caractères ou None."
        assert (
                isinstance(movie_backdrop, str)
                and len(movie_backdrop) <= 255 or movie_backdrop is None
        ), "L'attribut 'movie_backdrop' doit être une chaîne de caractères ou None."
        assert (
                isinstance(movie_description, str)
                and len(movie_description) <= 65535
                or movie_description is None
        ), "L'attribut 'movie_description' doit être une chaîne de caractères ou None."
        assert (
                isinstance(movie_tagline, str)
                and len(movie_tagline) <= 65535
                or movie_tagline is None
        ), "L'attribut 'movie_description' doit être une chaîne de caractères ou None."
        assert (
                isinstance(movie_rating, float) and 0.0 <= movie_rating <= 100.0
        ), "L'attribut 'movie_rating' doit être un entier/decimal entre 0.0 et 100.0"
        assert (
                isinstance(movie_release_date, str)
                and re.match(r'\d{4}-\d{2}-\d{2}', movie_release_date)
        ), "Format doit être YYYY-MM-DD"

        self.db = Database()
        self.id = id
        self.movie_api_id = movie_api_id  # valeur unique
        self.movie_original_title = movie_original_title
        self.movie_french_title = movie_french_title
        self.movie_original_language = movie_original_language
        self.movie_poster = movie_poster
        self.movie_backdrop = movie_backdrop
        self.movie_description = movie_description
        self.movie_tagline = movie_tagline
        self.movie_rating = movie_rating
        self.movie_release_date = movie_release_date
        self.genres = genres or []

    def exist(self):
        data = self.db.get_data("movies", "*", f"movie_api_id={self.movie_api_id}", False)
        return True if data else False

    def get_by_api_id(self, api_id):
        data = self.db.get_data("movies", "*", f"movie_api_id={api_id}", False)
        return data

    def get_by_id(self, id):
        data = self.db.get_data("movies", "*", f"id={id}", False)
        return data

    def save(self):
        if self.id:
            self.db.update_data(
                "movies",
                [
                    "movie_api_id",
                    "movie_original_title",
                    "movie_french_title",
                    "movie_original_language",
                    "movie_poster",
                    "movie_backdrop",
                    "movie_description",
                    "movie_tagline",
                    "movie_rating",
                    "movie_release_date",
                ],
                [
                    self.movie_api_id,
                    self.movie_original_title,
                    self.movie_french_title,
                    self.movie_original_language,
                    self.movie_poster,
                    self.movie_backdrop,
                    self.movie_description,
                    self.movie_tagline,
                    self.movie_rating,
                    self.movie_release_date
                ],
                f"id={self.id}",
            )
        else:
            self.db.add_data(
                "movies",
                "movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_poster,"
                "movie_backdrop, movie_description, movie_tagline, movie_rating, movie_release_date",
                [
                    self.movie_api_id,
                    self.movie_original_title,
                    self.movie_french_title,
                    self.movie_original_language,
                    self.movie_poster,
                    self.movie_backdrop,
                    self.movie_description,
                    self.movie_tagline,
                    self.movie_rating,
                    self.movie_release_date,
                ],
            )
            self.id = self.db.cursor.lastrowid

        # sauvegarde les genres associés à ce film
        if not isinstance(self.genres, list):
            self.genres = [self.genres]
        for genre in self.genres:
            genre.save()
            self.db.add_data("movies_genres", "movie_id, genre_id", [self.id, genre.id])

    def delete(self):
        if self.id:
            # supprime les entrées dans la table de liaison movies_genres
            self.db.delete_data("movies_genres", f"movie_id={self.id}")
            # supprime le film lui-même
            self.db.delete_data("movies", f"id={self.id}")
            self.id = None
