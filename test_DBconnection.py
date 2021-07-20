import unittest
from DBconnection import search_value, search_vin, getall, insert_db, delete_from_db
from FillDB import createandfill
class TestDatabaseFunctions(unittest.TestCase):
    def test_search(self):
        # test if search_value function returns empty list when sending wrong make name
        self.assertIsNone(search_value("Make", "Land roover"))

        # test if search_value function returns list when sending right make name
        self.assertIsNotNone(search_value("Make", "Land Rover"))

    def test_vin(self):
        # test if search_vin function returns a result when sending a string instead of a integer
        self.assertIsNone(search_vin("_id", "1f"))

        # test if search function returns a result when sending when sending the right integer
        self.assertIsNotNone(search_vin("_id", 1))

    def test_getall(self):
        # test if getall function returns something when sending the wrong key
        self.assertIsNone(getall("Makee"))

        # test if getall function returns a result when sending right key
        self.assertIsNotNone(getall("Make"))

    def test_insert(self):
        # test if search function returns list when sending right make name
        self.assertIsNotNone(insert_db({"_id": 1000000000, "Type": "Car", "Make": "Test", "Model": "Test", "Year": 2007, "Seat capacity": 5,
          "Roof rack availability": True}))

    def test_delete(self):
        # test if search function returns list when sending right make name
        self.assertIsNotNone(delete_from_db({"_id": 1000000000, "Type": "Car", "Make": "Test", "Model": "Test", "Year": 2007, "Seat capacity": 5,
          "Roof rack availability": True}))

