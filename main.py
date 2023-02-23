# MovieDB Python V2
import os
from tkinter import *
from tkinter import ttk
import utils  # Module contenant les fonctions de l'application
import styles.ttk_styles as styles  # Module contenant les styles de l'application et des constantes de couleur

# Définir les couleurs et le style des boutons
bg = styles.bg
txt = styles.txt


# Créer l'interface utilisateur
class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True, fill=BOTH)

        # Créer un Frame en haut de la fenêtre pour la barre de recherche
        self.top_frame = Frame(self, bg=bg, height=50)
        self.top_frame.pack(side=TOP, fill=X)

        # Créer un Frame principal qui prendra le reste de l'écran pour afficher les résultats
        self.content_frame = Frame(self, bg=txt)
        self.content_frame.pack(side=TOP, fill=BOTH, expand=True)

        # Créer un Frame en pied de page pour les différents params
        self.bottom_frame = Frame(self, bg=bg, height=50)
        self.bottom_frame.pack(side=BOTTOM, fill=X)


# Créer une instance de l'application
app = App()
# Configurer la fenêtre principale
app.master.config(background=bg)
app.config(background=bg)
app.master.iconbitmap('@img/ico.xbm')
app.master.title("MovieDB v2.0")
app.master.geometry("800x600")  # Taille de la fenêtre à améliorer

# content_frame
# create a Text widget in content_frame
result_text = Text(app.content_frame, bg='white', fg=bg)
result_text.pack(side=TOP, fill=BOTH, expand=True)


# search button command
def search_command():
    results = utils.search(search_entry)
    # result_text.delete(1.0, END)  # affichage brut
    # result_text.insert(END, results)  # affichage brut
    # Supprimer les anciens widgets du content_frame
    for widget in app.content_frame.winfo_children():
        widget.destroy()

    # Créer le tableau
    table = ttk.Treeview(app.content_frame, columns=(1, 2, 3, 4), height=5, show="headings")
    table.heading(1, text="ID")
    table.column(1, width=20)
    table.heading(2, text="Titre")
    table.column(2, width=150, stretch=True)
    table.heading(3, text="Note")
    table.column(3, width=5)
    table.heading(4, text="-_-")
    table.column(4, width=50)
    app.content_frame.columnconfigure(2, weight=1)

    # Ajouter les résultats dans le tableau
    for result in results:
        table.insert('', END, values=(
            result['movie_api_id'], result['movie_french_title'], f"{result['movie_rating']} %",
            result['movie_poster']))

    # Afficher le tableau dans le content_frame
    table.pack(side=TOP, fill=BOTH, expand=True)


def search_detail_command():
    result = utils.detail(search_detail_entry)
    result_text.delete(1.0, END)
    result_text.insert(END, result)


# update button command
def update_command():
    utils.update_genres_table()
    update_button.configure(text="Mise a jour finis!", style='Finished.TButton')


def valider(event):
    print("Validation!")


# TOP_FRAME
# Ajouter une barre de recherche pour les films
search_label = Label(app.top_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_entry = Entry(app.top_frame)
# search_button = Button(app.top_frame, text="?", command=search_command)
search_button = ttk.Button(app.top_frame, text="?", style='Search.TButton', command=search_command)

search_button.pack(side=RIGHT, padx=5, pady=5)
search_entry.pack(side=RIGHT, padx=5, pady=5)
search_label.pack(side=RIGHT, padx=5)


# Ajouter une barre de recherche pour afficher les détails d'un film
# cette fonction est a rajouter dans le tableau de la liste des films rechercher
# search_detail_label = Label(app.top_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
# search_detail_entry = Entry(app.top_frame)
# search_detail_button = Button(app.top_frame, text="?", command=search_detail_command)
# search_detail_button.pack(side=LEFT, padx=5, pady=5)
# search_detail_entry.pack(side=LEFT, padx=5, pady=5)
# search_label.pack(side=LEFT, padx=5)

# CONTENT_FRAME


# BOTTOM_FRAME
# Ajouter un bouton pour mettre à jour la table des genres
update_button = ttk.Button(app.bottom_frame, text="Mettre à jour les genres", style='Custom.TButton',
                           command=update_command)
update_button.pack(side=LEFT, padx=5, pady=5)
exit_btn = ttk.Button(app.bottom_frame, text="X", style='Exit.TButton', command=quit)
exit_btn.pack(side=RIGHT)
# Lancer le programme
app.mainloop()
