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


def genre(genre_id_list):
    sql = '''SELECT genre_name FROM genres WHERE genre_id IN (%s)'''
    genres = []
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        for genre_id in genre_id_list:
            curs.execute(sql, genre_id)
            response = curs.fetchall()
            genres.append(response)
        connexion.commit()
        curs.close()
        print(genres)
        return genres
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def genres():
    connexion = None
    genres_list = []
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute('SELECT * FROM genres')
        response = curs.fetchall()
        for genre in response:
            genre_dict = {}
            genre_dict.update({'genre_id': genre[0]})
            genre_dict.update({'genre_api_id': genre[1]})
            genre_dict.update({'genre_name': genre[2]})
            genres_list.append(genre_dict)
        connexion.commit()
        curs.close()
        return genres_list
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    




def create_movie(movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year, genre_id_list):
    sql = """INSERT INTO movies(movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING movie_id"""

    sql_genre = """INSERT INTO movies_genres (movie_id, genre_id) VALUES(%s, %s)"""

    connexion = None
    movie_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year))
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
    sql = ''' SELECT * FROM movies '''
    movies_list = []
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute(sql)
        response = curs.fetchall()
        for movie in response:
            movie_dict = {}
            movie_dict.update({'movie_id': movie[0]})
            movie_dict.update({'movie_api_id': movie[1]})
            movie_dict.update({'movie_original_title': movie[2]})
            movie_dict.update({'movie_french_title': movie[3]})
            movie_dict.update({'movie_original_language': movie[4]})
            movie_dict.update({'movie_img': movie[5]})
            movie_dict.update({'movie_description': movie[6]})
            movie_dict.update({'movie_rating': movie[7]})
            movie_dict.update({'movie_year': movie[8]})
            genres = []
            for genre in movie_genres(str(movie[0])):
                genres.append(genre)
            movie_dict.update({'movie_genres': genres})           
            movies_list.append(movie_dict)
        connexion.commit()
        curs.close()
        print(movies_list)
        return movies_list
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def get_movie(movie_id):
    sql_movies = ''' SELECT * FROM movies WHERE movie_id = %s '''
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute(sql_movies, movie_id)
        resp = curs.fetchall()
        movie = {}
        movie.update({'movie_id': resp[0][0]})
        movie.update({'movie_api_id': resp[0][1]})
        movie.update({'movie_original_title': resp[0][2]})
        movie.update({'movie_french_title': resp[0][3]})
        movie.update({'movie_original_language': resp[0][4]})
        movie.update({'movie_img': resp[0][5]})
        movie.update({'movie_description': resp[0][6]})
        movie.update({'movie_rating': resp[0][7]})
        movie.update({'movie_year': resp[0][8]})
        genres = []
        for genre in movie_genres(str(resp[0][0])):
            genres.append(genre)
        movie.update({'movie_genres': genres})
        connexion.commit()
        curs.close()
        return movie
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def movie_genres(movie_id):
    sql_genre = ''' SELECT genres.genre_name FROM genres INNER JOIN movies_genres ON genres.genre_id = movies_genres.genre_id WHERE movies_genres.movie_id = %s'''
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute(sql_genre, movie_id)
        resp = curs.fetchall()
        connexion.commit()
        curs.close()
        return resp
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()

def update_movie(movie_id, movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year):
    # print(movie_id, movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year, genre_id_list)
    sql_movie = """ UPDATE movies SET movie_api_id = %s, movie_original_title = %s, movie_french_title = %s, movie_original_language = %s, movie_img = %s, movie_description = %s, movie_rating = %s, movie_year = %s WHERE movie_id = %s"""
    connexion = None
    update_rows = 0
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql_movie, (movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year, movie_id))
        update_rows = cursor.rowcount
        print("this movie is update")
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return update_rows

if __name__ == '__main__':
    pass
    # movie_genres('1')
    # get_movie('1')
    # movies()
    # create_movie('alien', 'alien le 8eme passager', 'usa', 'alien.png', 'un vaisseau, un alien et sigourney weather', 6, 1978, [('1',), ('3',), ('5',)])
    # genres()
    # genre([('4',), ('5',)])
    # delete_genre('4')
    # create_genre("Horror")
    # create_genres([('Horror',), ('Fantasy',), ('Action',), ('Comedy',), ('Sci-fy',)])
    # update_genre(14, 'Science-Fiction')
    # create_genres([('28','Action',), ('12','Adventure',), ('35','Comedy',), ('80','Crime',), ('99','Documentary',), ('18','Drama',), ('10751','Family',), ('14','Fantasy',), ('36','History',), ('27','Horror',), ('10402','Music',), ('9648','Mystery',), ('10749','Romance',), ('878','Science Fiction',), ('10770','TV Movie',), ('53','Thriller',), ('10752','War',), ('37','Western',)])

