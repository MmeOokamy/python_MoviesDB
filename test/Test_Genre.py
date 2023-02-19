import unittest
from db import Database
from models.genre import Genre


class TestGenre(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.genre = Genre(genre_api_id=1, genre_name="Action")

    def tearDown(self):
        self.genre.delete()
        self.db.close_connection()

    def test_get_genre_name(self):
        # Test that get_genre_name returns the correct genre name
        self.genre.save()
        self.assertEqual(self.genre.get_genre_name(), "Action")

    def test_exist(self):
        # Test that exist returns True if a genre exists in the database and False otherwise
        self.assertFalse(self.genre.exist())
        self.genre.save()
        self.assertTrue(self.genre.exist())

    def test_save(self):
        # Test that save method adds a new genre to the database if the genre does not exist
        self.genre.save()
        self.assertIsNotNone(self.genre.id)
        # Test that save method updates the genre name if the genre exists in the database
        self.genre.genre_name = "Comedy"
        self.genre.save()
        self.assertEqual(self.genre.get_genre_name(), "Comedy")

    def test_delete(self):
        # Test that delete method removes the genre from the database
        self.genre.save()
        self.assertIsNotNone(self.genre.id)
        self.genre.delete()
        self.assertIsNone(self.genre.id)
        self.assertFalse(self.genre.exist())


if __name__ == "__main__":
    unittest.main()
