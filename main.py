# MovieDB Python V2
import os
from tkinter import *
from colors import COLORS

from Api import API

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
