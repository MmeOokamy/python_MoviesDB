import psycopg2
from config import config


def create_category(category_description):
    sql = """INSERT INTO categories(category_description) VALUES(%s) RETURNING category_id"""
    connexion = None
    category_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (category_description,))
        category_id = cursor.fetchone()[0]
        connexion.commit()
        print("it's commit, you are create an Category")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return category_id


def create_categories(category_list):
    sql = """INSERT INTO categories(category_description) VALUES(%s)"""
    connexion = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.executemany(sql, category_list)
        connexion.commit()
        print("it's commit, you are create Categories : " + str(category_list))
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def update_category(category_id, new_category_description):
    sql = """ UPDATE categories SET category_description = %s WHERE category_id = %s"""
    connexion = None
    update_rows = 0
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (new_category_description, category_id))
        update_rows = cursor.rowcount
        print("this category is update")
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()
    return update_rows


def delete_category(category_id):
    sql = """ DELETE FROM categories WHERE category_id = %s"""
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, category_id)
        print("this category is delete")
        connexion.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error : " + str(error))
    finally:
        if connexion is not None:
            connexion.close()


def category(category_id):
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute('SELECT * FROM categories where category_id = %s', category_id)
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


def categories():
    connexion = None
    try:
        params = config()
        connexion = psycopg2.connect(**params)
        curs = connexion.cursor()
        curs.execute('SELECT * FROM categories')
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



def create_movie_alone(movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date):
    sql_movie = """INSERT INTO movies( movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING movie_id"""
    connexion = None
    movie_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql_movie, (movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date))
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


def create_movie(movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date, category_id_list):
    sql = """INSERT INTO movies( movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING movie_id"""

    sql_category = """INSERT INTO movies_categories (movie_id, category_id) VALUES(%s, %s)"""

    connexion = None
    movie_id = None

    try:
        params = config()
        connexion = psycopg2.connect(**params)
        cursor = connexion.cursor()
        cursor.execute(sql, (movie_original_title, movie_french_title, movie_origin, movie_img, movie_description, movie_rating, movie_date))
        movie_id = cursor.fetchone()[0]

        for cat_id in category_id_list:
             cursor.execute(sql_category, (movie_id, cat_id))

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
        SELECT movies.movie_id, movies.movie_original_title, categories.category_description 
        FROM movies
        INNER JOIN movies_categories
        ON movies.movie_id = movies_categories.movie_id
        INNER JOIN categories
        ON movies_categories.category_ID = categories.category_id
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
        SELECT movies.movie_id, movies.movie_original_title, categories.category_description 
        FROM movies
        INNER JOIN movies_categories
        ON movies.movie_id = movies_categories.movie_id
        INNER JOIN categories
        ON movies_categories.category_ID = categories.category_id
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
    # pass
    movie('1')
    # movies()
    # create_movie('alien', 'alien le 8eme passager', 'usa', 'alien.png', 'un vaisseau, un alien et sigourney weather', 6, 1978, [('1',), ('3',), ('5',)])
    # categories()
    # category('3')
    # delete_category('4')
    # create_category("Horror")
    # create_categories([('Horror',), ('Fantasy',), ('Action',), ('Comedy',), ('Sci-fy',)])
    # update_category(1, 'Action')

