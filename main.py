# MovieDB Python V2
import os
from tkinter import *
from tkinter import ttk
import utils # Module contenant les fonctions de l'application
import ttk_styles as styles  # Module contenant les styles de l'application et des constantes de couleur

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
        
        # Créer un Frame principal qui prendra le reste de l'écran pour afficher les résultatsn
        self.content_frame = Frame(self, bg=txt)
        self.content_frame.pack(side=TOP, fill=BOTH, expand=True)
        

# Créer une instance de l'application
app = App()
# Configurer la fenêtre principale
app.master.config(background=bg)
app.config(background=bg)
app.master.iconbitmap('@img/ico.xbm')
app.master.title("MovieDB v2.0")
app.master.geometry("600x400")  # Taille de la fenêtre à améliorer


# content_frame
# create a Text widget in content_frame
result_text = Text(app.content_frame, bg='white', fg=bg)
result_text.pack(side=TOP, fill=BOTH, expand=True)
# search button command
def search_command():
    result = utils.search(search_entry)
    result_text.delete(1.0, END)
    result_text.insert(END, result)
    
def search_detail_command():
    result = utils.detail(search_detail_entry)
    result_text.delete(1.0, END)
    result_text.insert(END, result)
    
# update button command
def update_command():
    utils.update_genres_table()
    update_button.configure(text="Mise a jour finis!", style='Finished.TButton')


# Ajouter un bouton pour mettre à jour la table des genres
# update_button = ttk.Button(app.top_frame, text="Mettre à jour les genres", style='Custom.TButton', command=update_command)
# # update_button = ttk.Button(app.top_frame, text="Mettre à jour les genres", style='Custom.TButton', command=utils.update_genres_table)
# # update_button = Button(app.top_frame, text="Mettre à jour les genres", command=utils.update_genres_table)
# update_button.pack(side=LEFT, padx=5, pady=5)

# Ajouter une barre de recherche pour les films
search_label = Label(app.top_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_entry = Entry(app.top_frame)
search_button = Button(app.top_frame, text="?", command=search_command)
# search_button = Button(app.top_frame, text="?", command=lambda: utils.search(search_entry))
search_button.pack(side=RIGHT, padx=5, pady=5)
search_entry.pack(side=RIGHT, padx=5, pady=5)
search_label.pack(side=RIGHT, padx=5)


# Ajouter une barre de recherche pour afficher les détails d'un film
search_detail_label = Label(app.top_frame, text="MDB, est ce que tu connais :", bg=bg, fg=txt)
search_detail_entry = Entry(app.top_frame)
search_detail_button = Button(app.top_frame, text="?", command=search_detail_command)
search_detail_button.pack(side=LEFT, padx=5, pady=5)
search_detail_entry.pack(side=LEFT, padx=5, pady=5)
search_label.pack(side=LEFT, padx=5)

# Lancer le programme
app.mainloop()
