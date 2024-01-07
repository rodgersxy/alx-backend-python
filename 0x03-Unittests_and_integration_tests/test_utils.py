#!/usr/bin/env python3
"""
Unittests and Integration Tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittests for access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unittests for get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, payload):
        """
        Test get_json
        """
        class Mocked(Mock):
            """
            Mock class
            """

            def json(self):
                """
                Mock json
                """
                return payload
        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """
    Unittests for memoize
    """
    def test_memoize(self):
        """
        Test memoize
        """
        class TestClass:
            """
            Test class
            """

            def a_method(self):
                """
                Test method
                """
                return 42

            @memoize
            def a_property(self):
                """
                Test property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock.assert_called_once()
