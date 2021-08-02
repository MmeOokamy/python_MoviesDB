import psycopg2
from config import config


def create_genre(genre_api_id, genre_name):
    sql = """INSERT INTO genres(genre_api_id, genre_name) VALUES(%s, %s) RETURNING genre_id"""
    connexion = None
    genre_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (genre_api_id, genre_name,))
        genre_id = cursor.fetchone()[0]
        connexion.commit()
        print("it's commit, you are create a new genre")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return genre_id


def create_genres(genre_list):
    sql = """INSERT INTO genres(genre_api_id, genre_name) VALUES(%s, %s)"""
    connexion = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.executemany(sql, genre_list)
        connexion.commit()
        print("it's commit, you are create genres : " + str(genre_list))
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def update_genre(genre_id, new_genre_name):
    sql = """ UPDATE genres SET genre_name = %s WHERE genre_id = %s"""
    connexion = None
    update_rows = 0
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (new_genre_name, genre_id))
        update_rows = cursor.rowcount
        print("this genre is update")
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return update_rows


def delete_genre(genre_id):
    sql = """ DELETE FROM genres WHERE genre_id = %s"""
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, genre_id)
        print("this genre is delete")
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def genre(genre_id):
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute('SELECT * FROM genres where genre_id = %s', genre_id)
        response = curs.fetchall()
        for r in response:
            print(r)
        connexion.commit()
        curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def genres():
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute('SELECT * FROM genres')
        response = curs.fetchall()
        for r in response:
            print(r)
        connexion.commit()
        curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()



def create_movie_alone(movie_api_id, movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date):
    sql_movie = """INSERT INTO movies(movie_api_id, movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING movie_id"""
    connexion = None
    movie_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql_movie, (movie_api_id, movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date))
        movie_id = cursor.fetchone()[0]
        connexion.commit()
        print("it's commit, you are create an Movie")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return movie_id


def create_movie(movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date, genre_id_list):
    sql = """INSERT INTO movies( movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING movie_id"""

    sql_genre = """INSERT INTO movies_genres (movie_id, genre_id) VALUES(%s, %s)"""

    connexion = None
    movie_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date))
        movie_id = cursor.fetchone()[0]

        for cat_id in genre_id_list:
             cursor.execute(sql_genre, (movie_id, cat_id))

        connexion.commit()
        print("it's commit, you are create an Movie")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def movies():
    sql = '''
        SELECT movies.movie_id, movies.movie_original_title, genres.genre_name
        FROM movies
        INNER JOIN movies_genres
        ON movies.movie_id = movies_genres.movie_id
        INNER JOIN genres
        ON movies_genres.genre_ID = genres.genre_id
        '''

    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute(sql)
        response = curs.fetchall()
        for r in response:
            print(r)
        connexion.commit()
        curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def movie(movie_id):
    sql = '''
        SELECT movies.movie_id, movies.movie_original_title, genres.genre_name 
        FROM movies
        INNER JOIN movies_genres
        ON movies.movie_id = movies_genres.movie_id
        INNER JOIN genres
        ON movies_genres.genre_ID = genres.genre_id
        WHERE movies.movie_id = %s
        '''

    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute(sql, movie_id)
        response = curs.fetchall()
        for r in response:
            print(r)
        connexion.commit()
        curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()



if __name__ == '__main__':
    pass
    # movie('1')
    # movies()
    # create_movie('alien', 'alien le 8eme passager', 'usa', 'alien.png', 'un vaisseau, un alien et sigourney weather', 6, 1978, [('1',), ('3',), ('5',)])
    # genres()
    # genre('3')
    # delete_genre('4')
    # create_genre("Horror")
    # create_genres([('Horror',), ('Fantasy',), ('Action',), ('Comedy',), ('Sci-fy',)])
    # update_genre(1, 'Action')
    # create_genres([('28','Action',), ('12','Adventure',), ('35','Comedy',), ('80','Crime',), ('99','Documentary',), ('18','Drama',), ('10751','Family',), ('14','Fantasy',), ('36','History',), ('27','Horror',), ('10402','Music',), ('9648','Mystery',), ('10749','Romance',), ('878','Science Fiction',), ('10770','TV Movie',), ('53','Thriller',), ('10752','War',), ('37','Western',)])

