from tkinter import ttk
from styles.colors import COLORS # Module contenant des constantes de couleur

COLORS = {
    '':'',
    'w': '#ffffff',
    'b': '#000000',
    'light_blue': '#a5d8dd',
    'blue': '#0091d5',
    'dark_blue': '#1c4e80',
}


# Définir les couleurs et le style des boutons
bg = COLORS['dark_blue']
txt = COLORS['w']

style = ttk.Style()
style.configure('Custom.TButton', 
                foreground=txt, 
                background='#4CAF50',
                font=('Sans-serif', 12),
                padding=10,
                borderwidth=2,
                relief='groove')

# update button
style.configure('Finished.TButton', 
                foreground=txt, 
                background=bg,
                font=('Sans-serif', 12),
                padding=10,
                borderwidth=2,
                relief='groove')