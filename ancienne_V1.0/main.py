from api import get_api_movie, get_api_movies_list
# from crud import genres, create_movie
# from models import Movie, Genre, 
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

def search_movies():
    # troncate data_list for create new data_list
    for i in data_list.get_children():
        data_list.delete(i)
    # get text input/entry
    search = search_bar.get()
    # use get_data function and insert into the window
    movie = get_api_movies_list(search)
    for row in movie:
        id = row['movie_id']
        ori_title = row['movie_original_title']
        fr_title = row['movie_french_title']
        data_list.insert('', END, values=(id, ori_title, fr_title))
        
def check_api_id():
    if len(data_list.selection()) == 1:
        # One item selected
        item_dict = data_list.item(data_list.selection())
        print(item_dict['values'][0])
        return item_dict['values'][0]
    else:
        messagebox.showinfo('Information', "Veuillez Selectionner un Film")
        print(len(data_list.selection()))
        # MULTI SELECTION 
        # api_id = data_list.selection()
        # for id in api_id:
        #     item_row = data_list.item(id)
        #     print(item_row['values'][0])
    

def get_movie_detail():
    get_api_id = data_list.item(data_list.selection())
    api_id = get_api_id['values'][0]
    movie = get_api_movie(api_id)
    print(movie)
    create_frame = Toplevel(app, bg=BG_COLOR)

    # Label
    create_movie_api_id_label = Label(create_frame, text='id movie api', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_original_title_label = Label(create_frame, text='Titre Original', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_french_title_label = Label(create_frame, text='Titre Français', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_original_language_label = Label(create_frame, text='Original Language', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_img_label = Label(create_frame, text='Image', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_description_label = Label(create_frame, text='Description', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_rating_label = Label(create_frame, text='Note', bg=BG_COLOR, fg=TITLE_COLOR)
    create_movie_year_label = Label(create_frame, text='Année', bg=BG_COLOR, fg=TITLE_COLOR)

    # Entry
    create_movie_api_id_entry = Entry(create_frame)
    create_movie_original_title_entry = Entry(create_frame)
    create_movie_french_title_entry = Entry(create_frame)
    create_movie_original_language_entry = Entry(create_frame)
    create_movie_img_entry = Entry(create_frame)
    create_movie_description_entry = Text(create_frame, height=4)
    create_movie_rating_entry = Entry(create_frame)
    create_movie_year_entry = Entry(create_frame)

    #Fill Entry with movie database
    create_movie_api_id_entry.insert(0, movie['movie_api_id'])
    create_movie_original_title_entry.insert(0,movie['movie_original_title'])
    create_movie_french_title_entry.insert(0,movie['movie_french_title'])
    create_movie_original_language_entry.insert(0,movie['movie_original_language'])
    create_movie_img_entry.insert(0,movie['movie_img'])
    create_movie_description_entry.insert(1.0, movie['movie_description'])
    create_movie_rating_entry.insert(0,movie['movie_rating'])
    create_movie_year_entry.insert(0,movie['movie_year'])



    # multi selected list of genres =D    
    genres_frame = Frame(create_frame, bg=BG_COLOR)
    genres_list_db = genres()
    vars = []
    for genre in genres_list_db:
        id = genre['genre_id']
        name = genre['genre_name']
        var = StringVar(value=id)
        vars.append(var)
        genres_cbx = Checkbutton(genres_frame, variable=var, text=name, onvalue=id, offvalue='', anchor=W)
        genres_cbx.pack(fill="x", anchor="w")
    
    def new_movie():
        movie_api_id = create_movie_api_id_entry.get()
        movie_original_title = create_movie_original_title_entry.get()
        movie_french_title = create_movie_french_title_entry.get()
        movie_original_language = create_movie_original_language_entry.get()
        movie_img = create_movie_img_entry.get()
        movie_description = create_movie_description_entry.get("1.0","end")
        movie_rating = create_movie_rating_entry.get()
        movie_year = create_movie_year_entry.get()

        # MULTI SELECTION 
        genres_id_tuple = []
        for var in vars:
            value = var.get()
            if value:
                genres_id_tuple.append(value)
        
        movies_list = genres_id_tuple
        create_movie(movie_api_id, movie_original_title, movie_french_title, movie_original_language, movie_img, movie_description, movie_rating, movie_year, movies_list)


    # BTN
    save_btn = Button(create_frame, text='Save data', justify=CENTER, command=new_movie)
    exit_btn = Button(create_frame, text="EXIT", justify=CENTER, command=create_frame.destroy)

    """ UPDATE FRAME Pack, grid, place """
    # Label
    create_movie_original_title_label.grid(row=0, column=0, padx=1, pady=1)
    create_movie_french_title_label.grid(row=1, column=0, padx=1, pady=1)
    create_movie_original_language_label.grid(row=2, column=0, padx=1, pady=1)
    create_movie_img_label.grid(row=3, column=0, padx=1, pady=1)
    create_movie_description_label.grid(row=4, column=0, padx=1, pady=1)
    create_movie_rating_label.grid(row=5, column=0, padx=1, pady=1)
    create_movie_year_label.grid(row=6, column=0, padx=1, pady=1)
    create_movie_api_id_label.grid(row=7, column=0, padx=1, pady=1)
    # update_movie_id_label.grid(row=8, column=0, padx=1, pady=1)

    # Entry
    create_movie_original_title_entry.grid(row=0, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_french_title_entry.grid(row=1, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_original_language_entry.grid(row=2, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_img_entry.grid(row=3, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_description_entry.grid(row=4, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_rating_entry.grid(row=5, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_year_entry.grid(row=6, column=1, padx=1, pady=1, sticky=NSEW)
    create_movie_api_id_entry.grid(row=7, column=1, padx=1, pady=1, sticky=NSEW)
    # update_movie_id_entry.grid(row=8, column=1, padx=1, pady=1, sticky=NSEW)

    # multi selected list of genres =D
    genres_frame.grid(row=0, column=3, rowspan=10, ipadx=5, padx=10)

    # btn
    save_btn.grid(row=9, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)
    exit_btn.grid(row=10, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)



# create the application
app = App()

#
# here are method calls to the window manager class
#
app.master.config(background=BG_COLOR)
app.config(background=BG_COLOR)
app.master.title("MILV")
app.master.geometry("1000x400")
 
# icone = PhotoImage(file='img/OokaLogo.png')
# app.master.iconphoto(True, icone)
# app.master.iconbitmap('img/OokaLogo.ico') # windows
# app.tk.call('wm', 'iconphoto', app.master._w, LOGO)


# get width
width_win = app.master.winfo_width()
# get height
height_win = app.master.winfo_height()

app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

box_left_top = Frame(app, bg=CONTENT_BG_COLOR, width=150)
box_left_bottom = Frame(app, bg=CONTENT_BG_COLOR, width=150)
box_middle_top = Frame(app, bg=CONTENT_BG_COLOR, height=50)
box_middle = Frame(app, bg=CONTENT_BG_COLOR)

# text
title_label = Label(box_left_top, text="coucou", bg=BG_COLOR, fg=TITLE_COLOR)
search_bar = Entry(box_middle_top)
search_enter = Button(box_middle_top, text='Search movie', command=search_movies)
txt_01_label = Label(box_left_top, text="txt 1", bg=CONTENT_BG_COLOR, fg=TXT_COLOR)
# txt_02_label = Label(box_middle, text="txt 2", bg=CONTENT_BG_COLOR, fg=TXT_COLOR)

# fill the box
data_list = ttk.Treeview(box_middle, columns=(1, 2, 3), height=5, show="headings")
data_list.heading(1, text="ID")
data_list.heading(2, text="Original Title")
data_list.heading(3, text="French Title")
data_list.column(1, width=75)
data_list.column(2, width=200)
data_list.column(3, width=200)

# BTN
exit_btn = Button(box_left_bottom, text="EXIT", command=quit)
open_btn = Button(box_left_bottom, text="Check id", command=get_movie_detail)



# Pack & grid
box_left_top.grid(row=0, column=0)
box_left_bottom.grid(row=1, column=0)
box_middle_top.grid(row=0, column=1)
box_middle.grid(row=1, column=1)
title_label.pack()
search_bar.pack(side=LEFT)
search_enter.pack(side=RIGHT)
txt_01_label.pack()
# txt_02_label.pack()
data_list.pack()
exit_btn.pack(fill=X)
open_btn.pack(fill=X)

# start the program
app.mainloop()
