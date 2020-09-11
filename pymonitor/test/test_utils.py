import unittest
from typing import Dict
from pymonitor.utils import dict_to_string


class TestUtils(unittest.TestCase):

    def test_dict_to_string(self):
        truth: Dict = {'one': 1, 'two': 2}
        expected = "one: {1} two: {2} "
        actual = dict_to_string(truth)

        self.assertEqual(actual, expected)

    def test_dict_to_string_empty(self):
        truth: Dict = {}
        expected = ""
        actual = dict_to_string(truth)

        self.assertEqual(actual, expected)
