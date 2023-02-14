# MovieDB Python V2
import os
from tkinter import *
from colors import COLORS

import utils


bg = COLORS['dark_blue']
txt = COLORS['w']


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
update_button = Button(app.top_frame, text="Mettre à jour les genres", command=utils.update_genres_table)
update_button.pack(side=LEFT, padx=5, pady=5)
# movies
search_label = Label(app.top_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_entry = Entry(app.top_frame)
search_button = Button(app.top_frame, text="?", command=lambda: utils.search(search_entry))
search_button.pack(side=RIGHT, padx=5, pady=5)
search_entry.pack(side=RIGHT, padx=5, pady=5)
search_label.pack(side=RIGHT, padx=5)

search_detail_label = Label(app.content_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_detail_entry = Entry(app.content_frame)
search_detail_button = Button(app.content_frame, text="?", command=lambda:utils.detail(search_detail_entry))
search_detail_button.pack(side=RIGHT, padx=5, pady=5)
search_detail_entry.pack(side=RIGHT, padx=5, pady=5)
search_label.pack(side=RIGHT, padx=5)

# start the program
app.mainloop()
