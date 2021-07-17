import tkinter as tk
from tkinter import *

BG_COLOR = "#F83A00"
CONTENT_COLOR = '#FF754A'
TXT_COLOR = "white"
TITLE_COLOR = "black"


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
app = App()

#
# here are method calls to the window manager class
#
app.master.config(background=BG_COLOR)
app.config(background=BG_COLOR)
app.master.title("MILV")
app.master.geometry("1080x720")
app.master.iconbitmap("img/OokaLogo.ico")

# get width
width_win = app.master.winfo_width()
# get height
height_win = app.master.winfo_height()

app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

box_left = Frame(app, bg=CONTENT_COLOR)
box_middle = Frame(app, bg=CONTENT_COLOR)

# text
title_label = Label(box_left, text="coucou", bg=BG_COLOR, fg=TITLE_COLOR)
txt_01_label = Label(box_left, text="txt 1", bg=CONTENT_COLOR, fg=TXT_COLOR)
txt_02_label = Label(box_middle, text="txt 2", bg=CONTENT_COLOR, fg=TXT_COLOR)


# Pack & grid
box_left.grid(row=0, column=0)
box_middle.grid(row=0, column=1)
title_label.pack()
txt_01_label.pack()
txt_02_label.pack()

# start the program
app.mainloop()
