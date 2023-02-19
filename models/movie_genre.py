from db import Database

class MovieGenre:
    def __init__(self, movie_id, genre_id):
        self.db = Database()
        self.movie_id = movie_id
        self.genre_id = genre_id
        
    def save(self):
        self.db.add_data("movies_genres", "movie_id, genre_id", [self.movie_id, self.genre_id])
        
    def delete(self):
        self.db.delete_data("movies_genres", f"movie_id={self.movie_id}")
        
    def all_genre_id(self, movie_id=None):
        if movie_id is None:
            movie_id = self.movie_id

        data = self.db.get_data("movies_genres", "genre_id", f"movie_id={movie_id}", False)
        return data