from db import Database

db = Database()


class Genre:
    def __init__(self, genre_api_id: int, id=None, genre_name: str = None):

        self.id = id
        self.genre_api_id = genre_api_id
        self.genre_name = genre_name

    def save(self, db):
        if self.id is None:
            data = db.get_data("genres", "*", f"genre_api_id={self.genre_api_id}")
            if data:
                self.id = data[0][0]
                db.update_data("genres", ["genre_name"], [self.genre_name], f"id={self.id}")
            else:
                db.add_data("genres", "genre_api_id, genre_name", (self.genre_api_id, self.genre_name))
                self.id = db.cursor.lastrowid
        else:
            db.update_data("genres", ["genre_api_id", "genre_name"], [self.genre_api_id, self.genre_name],
                           f"id={self.id}")

    def delete(self, db):
        if self.id is not None:
            db.delete_data("genres", f"id={self.id}")
            self.id = None


class Movie:
    def __init__(self, movie_api_id: int, movie_original_title: str, id=None, movie_french_title: str = None,
                 movie_original_language: str = None, movie_img: str = None, movie_description: str = None,
                 movie_rating: int = 0, movie_year: int = 1895, genres: list[Genre] = []):
        assert isinstance(movie_api_id, int), "L'attribut 'movie_api_id' doit être un entier."
        assert isinstance(movie_original_title, str) and len(
            movie_original_title) <= 255, "L'attribut 'movie_original_title' doit être une chaîne de caractères."
        assert isinstance(movie_french_title, str) and len(
            movie_french_title) <= 255 or movie_french_title is None, "L'attribut 'movie_french_title' doit être une " \
                                                                      "chaîne de caractères ou None."
        assert isinstance(movie_original_language, str) and len(
            movie_original_language) <= 255 or movie_original_language is None, "L'attribut 'movie_original_language' "\
                                                                                "doit être une chaîne de caractères " \
                                                                                "ou None."
        assert isinstance(movie_img, str) and len(
            movie_img) <= 255 or movie_img is None, "L'attribut 'movie_img' doit être une chaîne de caractères ou None."
        assert isinstance(movie_description, str) and len(
            movie_description) <= 65535 or movie_description is None, "L'attribut 'movie_description' doit être une " \
                                                                      "chaîne de caractères ou None."
        assert isinstance(movie_rating,
                          int) and 0 <= movie_rating <= 100, "L'attribut 'movie_rating' doit être un entier entre 0 " \
                                                             "et 100"
        assert isinstance(movie_year,
                          int) and movie_year >= 1895, "L'attribut 'movie_year' doit être un entier supérieur ou égal "\
                                                       "à 1895"

        self.id = id
        self.movie_api_id = movie_api_id  # valeur unique
        self.movie_original_title = movie_original_title
        self.movie_french_title = movie_french_title
        self.movie_original_language = movie_original_language
        self.movie_img = movie_img
        self.movie_description = movie_description
        self.movie_rating = movie_rating
        self.movie_year = movie_year
        self.genres = genres or []

    def save(self, db):
        if self.id:
            db.update_data("movies",
                           ["movie_api_id", "movie_original_title", "movie_french_title", "movie_original_language",
                            "movie_img", "movie_description", "movie_rating", "movie_year"],
                           [self.movie_api_id, self.movie_original_title, self.movie_french_title,
                            self.movie_original_language, self.movie_img, self.movie_description, self.movie_rating,
                            self.movie_year],
                           f"id={self.id}")
        else:
            db.add_data("movies",
                        "movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, "
                        "movie_description, movie_rating, movie_year",
                        [self.movie_api_id, self.movie_original_title, self.movie_french_title,
                         self.movie_original_language, self.movie_img, self.movie_description, self.movie_rating,
                         self.movie_year])
            self.id = db.cursor.lastrowid

        # sauvegarde les genres associés à ce film
        if not isinstance(self.genres, list):
            self.genres = [self.genres]
        for genre in self.genres:
            genre.save(db)
            db.add_data("movies_genres", "movie_id, genre_id", [self.id, genre.id])

    def delete(self, db):
        if self.id:
            # supprime les entrées dans la table de liaison movies_genres
            db.delete_data("movies_genres", f"movie_id={self.id}")
            # supprime le film lui-même
            db.delete_data("movies", f"id={self.id}")
            self.id = None
