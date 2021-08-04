from api import get_api_movies_list
from crud import *
import psycopg2
from tkinter import ttk
from tkinter import *

BG_COLOR = "#F83A00"
CONTENT_BG_COLOR = '#FF754A'
TXT_COLOR = "white"
TITLE_COLOR = "black"

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

def create_movie():
    movie_api_id = movie_api_id_entry.get()
    movie_original_title = movie_original_title_entry.get()
    movie_french_title = movie_french_title_entry.get()
    movie_origin = movie_origin_entry.get()
    movie_img = movie_img_entry.get()
    movie_description = movie_description_entry.get()
    movie_rating = movie_rating_entry.get()
    movie_year = movie_year_entry.get()

    create_movie_alone(movie_api_id, movie_original_title, movie_french_title, movie_origin,movie_img, movie_description, movie_rating, movie_year)



# create the application
app = App()

#
# here are method calls to the window manager class
#
app.master.config(background=BG_COLOR)
app.config(background=BG_COLOR)
app.master.title("MILV")
app.master.geometry("1000x400")


# label
movie_api_id_label = Label(app, text='id movie api', bg=BG_COLOR, fg=TITLE_COLOR)
movie_original_title_label = Label(app, text='Titre Original', bg=BG_COLOR, fg=TITLE_COLOR)
movie_french_title_label = Label(app, text='Titre Français', bg=BG_COLOR, fg=TITLE_COLOR)
movie_origin_label = Label(app, text='Origine', bg=BG_COLOR, fg=TITLE_COLOR)
movie_img_label = Label(app, text='Image', bg=BG_COLOR, fg=TITLE_COLOR)
movie_description_label = Label(app, text='Description', bg=BG_COLOR, fg=TITLE_COLOR)
movie_rating_label = Label(app, text='Note', bg=BG_COLOR, fg=TITLE_COLOR)
movie_year_label = Label(app, text='Année', bg=BG_COLOR, fg=TITLE_COLOR)

# Entry
movie_api_id_entry = Entry(app)
movie_original_title_entry = Entry(app)
movie_french_title_entry = Entry(app)
movie_origin_entry = Entry(app)
movie_img_entry = Entry(app)
movie_description_entry = Entry(app)
movie_rating_entry = Entry(app)
movie_year_entry = Entry(app)

# multi selected list of genres =D
genres_list = ttk.Treeview(app, columns=(1, 2), height=10, show="headings")
genres_list.heading(1, text="ID")
genres_list.heading(2, text="Name")
genres_list.column(1, width=50)
genres_list.column(2, width=150)

genres_list_db = genres()
for genre in genres_list_db:
    id = genre['genre_id']
    name = genre['genre_name']
    genres_list.insert('', END, values=(id, name))


# BTN
save_btn = Button(app, text='Save', justify=CENTER, command=create_movie)
exit_btn = Button(app, text="EXIT", justify=CENTER, command=quit)

# Pack, grid, place
movie_original_title_label.grid(row=0, column=0, padx=2, pady=2)
movie_french_title_label.grid(row=1, column=0, padx=2, pady=2)
movie_origin_label.grid(row=2, column=0, padx=2, pady=2)
movie_img_label.grid(row=3, column=0, padx=2, pady=2)
movie_description_label.grid(row=4, column=0, padx=2, pady=2)
movie_rating_label.grid(row=5, column=0, padx=2, pady=2)
movie_year_label.grid(row=6, column=0, padx=2, pady=2)
movie_api_id_label.grid(row=7, column=0, padx=2, pady=2)

# Entry
movie_original_title_entry.grid(row=0, column=1, padx=2, pady=2)
movie_french_title_entry.grid(row=1, column=1, padx=2, pady=2)
movie_origin_entry.grid(row=2, column=1, padx=2, pady=2)
movie_img_entry.grid(row=3, column=1, padx=2, pady=2)
movie_description_entry.grid(row=4, column=1, padx=2, pady=2)
movie_rating_entry.grid(row=5, column=1, padx=2, pady=2)
movie_year_entry.grid(row=6, column=1, padx=2, pady=2)
movie_api_id_entry.grid(row=7, column=1, padx=2, pady=2)

# multi selected list of genres =D
genres_list.grid(row=0, column=3, rowspan=8)

# btn
save_btn.grid(row=8, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)
exit_btn.grid(row=9, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)

# start the program
app.mainloop()
