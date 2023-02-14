-- # Structure de la base de donnée pour sqlite3
CREATE TABLE IF NOT EXISTS "movies" (
	"id"	INTEGER,
	"movie_api_id"	INTEGER NOT NULL UNIQUE,
	"movie_original_title"	VARCHAR(255) NOT NULL,
	"movie_french_title"	VARCHAR(255),
	"movie_original_language"	VARCHAR(255),
	"movie_img"	VARCHAR(255),
	"movie_description"	TEXT,
	"movie_rating"	INTEGER DEFAULT 0 CHECK("movie_rating" BETWEEN 0 AND 100),
	"movie_year"	INTEGER DEFAULT 1895 CHECK("movie_year" >= 1895),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "genres" (
	"id"	INTEGER,
	"genre_api_id"	INTEGER NOT NULL UNIQUE,
	"genre_name"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "movies_genres" (
	"movie_id"	INTEGER NOT NULL,
	"genre_id"	INTEGER NOT NULL,
	FOREIGN KEY("movie_id") REFERENCES "movies"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("genre_id") REFERENCES "genres"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("movie_id","genre_id")
);



# Voici la table `genres`
CREATE TABLE IF NOT EXISTS "genres" (
	"id"	INTEGER,
	"genre_api_id"	INTEGER NOT NULL UNIQUE,
	"genre_name"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

# class Database qui fait le lien entre la base de donnée et l'application:
class Database:

    def __init__(self):
        self.conn = sqlite3.connect("movies.db")
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, fields):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        self.cursor.execute(query)
        self.conn.commit()

    def add_data(self, table_name, fields, values):
        placeholders = ', '.join('?' * len(values))
        query = f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_data(self, table_name, fields, conditions=None):
        query = f"SELECT {fields} FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def update_data(self, table_name, fields, values, conditions):
        placeholders = ', '.join([f"{field}=?" for field in fields])
        query = f"UPDATE {table_name} SET {placeholders} WHERE {conditions}"
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_data(self, table_name, conditions):
        query = f"DELETE FROM {table_name} WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


# model / class en python
class Genre:
    def __init__(self, genre_api_id: int, id=None, genre_name: str = None):
        self.db = Database()
        self.id = id
        self.genre_api_id = genre_api_id
        self.genre_name = genre_name

    def __str__(self):
        return self.genre_name


    def exist(self):
        data = self.db.get_data("genres", "*", f"genre_api_id={self.genre_api_id}")
        return True if data else False
    
    def save(self):
        if self.id is None:
            data = self.db.get_data("genres", "*", f"genre_api_id={self.genre_api_id}")
            if data:
                self.id = data[0][0]
                self.db.update_data(
                    "genres", ["genre_name"], [self.genre_name], f"id={self.id}"
                )
            else:
                self.db.add_data(
                    "genres",
                    "genre_api_id, genre_name",
                    (self.genre_api_id, self.genre_name),
                )
                self.id = self.db.cursor.lastrowid
        else:
            self.db.update_data(
                "genres",
                ["genre_api_id", "genre_name"],
                [self.genre_api_id, self.genre_name],
                f"id={self.id}",
            )

    def delete(self):
        if self.id is not None:
            self.db.delete_data("genres", f"id={self.id}")
            self.id = None

# voila la fonctionpour appeler la list des genres depuis l'api
def get_genres(self):
	# utilise pour mettre a jour la liste des genres en base
	response = requests.get(
		f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language={self.language}"
	)
	if response.status_code == 200:
		genres = response.json()
		return genres['genres']


le contexte: c'est une application python tkinter, qui utilise une api.

je voudrais faire une fonction qui met a jour la table `genres` avec la liste 
des genres qui retourne l'api en utilisant la fonction `get_genres` pour recupérer la liste des genres puis verifier si le genre est deja présent dans la table `genres` avec la methode `Genre.exist()`. puis sauvegarder ou non en fonction de la reponse.
Tu peux m'aider?



ok alors ce qui suit est le fichier main.py.
c'est dans ce fichier quon créer l'interface utilisateur, quel est ton avis ?

import os
from tkinter import *
from colors import COLORS

from Api import API
from models import Genre, Movie

api = API()

bg = COLORS['dark_blue']
txt = COLORS['w']


def detail():
    mdb_id = search_detail_entry.get()
    movie = api.get_movie(mdb_id)
    if movie:
        print(movie)
    else:
        print("Connais pô!")


def search():
    entry = search_entry.get()
    movies = api.search_movies(entry)
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("Connais pô!")

def update_genres_table():
    db = Database()
    # appele l'api des genres et met a jour la bdd.
    genres = api.get_genres()
    for genre in genres:
        genre_obj = Genre(genre['id'], None, genre['name'])
        if not genre_obj.exist():
            genre_obj.save()
    db.close_connection()
            

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill=BOTH)

        # Créer un Frame en haut de la fenêtre
        self.top_frame = Frame(self, bg=bg, height=50)
        self.top_frame.pack(side=TOP, fill=X)

        # Créer un Frame principal qui prendra le reste de l'écran
        self.content_frame = Frame(self, bg='white')
        self.content_frame.pack(side=TOP, fill=BOTH, expand=True)


app = App()
app.master.config(background=bg)
app.config(background=bg)
app.master.iconbitmap('@img/ico.xbm')
app.master.title("MovieDB v2.0")
app.master.geometry("600x400")  # taille a amélioré

# top frame avec la recherche
# movies
search_button = Button(app.top_frame, text="?", command=search)
search_button.pack(side=RIGHT, padx=5, pady=5)
search_entry = Entry(app.top_frame)
search_entry.pack(side=RIGHT, padx=5, pady=5)
search_label = Label(app.top_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_label.pack(side=RIGHT, padx=5)

search_detail_button = Button(app.content_frame, text="?", command=detail)
search_detail_button.pack(side=RIGHT, padx=5, pady=5)
search_detail_entry = Entry(app.content_frame)
search_detail_entry.pack(side=RIGHT, padx=5, pady=5)
search_detail_label = Label(app.content_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_label.pack(side=RIGHT, padx=5)

# start the program
app.mainloop()
