import requests
from tkinter import *
from api import get_api_movies_list, get_api_movie
from io import BytesIO
from PIL import Image, ImageTk
import psycopg2

BG_COLOR = "#F83A00"
CONTENT_BG_COLOR = '#FF754A'
TXT_COLOR = "white"
TITLE_COLOR = "black"

class Movie:
    
    def __init__(self, movie_id, movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year, genres_list):
        self.movie_id = movie_id
        self.movie_api_id = movie_api_id
        self.movie_original_title = movie_original_title
        self.movie_french_title = movie_french_title
        self.movie_original_language = movie_original_language
        self.movie_img = movie_img
        self.movie_description = movie_description
        self.movie_rating = movie_rating
        self.movie_year = movie_year
        self.genres_list = genres_list

    def get_poster(self, size_percent):
        image_api = 'https://image.tmdb.org/t/p/w500' + self.movie_img
        resp_img = requests.get(image_api)
        if resp_img.status_code==200: 
            img_data = resp_img.content
        
        poster = Image.open(BytesIO(img_data))
        
        new_height = poster.height*size_percent
        new_width = poster.width*size_percent
        poster = poster.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(poster)

        return img


    def movie_card(self, frame):
        img = Movie.get_poster(self, 0.2)
        card = LabelFrame(frame, width=150, text=self.movie_french_title, bg=BG_COLOR)
        
        # Img
        label = Label(card, image=img)
        label.image = img

        # movie-infos
        movie_id = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_id)
        movie_api_id = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_api_id)
        movie_original_title = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_original_title)
        movie_french_title = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_french_title)
        movie_original_language = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_original_language)
        movie_img = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_img)
        movie_description = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_description)
        movie_rating = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_rating)
        movie_year = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.movie_year)
        genres_list = Label(card, bg=BG_COLOR, fg=TITLE_COLOR, anchor='w',text=self.genres_list)

        label.grid(row=0, rowspan=10, column=0, sticky=W, padx=5)
        movie_id.grid(row=0, column=1, sticky=W)
        movie_api_id.grid(row=1, column=1, sticky=W)
        movie_original_title.grid(row=2, column=1, sticky=W)
        movie_french_title.grid(row=3, column=1, sticky=W)
        movie_original_language.grid(row=4, column=1, sticky=W)
        movie_img.grid(row=5, column=1, sticky=W)
        movie_description.grid(row=6, column=1, sticky=W)
        movie_rating.grid(row=7, column=1, sticky=W)
        movie_year.grid(row=8, column=1, sticky=W)
        genres_list.grid(row=9, column=1, sticky=W)

        card.pack()


