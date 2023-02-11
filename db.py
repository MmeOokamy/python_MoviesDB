import sqlite3


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

    def get_data(self, table_name, fields, conditions=None):
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
        data = self.cursor.fetchall()
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
