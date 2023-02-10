from db import Database

db = Database()

# create movies table
table_name = "movies"
fields = """
            movie_id SERIAL PRIMARY KEY UNIQUE,
            movie_api_id INTEGER UNIQUE,
            movie_original_title VARCHAR(255) NOT NULL,
            movie_french_title VARCHAR(255) NOT NULL,
            movie_original_language VARCHAR(255) NOT NULL,
            movie_img VARCHAR(255) NOT NULL,
            movie_description TEXT NOT NULL,
            movie_rating INTEGER,
            movie_year INTEGER
        """
db.create_table(table_name, fields)

# create genres table
table_name = "genres"
fields = """
            genre_id SERIAL PRIMARY KEY,
            genre_api_id INTEGER UNIQUE,
            genre_name VARCHAR(255)
        """
db.create_table(table_name, fields)

# create movies_genres table
table_name = "movies_genres"
fields = """
            movie_id INTEGER NOT NULL,
            genre_id INTEGER NOT NULL,
            PRIMARY KEY (movie_id , genre_id),
            FOREIGN KEY (movie_id)
                REFERENCES movies (movie_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (genre_id)
                REFERENCES genres (genre_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        """
db.create_table(table_name, fields)

db.close_connection()
