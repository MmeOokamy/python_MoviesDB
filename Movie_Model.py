import psycopg2
from config import config


class Movie:

    def __init__(self, movie_orginal_title, movie_french_title, movie_origin, movie_img, movie_description,
                 movie_rating, movie_date, movie_category):
        self.movie_orginal_title = movie_orginal_title
        self.movie_french_title = movie_french_title
        self.movie_origin = movie_origin
        self.movie_img = movie_img
        self.movie_description = movie_description
        self.movie_rating = movie_rating
        self.movie_date = movie_date
        self.movie_category = movie_category

    # def insert_movie(self, movie_orginal_title, movie_french_title, movie_origin, movie_img,
    #                  movie_description, movie_rating, movie_date):
    #     """ insert a new movie into the movies table """
    #     sql = """INSERT INTO movies(movie_orginal_title, movie_french_title, movie_origin, movie_img,
    #     movie_description, movie_rating, movie_date) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING movie_id; """
    #     conn = None
    #     movie_id = None
    #     try:
    #         # read database configuration
    #         params = config()
    #         # connect to the PostgreSQL database
    #         conn = psycopg2.connect(**params)
    #         # create a new cursor
    #         cur = conn.cursor()
    #         # execute the INSERT statement
    #         cur.execute(sql, (movie_orginal_title, movie_french_title, movie_origin, movie_img, movie_description,
    #                           movie_rating, movie_date))
    #         # get the generated id back
    #         movie_id = cur.fetchone()[0]
    #         # commit the changes to the database
    #         conn.commit()
    #         # close communication with the database
    #         cur.close()
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print("error : " + str(error))
    #     finally:
    #         if conn is not None:
    #             conn.close()
    #
    #     return movie_id

#
# Movie.insert_movie(
#     None,
#     movie_orginal_title='The Fifth Element',
#     movie_french_title='Le Cinquième Élément',
#     movie_origin='anglais',
#     movie_img='8nx8sttha1Zidt73SbNncVfSwqk.jpg',
#     movie_description='New York, XXIIIème siècle. Une boule de feu fonce sur la Terre.',
#     movie_rating=4,
#     movie_date=None
# )
