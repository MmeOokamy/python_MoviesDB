import requests
from api import get_api_movies_list
from crud import create_movie, get_movie, movies, genres
import psycopg2
from tkinter import ttk, messagebox
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk


BG_COLOR = "#F83A00"
CONTENT_BG_COLOR = '#FF754A'
TXT_COLOR = "white"
TITLE_COLOR = "black"

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

def add_movie():
    movie_api_id = movie_api_id_entry.get()
    movie_original_title = movie_original_title_entry.get()
    movie_french_title = movie_french_title_entry.get()
    movie_original_language = movie_original_language_entry.get()
    movie_img = movie_img_entry.get()
    movie_description = movie_description_entry.get()
    movie_rating = movie_rating_entry.get()
    movie_year = movie_year_entry.get()

    # MULTI SELECTION 
    genres_id_tuple = []
    genres_id_list = genres_list.selection()
    for id in genres_id_list:
        item_row = genres_list.item(id)
        # print(item_row['values'][0])
        genres_id_tuple.append(item_row['values'][0])
    
    movies_list = genres_id_tuple
    create_movie(movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year, movies_list)

def read_movie():
    if len(movies_list.selection()) == 1:
        # One item selected
        item_dict = movies_list.item(movies_list.selection())
        id = str(item_dict['values'][0])
        film = get_movie(id)
        print(film)
        image_api = 'https://image.tmdb.org/t/p/w500' + film['movie_img']
        resp_img = requests.get(image_api)
        if resp_img.status_code==200: 
            img_data = resp_img.content
        
        toplevel = Toplevel(formApp, bg=BG_COLOR)
        toplevel.title(film['movie_original_title'])

        left_frame = Frame(toplevel, bg=BG_COLOR)
        right_frame = Frame(toplevel, bg=BG_COLOR, width=200)
        poster = Image.open(BytesIO(img_data))
        
        new_height = poster.height/2
        new_width = poster.width/2
        poster = poster.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(poster)

        label = Label(left_frame,image=img, bg=BG_COLOR)
        label.image = img 
        label.pack(expand=True)

        toplevel_id_label = Label(right_frame, text='id movie', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')
        toplevel_api_id_label = Label(right_frame, text='id movie api', bg=BG_COLOR, fg=TITLE_COLOR,  anchor='w')
        toplevel_original_title_label = Label(right_frame, text='Titre Original', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')
        toplevel_french_title_label = Label(right_frame, text='Titre Français', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')
        toplevel_original_language_label = Label(right_frame, text='Original Language', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')
        toplevel_description_label = Label(right_frame, text='Description', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')
        toplevel_rating_label = Label(right_frame, text='Note', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')
        toplevel_year_label = Label(right_frame, text='Année', bg=BG_COLOR, fg=TITLE_COLOR, anchor='w')

        movie_db_id_label = Label(right_frame, text=film['movie_id'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')
        movie_db_api_id_label = Label(right_frame, text=film['movie_api_id'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')
        movie_db_original_title_label = Label(right_frame, text=film['movie_original_title'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')
        movie_db_french_title_label = Label(right_frame, text=film['movie_french_title'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')
        movie_db_original_language_label = Label(right_frame, text=film['movie_original_language'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')
        movie_db_description_label = Text(right_frame, bg=BG_COLOR, fg=TXT_COLOR, height=4, borderwidth=0, highlightthickness=0)
        movie_db_description_label.insert(1.0, film['movie_description'])
        movie_db_rating_label = Label(right_frame, text=film['movie_rating'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')
        movie_db_year_label = Label(right_frame, text=film['movie_year'], bg=BG_COLOR, fg=TXT_COLOR, anchor='w')

        toplevel_id_label.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        toplevel_api_id_label.grid(row=1, column=0, padx=2, pady=2, sticky=W)
        toplevel_original_title_label.grid(row=2, column=0, padx=2, pady=2, sticky=W)
        toplevel_french_title_label.grid(row=3, column=0, padx=2, pady=2, sticky=W)
        toplevel_original_language_label.grid(row=4, column=0, padx=2, pady=2, sticky=W)
        toplevel_description_label.grid(row=5, column=0, padx=2, pady=2, sticky=W)
        toplevel_rating_label.grid(row=6, column=0, padx=2, pady=2, sticky=W)
        toplevel_year_label.grid(row=7, column=0, padx=2, pady=2, sticky=W)

        movie_db_id_label.grid(row=0, column=1, padx=2, pady=2, sticky=W)
        movie_db_api_id_label.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        movie_db_original_title_label.grid(row=2, column=1, padx=2, pady=2, sticky=W)
        movie_db_french_title_label.grid(row=3, column=1, padx=2, pady=2, sticky=W)
        movie_db_original_language_label.grid(row=4, column=1, padx=2, pady=2, sticky=W)
        movie_db_description_label.grid(row=5, column=1, padx=2, pady=2, sticky=W)
        movie_db_rating_label.grid(row=6, column=1, padx=2, pady=2, sticky=W)
        movie_db_year_label.grid(row=7, column=1, padx=2, pady=2, sticky=W)

        left_frame.pack(side=LEFT)
        right_frame.pack(side=RIGHT, expand=False)
    else:
        messagebox.showinfo('Information', "Veuillez Selectionner un Film")
        print(len(movies_list.selection()))
    

# create the application
formApp = App()

#
# here are method calls to the window manager class
#
formApp.master.config(background=BG_COLOR)
formApp.config(background=BG_COLOR)
formApp.master.title("MILV")
formApp.master.geometry("1000x400")

# Style
style = ttk.Style(formApp)
# style.theme_use("clam") # if i used this theme i can't change border of treeview
style.configure("Treeview", background=CONTENT_BG_COLOR, fieldbackground=CONTENT_BG_COLOR, foreground=TITLE_COLOR,  borderwidth=0, bordercolor=BG_COLOR)


# Frame
movies_left_frame = Frame(formApp, bg=BG_COLOR)
movies_left_frame.configure(padx=10)
movies_right_frame = Frame(formApp, bg=BG_COLOR)

""" MOVIES RIGHT FRAME """

# Treeview
movies_list = ttk.Treeview(movies_left_frame, columns=(1,2), height=10, show="headings")
movies_list.heading(1, text="ID")
movies_list.heading(2, text="Title")
movies_list.column(1, width=25)
movies_list.column(2, width=250)

movies_list_db = movies()
for movie in movies_list_db:
    id = movie['movie_id']
    name = movie['movie_name']
    movies_list.insert('', END, values=(id, name))

# BTN
read_btn = Button(movies_left_frame, text='Read More', justify=CENTER, command=read_movie)


""" MOVIES RIGHT FRAME """

# Label
movie_api_id_label = Label(movies_right_frame, text='id movie api', bg=BG_COLOR, fg=TITLE_COLOR)
movie_original_title_label = Label(movies_right_frame, text='Titre Original', bg=BG_COLOR, fg=TITLE_COLOR)
movie_french_title_label = Label(movies_right_frame, text='Titre Français', bg=BG_COLOR, fg=TITLE_COLOR)
movie_original_language_label = Label(movies_right_frame, text='Original Language', bg=BG_COLOR, fg=TITLE_COLOR)
movie_img_label = Label(movies_right_frame, text='Image', bg=BG_COLOR, fg=TITLE_COLOR)
movie_description_label = Label(movies_right_frame, text='Description', bg=BG_COLOR, fg=TITLE_COLOR)
movie_rating_label = Label(movies_right_frame, text='Note', bg=BG_COLOR, fg=TITLE_COLOR)
movie_year_label = Label(movies_right_frame, text='Année', bg=BG_COLOR, fg=TITLE_COLOR)

# Entry
movie_api_id_entry = Entry(movies_right_frame)
movie_original_title_entry = Entry(movies_right_frame)
movie_french_title_entry = Entry(movies_right_frame)
movie_original_language_entry = Entry(movies_right_frame)
movie_img_entry = Entry(movies_right_frame)
movie_description_entry = Entry(movies_right_frame)
movie_rating_entry = Entry(movies_right_frame)
movie_year_entry = Entry(movies_right_frame)

# multi selected list of genres =D
genres_list = ttk.Treeview(movies_right_frame, columns=(1, 2), height=10, show="headings")
genres_list.heading(1, text="ID")
genres_list.heading(2, text="Name")
genres_list.column(1, width=25)
genres_list.column(2, width=100)

genres_list_db = genres()
for genre in genres_list_db:
    id = genre['genre_id']
    name = genre['genre_name']
    genres_list.insert('', END, values=(id, name))


# BTN
save_btn = Button(movies_right_frame, text='Save', justify=CENTER, command=add_movie)
exit_btn = Button(movies_right_frame, text="EXIT", justify=CENTER, command=quit)


""" MOVIES LEFT FRAME Pack, grid, place """
movies_list.pack()
read_btn.pack(side=BOTTOM)


""" MOVIES RIGHT FRAME Pack, grid, place """
# Label
movie_original_title_label.grid(row=0, column=0, padx=2, pady=2)
movie_french_title_label.grid(row=1, column=0, padx=2, pady=2)
movie_original_language_label.grid(row=2, column=0, padx=2, pady=2)
movie_img_label.grid(row=3, column=0, padx=2, pady=2)
movie_description_label.grid(row=4, column=0, padx=2, pady=2)
movie_rating_label.grid(row=5, column=0, padx=2, pady=2)
movie_year_label.grid(row=6, column=0, padx=2, pady=2)
movie_api_id_label.grid(row=7, column=0, padx=2, pady=2)

# Entry
movie_original_title_entry.grid(row=0, column=1, padx=2, pady=2)
movie_french_title_entry.grid(row=1, column=1, padx=2, pady=2)
movie_original_language_entry.grid(row=2, column=1, padx=2, pady=2)
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

"""" FRAME """
movies_right_frame.pack(side=RIGHT)
movies_left_frame.pack(fill=BOTH, expand=True,side=LEFT)

# start the program
formApp.mainloop()
