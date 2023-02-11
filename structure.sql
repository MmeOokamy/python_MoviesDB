-- # Structure de la base de donnée pour sqlite3
CREATE TABLE IF NOT EXISTS "movies" (
	"id"	INTEGER,
	"movie_api_id"	INTEGER NOT NULL UNIQUE,
	"movie_original_title"	VARCHAR(255) NOT NULL,
	"movie_french_title"	VARCHAR(255),
	"movie_original_language"	VARCHAR(255),
	"movie_img"	VARCHAR(255),
	"movie_description"	TEXT,
	"movie_rating"	INTEGER DEFAULT 0 CHECK("movie_rating" BETWEEN 0 AND 100),
	"movie_year"	INTEGER DEFAULT 1895 CHECK("movie_year" >= 1895),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "genres" (
	"id"	INTEGER,
	"genre_api_id"	INTEGER NOT NULL UNIQUE,
	"genre_name"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "movies_genres" (
	"movie_id"	INTEGER NOT NULL,
	"genre_id"	INTEGER NOT NULL,
	FOREIGN KEY("movie_id") REFERENCES "movies"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("genre_id") REFERENCES "genres"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("movie_id","genre_id")
);

-- # class Database qui fait le lien entre la base de donnée et l'application:

-- class Database:

--     def __init__(self):
--         self.conn = sqlite3.connect("movies.db")
--         self.cursor = self.conn.cursor()

--     def create_table(self, table_name, fields):
--         query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
--         self.cursor.execute(query)
--         self.conn.commit()

--     def add_data(self, table_name, fields, values):
--         placeholders = ', '.join('?' * len(values))
--         query = f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
--         self.cursor.execute(query, values)
--         self.conn.commit()

--     def get_data(self, table_name, fields, conditions=None):
--         query = f"SELECT {fields} FROM {table_name}"
--         if conditions:
--             query += f" WHERE {conditions}"
--         self.cursor.execute(query)
--         data = self.cursor.fetchall()
--         return data

--     def update_data(self, table_name, fields, values, conditions):
--         placeholders = ', '.join([f"{field}=?" for field in fields])
--         query = f"UPDATE {table_name} SET {placeholders} WHERE {conditions}"
--         self.cursor.execute(query, values)
--         self.conn.commit()

--     def delete_data(self, table_name, conditions):
--         query = f"DELETE FROM {table_name} WHERE {conditions}"
--         self.cursor.execute(query)
--         self.conn.commit()

--     def close_connection(self):
--         self.conn.close()


-- # model / class en python

-- class Genre:
--     def __init__(self, id, genre_api_id, genre_name):

--         self.id = id
--         self.genre_api_id = genre_api_id  # valeur unique
--         self.genre_name = genre_name
        
--     def save(self, db):
--         if self.id is None:
--             data = db.get_data("genres", "*", f"genre_api_id={self.genre_api_id}")
--             if data:
--                 self.id = data[0][0]
--                 db.update_data("genres", ["genre_name"], [self.genre_name], f"id={self.id}")
--             else:
--                 db.add_data("genres", "genre_api_id, genre_name", (self.genre_api_id, self.genre_name))
--                 self.id = db.cursor.lastrowid
--         else:
--             db.update_data("genres", ["genre_api_id", "genre_name"], [self.genre_api_id, self.genre_name], f"id={self.id}")

--     def delete(self, db):
--         if self.id is not None:
--             db.delete_data("genres", f"id={self.id}")
--             self.id = None


-- class Movie:
--     def __init__(self, movie_api_id: int, movie_original_title: str, id=None, movie_french_title: str = None, movie_original_language: str = None, movie_img: str = None, movie_description: str = None, movie_rating: int = 0, movie_year: int = 1895, genres: list[Genre] = None):

--         self.id = id
--         self.movie_api_id = movie_api_id  # valeur unique
--         self.movie_original_title = movie_original_title
--         self.movie_french_title = movie_french_title
--         self.movie_original_language = movie_original_language
--         self.movie_img = movie_img
--         self.movie_description = movie_description
--         self.movie_rating = movie_rating
--         self.movie_year = movie_year
--         self.genres = genres or []

-- def save():
-- 	# verifie si movie_api_id existe
-- 	# si existe alors on update_data dans la table 
-- 	# sinon on add_data

-- def delete():
-- 	# verifie si movie_api_id existe
-- 	# si existe alors on delete_data



