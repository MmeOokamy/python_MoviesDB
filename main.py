import tkinter as tk
from tkinter import *

BG_COLOR = "#F83A00"
CONTENT_COLOR = '#FF754A'


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
app = App()

#
# here are method calls to the window manager class
#
app.master.title("MILV")
app.master.geometry("1080x720")
app.master.iconbitmap("img/OokaLogo.ico")
app.master.config(background=BG_COLOR)
app.config(background=BG_COLOR)

# get width
width_win = app.master.winfo_width()
# get height
height_win = app.master.winfo_height()

# Left column
frame_left = Frame(app, bg=BG_COLOR)

# Main content
frame_main = Frame(app, bg=BG_COLOR)

# Left Part
can_menu = Canvas(frame_left, width=150, height=height_win, bg=CONTENT_COLOR, bd=0, highlightthickness=0,
                  relief='ridge')
can_menu.pack(padx=20, pady=20, fill=Y, expand=True)
label_title = Label(can_menu, text='Categories', font=('Roboto', 30), bg=CONTENT_COLOR, fg='white')
label_title.grid(row=0, column=0)
label_text_list = Label(can_menu, text='Show Me(1)', font=('Roboto', 20), bg=CONTENT_COLOR, fg='white')
label_text_list.grid(row=1, column=0)

btn_exit = Button(can_menu, text="EXIT", command=app.master.destroy, bg=CONTENT_COLOR, fg='white')
btn_exit.grid(row=2, column=0, sticky='s')

# Main Part
can_middle_search = Canvas(frame_main, height=50, bg=CONTENT_COLOR, bd=0, highlightthickness=0, relief='ridge')
can_middle_search.pack(padx=20, pady=20, fill=X)

can_middle_content = Canvas(frame_main, width=width_win - 300, bg=CONTENT_COLOR, bd=0, highlightthickness=0, relief='ridge')
can_middle_content.pack(padx=20, pady=20, expand=True)

# init frame
frame_left.grid(row=0, column=0, sticky="nesw")
frame_main.grid(row=0, column=1, sticky="nesw")

# start the program
app.mainloop()
