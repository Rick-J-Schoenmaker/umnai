import unittest
from FillDB import createandfill, delete_testdb
class TestFlaskFunctions(unittest.TestCase):
    def test_search(self):
        # Test if createandfill function returns message database deleted.
        self.assertRegex(delete_testdb(), "database deleted")
        # Test if createandfill function returns message database created.
        self.assertRegex(createandfill(), "database created")




