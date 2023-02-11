from db import Database

db = Database()

# create movies table
table_name = "movies"
fields = """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_api_id INTEGER UNIQUE NOT NULL,
            movie_original_title VARCHAR(255) NOT NULL,
            movie_french_title VARCHAR(255),
            movie_original_language VARCHAR(255),
            movie_img VARCHAR(255),
            movie_description TEXT,
            movie_rating INTEGER DEFAULT 0 CHECK (movie_rating BETWEEN 0 AND 100),
            movie_year INTEGER DEFAULT 1895 CHECK (movie_year >= 1895)
        """
db.create_table(table_name, fields)

# create genres table
table_name = "genres"
fields = """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_api_id INTEGER UNIQUE NOT NULL,
            genre_name VARCHAR(255) NOT NULL
        """
db.create_table(table_name, fields)

# create movies_genres table
table_name = "movies_genres"
fields = """
            movie_id INTEGER NOT NULL,
            genre_id INTEGER NOT NULL,
            PRIMARY KEY (movie_id , genre_id),
            FOREIGN KEY (movie_id)
                REFERENCES movies (id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (genre_id)
                REFERENCES genres (id)
                ON UPDATE CASCADE ON DELETE CASCADE
        """
db.create_table(table_name, fields)

db.close_connection()
