from api import get_data
from tkinter import ttk
from tkinter import *

BG_COLOR = "#F83A00"
CONTENT_COLOR = '#FF754A'
TXT_COLOR = "white"
TITLE_COLOR = "black"

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

def get_movie():
    # troncate data_list for create new data_list
    for i in data_list.get_children():
        data_list.delete(i)
    # get text input/entry
    search = search_bar.get()
    # use get_data function and inserte into the window
    movie = get_data(search)
    for row in movie:
        id = row['movie_id']
        ori_title = row['movie_original_title']
        fr_title = row['movie_french_title']
        data_list.insert('', END, values=(id, ori_title, fr_title))
        


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

box_left_top = Frame(app, bg=CONTENT_COLOR, width=150)
box_left_bottom = Frame(app, bg=CONTENT_COLOR, width=150)
box_middle_top = Frame(app, bg=CONTENT_COLOR, height=50)
box_middle = Frame(app, bg=CONTENT_COLOR)

# text
title_label = Label(box_left_top, text="coucou", bg=BG_COLOR, fg=TITLE_COLOR)
search_bar = Entry(box_middle_top)
search_enter = Button(box_middle_top, text='Search movie', command=get_movie)
txt_01_label = Label(box_left_top, text="txt 1", bg=CONTENT_COLOR, fg=TXT_COLOR)
# txt_02_label = Label(box_middle, text="txt 2", bg=CONTENT_COLOR, fg=TXT_COLOR)

# fill the box
data_list = ttk.Treeview(box_middle, columns=(1, 2, 3, 4), height=5, show="headings")
data_list.heading(1, text="movie_id")
data_list.heading(2, text="movie_original_title")
data_list.heading(3, text="movie_french_title")
data_list.column(1, width=50)
data_list.column(2, width=100)
data_list.column(3, width=100)

# BTN
exit_btn = Button(box_left_bottom, text="EXIT", command=quit)


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

# start the program
app.mainloop()
