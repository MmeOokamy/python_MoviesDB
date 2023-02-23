from tkinter import ttk
# from styles.colors import COLORS # Module contenant des constantes de couleur

COLORS = {
    '':'',
    'w': '#ffffff',
    'b': '#000000',
    'light_blue': '#a5d8dd',
    'blue': '#0091d5',
    'dark_blue': '#1c4e80',
    'light_green': '#4CAF50',
}


# Définir les couleurs et le style des boutons
bg = COLORS['dark_blue']
txt = COLORS['w']
lb = COLORS['light_blue']
lg = COLORS['light_green']

style = ttk.Style()
style.configure('Custom.TButton', 
                foreground=txt, 
                background=lg,
                font=('Sans-serif', 12),
                padding=5,
                borderwidth=2,
                relief='groove')

style.configure('Search.TButton', 
                foreground=lb, 
                background=bg,
                font=('Sans-serif', 8),
                padding=2,
                borderwidth=1,
                relief='groove')

# update button
style.configure('Finished.TButton', 
                foreground=txt, 
                background=bg,
                font=('Sans-serif', 12),
                padding=5,
                borderwidth=2,
                relief='groove')

style.configure('Exit.TButton',
                foreground=txt,
                background=bg,
                font=('Sans-serif', 12),
                padding=2,
                borderwidth=0,
                relief='groove')

# Redéfinir les couleurs de fond et de texte des boutons lorsqu'ils sont survolés
style.map('Custom.TButton', 
          foreground=[('active', txt)], 
          background=[('active', lg)])

style.map('Search.TButton', 
          foreground=[('active', lb)], 
          background=[('active', bg)])

style.map('Exit.TButton',
          foreground=[('active', lb)],
          background=[('active', bg)])

style.map('Finished.TButton', 
          foreground=[('active', txt)], 
          background=[('active', bg)])