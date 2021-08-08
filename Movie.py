import requests
from tkinter.ttk import *
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

    def get_poster(self):
        image_api = 'https://image.tmdb.org/t/p/w500' + self.movie_img
        resp_img = requests.get(image_api)
        if resp_img.status_code==200: 
            img_data = resp_img.content
        
        poster = Image.open(BytesIO(img_data))
        
        new_height = poster.height/2
        new_width = poster.width/2
        poster = poster.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(poster)

        return img


    def movie_card(self, frame):
        img = Movie.get_poster(self)
        card = LabelFrame(frame, bg=BG_COLOR, width=150, text=self.movie_french_title)
        
        label = Label(card, image=img, bg=BG_COLOR)
        label.image = img 
        label.pack(expand=True)

        card.pack()


