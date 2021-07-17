import psycopg2
from config import config


class Category:

    def __init__(self, name, category_description):
        self.name = name
        self.category_description = category_description


# def create_category(category_description):
#     sql = """INSERT INTO categories(category_description) VALUES(%s) RETURNING category_id"""
#     connexion = None
#     category_id = None
#
#     try:
#         params = config()
#         connexion = psycopg2.connect(**params)
#         cursor = connexion.cursor()
#         cursor.execute(sql, (category_description,))
#         category_id = cursor.fetchone()[0]
#         connexion.commit()
#         print("it's commit")
#         cursor.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("error : " + str(error))
#     finally:
#         if connexion is not None:
#             connexion.close()
#     return category_id
#
#
# create_category(category_description="Fantasy")
