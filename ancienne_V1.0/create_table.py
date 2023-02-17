import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        # """
        #     TRUNCATE TABLE movies CASCADE;
        #     TRUNCATE TABLE genres CASCADE;
        # """,
        # """
        #     DROP TABLE IF EXISTS movies CASCADE;
        #     DROP TABLE IF EXISTS genres CASCADE;
        #     DROP TABLE IF EXISTS movies_genres CASCADE;
        # """,
        """
        CREATE TABLE IF NOT EXISTS movies(
            movie_id SERIAL PRIMARY KEY UNIQUE,
            movie_api_id INTEGER UNIQUE,
            movie_original_title VARCHAR(255) NOT NULL,
            movie_french_title VARCHAR(255) NOT NULL,
            movie_original_language VARCHAR(255) NOT NULL,
            movie_img VARCHAR(255) NOT NULL,
            movie_description TEXT NOT NULL,
            movie_rating INTEGER,
            movie_year INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS genres (
            genre_id SERIAL PRIMARY KEY,
            genre_api_id INTEGER UNIQUE,
            genre_name VARCHAR(255)
        )
        """,
        """
        CREATE TABLE movies_genres (
            movie_id INTEGER NOT NULL,
            genre_id INTEGER NOT NULL,
            PRIMARY KEY (movie_id , genre_id),
            FOREIGN KEY (movie_id)
                REFERENCES movies (movie_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (genre_id)
                REFERENCES genres (genre_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Movies Database has been modified")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
