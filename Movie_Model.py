

class Movie:

    def __init__(self, orginal_title, french_title, origin, img, description, rating, date, category):
        self.original_title = orginal_title
        self.french_title = french_title
        self.origin = origin
        self.img = img
        self.description = description
        self.rating = rating
        self.date = date
        self.category = category

    """
            CREATE TABLE IF NOT EXISTS categories(
                 id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                 orginal_title TEXT,
                 french_title TEXT,
                 origin TEXT,
                 img TEXT,
                 description TEXT,
                 rating INTEGER,
                 date DATE,
                 category Category
            )
            """
