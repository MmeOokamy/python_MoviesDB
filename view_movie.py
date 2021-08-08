from Movie import Movie
from crud import movies
from tkinter import ttk, messagebox
from tkinter import *


BG_COLOR = "#F83A00"
CONTENT_BG_COLOR = '#FF754A'
TXT_COLOR = "white"
TITLE_COLOR = "black"

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
formApp = App()

#
# here are method calls to the window manager class
#
formApp.master.config(background=BG_COLOR)
formApp.config(background=BG_COLOR)
formApp.master.title("MILV")
formApp.master.geometry("1000x500")

movies = movies()


# Frame
movies_left_frame = LabelFrame(formApp, bg=BG_COLOR, text="My Favorite Movies")

movies_right_frame = Frame(formApp, bg=BG_COLOR)

for movie in movies:
   print(movie)
   film = Movie(movie['movie_id'], movie['movie_api_id'], movie['movie_original_title'], movie['movie_french_title'], movie['movie_original_language'], movie['movie_img'], movie['movie_description'], movie['movie_rating'], movie['movie_year'], movie['movie_genres'])
   film.movie_card(movies_right_frame)

# alien_movie = Movie(0, 878,'alien', 'alien le 8eme passager', 'usa', '/oYbXxveNEAIgDUyoDWhpN9Lct8V.jpg', 'un vaisseau, un alien et sigourney weather', 6, 1978, [('1',), ('3',), ('5',)])

# alien_movie.movie_card(movies_right_frame)

"""" FRAME """
movies_left_frame.pack(fill=BOTH, expand=True,side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)
movies_right_frame.pack(side=RIGHT, padx=10, pady=10)

# start the program
formApp.mainloop()
