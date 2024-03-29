import sqlite3
import os


class Database:
    """
    Cette classe représente une base de données SQLite. Elle fournit des méthodes pour créer des tables, ajouter des
    données, récupérer des données, mettre à jour des données et supprimer des données.
    """

    def __init__(self):
        """
        Cette méthode initialise une nouvelle connexion à la base de données SQLite, en utilisant le nom de fichier
        "movies.db". Elle crée également un curseur qui sera utilisé pour exécuter des requêtes sur la base de données.
        """
        # Vérifier si le fichier de la base de données existe
        if not os.path.isfile("movies.db"):
            # Si le fichier de la base de données n'existe pas, le créer et initialiser les tables
            self.conn = sqlite3.connect("movies.db")
            self.cursor = self.conn.cursor()
            self.db_init()
        else:
             # Si le fichier de la base de données existe, ouvrir la connexion à la base de données
            self.conn = sqlite3.connect("movies.db")
            self.cursor = self.conn.cursor()

       

    def create_table(self, table_name, fields):
        """
        Cette méthode prend en entrée le nom de la table (table_name) et la définition des champs de la table (
        fields). La définition des champs est une chaîne de caractères qui décrit les noms et les types des colonnes
        de la table.
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        self.cursor.execute(query)
        self.conn.commit()

    def add_data(self, table_name, fields, values):
        """
        Cette méthode prend en entrée le nom de la table où les données doivent être ajoutées, les noms des champs et
        les valeurs à ajouter. La méthode crée une requête SQL qui insère les valeurs spécifiées dans les champs
        spécifiés de la table, et utilise la méthode execute pour exécuter la requête sur la base de données. Enfin,
        la méthode utilise commit pour enregistrer les modifications sur la base de données.
        """
        placeholders = ', '.join('?' * len(values))
        query = f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_data(self, table_name, fields, conditions=None, fetchall=True):
        """
        Cette méthode prend en entrée le nom de la table, les champs à récupérer et une condition facultative pour
        filtrer les données. La méthode construit une requête SQL qui sélectionne les champs spécifiés de la table,
        et utilise la méthode execute pour exécuter la requête sur la base de données. Enfin, la méthode utilise
        fetchall pour récupérer les lignes sélectionnées et les retourne.
        """
        query = f"SELECT {fields} FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        if fetchall:
            data = self.cursor.fetchall()
        else:
            data = self.cursor.fetchone()
        return data

    def update_data(self, table_name, fields, values, conditions):
        """
        Cette méthode prend en entrée le nom de la table, les champs à mettre à jour (sous forme de liste),
        les nouvelles valeurs (sous forme de liste), ainsi que les conditions pour identifier les enregistrements à
        mettre à jour. Les champs et les valeurs sont liés ensemble à l'aide de la syntaxe field=?, et tous les
        paramètres sont passés à la méthode execute via une liste de valeurs.
        """
        placeholders = ', '.join([f"{field}=?" for field in fields])
        query = f"UPDATE {table_name} SET {placeholders} WHERE {conditions}"
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_data(self, table_name, conditions):
        """
        Cette méthode prend en entrée le nom de la table et les conditions pour sélectionner les données à supprimer.
        La requête SQL DELETE est utilisée pour supprimer les données sélectionnées. Assurez-vous de faire un commit
        après avoir exécuté la requête pour enregistrer les modifications.
        """
        query = f"DELETE FROM {table_name} WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        """
        Cette méthode permet de fermer la connexion à la base de données. Elle utilise la méthode close de l'objet de
        connexion pour fermer la connexion. Il est important de fermer la connexion lorsque vous avez terminé
        d'interagir avec la base de données, pour libérer les ressources système utilisées par la connexion.
        """
        self.conn.close()
        
    def db_init(self):
        table_name = "movies"
        fields = """
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_api_id INTEGER UNIQUE NOT NULL,
                    movie_original_title VARCHAR(255) NOT NULL,
                    movie_french_title VARCHAR(255),
                    movie_original_language VARCHAR(255),
                    movie_poster VARCHAR(255),
                    movie_backdrop VARCHAR(255),
                    movie_description TEXT,
                    movie_tagline TEXT,
                    movie_rating INTEGER DEFAULT 0 CHECK (movie_rating BETWEEN 0 AND 100),
                    movie_release_date DATE DEFAULT '1895-12-28' CHECK (movie_release_date >= '1895-12-28')
                """
        self.create_table(table_name, fields)

        # create genres table
        table_name = "genres"
        fields = """
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre_api_id INTEGER UNIQUE NOT NULL,
                    genre_name VARCHAR(255) NOT NULL
                """
        self.create_table(table_name, fields)

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
        self.create_table(table_name, fields)
