class Category:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def create_table(self):
        """
        CREATE TABLE IF NOT EXISTS categories(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             name TEXT,
             description TEXT
        )
        """