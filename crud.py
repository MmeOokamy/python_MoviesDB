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
    pass


def categories():
    pass


if __name__ == '__main__':
    pass
    # delete_category('4')
    # create_category("Action")
    # create_categories([('Horror',), ('Fantasy',)])
    # update_category(1, 'Action')
