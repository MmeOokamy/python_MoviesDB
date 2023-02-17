# Movies_python

    Odyssey Dev' : réecriture de MovieDB version python et Tkinter:
        - la Poo et ses methodes
        - Dev&Co, quand le polish ne suffit plus
        - Have fun
        - <3
        - en cas de bug : sudo apt-get install python3-tk



**Titre du projet :** 

    MovieDB
        |── env/
        |── img/
        |── styles/
        |   ├── colors.py
        |   └── ttk_styles.py
        |── test/
        |   ├── Test_Genre.py
        |   └── Test_Movie.py
        |── Api.py
        |── colors.py
        |── db_init.py
        |── db.py
        |── main.py
        |── models.py
        |── ttk_styles.py
        |── utils.py
       


**Description du projet :** 
    
    MovieDB est une application de gestion de films. Elle permet de rechercher, ajouter, supprimer et modifier des films ainsi que les genres associés à ces films.

**Fonctionnalités principales :**

    - Recherche de films par nom ou par genre
    - Affichage des détails d'un film, y compris le titre original, le synopsis, la date de sortie et les genres associés
    - Ajout d'un nouveau film, y compris son titre original, sa date de sortie, son synopsis et les genres associés
    - Modification des détails d'un film existant, y compris le titre original, la date de sortie, le synopsis et les genres associés
    - Suppression d'un film existant
    - Recherche de genres
    - Affichage des détails d'un genre, y compris le nom du genre et les films associés
    - Ajout d'un nouveau genre
    - Modification du nom d'un genre existant
    - Suppression d'un genre existant

**Architecture du projet :**

    - Le projet est écrit en Python 3 et utilise la bibliothèque Tkinter pour l'interface utilisateur.
    - Les données sont stockées dans une base de données SQLite.
    - Le modèle de données utilise deux classes : Movie et Genre. Chaque instance de Movie peut être associée à plusieurs instances de Genre.
    - Les opérations de lecture, d'écriture et de suppression de données sont effectuées via une classe Database qui utilise les modules Python sqlite3.
    - L'interface utilisateur est implémentée en utilisant la bibliothèque Tkinter. Les différents écrans sont implémentés sous forme de classes.

**Récapitulatif de ce qui a été fait :**

    - La base de données a été créée en utilisant SQLite, et une classe Database a été implémentée pour gérer les opérations de lecture, d'écriture et de suppression de données.
    - Deux classes de modèle de données ont été créées : Movie et Genre, qui utilisent la classe Database pour effectuer des opérations de base de données.
    - Les méthodes save() et delete() ont été implémentées pour les classes Movie et Genre.
    - Revision de l'Api `search_movies` et `get_movie`
    - Deplacer la logique de main.py dans un fichier utils.py qui fera le liens entre l'interface utilisateur et l'api / model / db
    - `Genre` ne sera pas modifiable par l'utilisateur, possibilité de mettre a jour par rapport a l'api


**Prochaines étapes :**

    c'est un peu le bordel =D :
    - revoir le fichier install.md et requirements.txt
    - Implémenter l'interface utilisateur en utilisant la bibliothèque Tkinter.
    - Créer des classes d'écran pour les différentes fonctionnalités de l'application.
    - Implémenter la recherche de films par nom.
    - Implémenter l'ajout de nouveaux films.
    - Implémenter la modification et la suppression de films existants.
    - Implémenter l'ajout, la modification et la suppression de genres.
    - Il y en a encore surement bcp =)
