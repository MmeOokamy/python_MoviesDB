from api import get_api_movies_list
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
    # use get_data function and inserte into the window
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
open_btn = Button(box_left_bottom, text="Check id", command=check_api_id)



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
