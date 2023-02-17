import re
from db import Database


class Genre:
    def __init__(self, genre_api_id: int, id=None, genre_name: str = None):
        self.db = Database()
        self.id = id
        self.genre_api_id = genre_api_id
        self.genre_name = genre_name

    def get_genre_name(self):
        (data,) = self.db.get_data("genres", "genre_name", f"genre_api_id={self.genre_api_id}", False)
        return data
    
    def exist(self):
        data = self.db.get_data("genres", "*", f"genre_api_id={self.genre_api_id}", False)
        return True if data else False
    
    def save(self):
        if self.id is None:
            data = self.db.get_data("genres", "*", f"genre_api_id={self.genre_api_id}")
            if data:
                self.id = data[0][0]
                self.db.update_data(
                    "genres", ["genre_name"], [self.genre_name], f"id={self.id}"
                )
            else:
                self.db.add_data(
                    "genres",
                    "genre_api_id, genre_name",
                    (self.genre_api_id, self.genre_name),
                )
                self.id = self.db.cursor.lastrowid
        else:
            self.db.update_data(
                "genres",
                ["genre_api_id", "genre_name"],
                [self.genre_api_id, self.genre_name],
                f"id={self.id}",
            )

    def delete(self):
        if self.id is not None:
            self.db.delete_data("genres", f"id={self.id}")
            self.id = None
