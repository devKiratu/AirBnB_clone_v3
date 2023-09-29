#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


@unittest.skipUnless(models.storage_t == 'db', "For db_stroage methods only")
class TestDBStorageMethods(unittest.TestCase):
    """Test existence and workings of the dbStorage methods"""
    def test_get_method_exists(self):
        """Test get method exists in db_storage"""
        class_props = dir(models.storage)
        self.assertIn('get', class_props)

    def test_get_method_fetches_right_object(self):
        """Test get method fetches correct object given the id"""
        first_state_id = list(models.storage.all(State).values())[0].id
        fetched_state_id = models.storage.get(State, first_state_id).id
        self.assertEqual(first_state_id, fetched_state_id)

    def test_get_method_returns_None_if_not_found(self):
        """Test get method returns None if object is not found"""
        result = models.storage.get(State, "nonexistentid")
        self.assertIsNone(result)

    def test_count_method_exists(self):
        """Test count method exists in db_storage"""
        class_props = dir(models.storage)
        self.assertIn('count', class_props)

    def test_count_all_objects(self):
        """Test count returns correct number of all objects"""
        expected = len(models.storage.all())
        actual = models.storage.count()
        self.assertEqual(expected, actual)

    def test_count_specific_objects(self):
        """Test count returns the correct number of various objects"""
        states_expected = len(models.storage.all(State))
        states_actual = models.storage.count(State)
        self.assertEqual(states_expected, states_actual)

        cities_expected = len(models.storage.all(City))
        cities_actual = models.storage.count(City)
        self.assertEqual(cities_expected, cities_actual)

        places_expected = len(models.storage.all(Place))
        places_actual = models.storage.count(Place)
        self.assertEqual(places_expected, places_actual)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
