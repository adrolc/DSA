import unittest

from data.searching_data import searching_data
from data.searching_data import SORTED_COLLECTION
from algorithms.searching.binary_search.binary_search import binary_search
from algorithms.searching.binary_search.binary_search_recursive import (
    binary_search as binary_search_recursive,
)


class TestBinarySearch(unittest.TestCase):
    def _test_search(self, wanted, expected_output):
        self.assertEqual(binary_search(SORTED_COLLECTION, wanted), expected_output)


class TestBinarySearchResursive(unittest.TestCase):
    def _test_search(self, wanted, expected_output):
        self.assertEqual(
            binary_search_recursive(SORTED_COLLECTION, wanted, 0, len(SORTED_COLLECTION) - 1),
            expected_output,
        )


algorithms = [
    {
        "test_class": TestBinarySearch,
        "method_prefix": "test_binary_search",
    },
    {
        "test_class": TestBinarySearchResursive,
        "method_prefix": "test_binary_search_recursive",
    },
]
# Dynamically generated test methods.
# Name and data are taken from the searching_data dictionary as:
# key: str = "test name"
# value: list[int] = [wanted_value, expected_output]
# Sorted collection is defined in searching_data.py
def add_method(cls, name, data):
    def method(self):
        self._test_search(data[0], data[1])

    method.__name__ = name
    setattr(cls, method.__name__, method)


for test_name, test_data in searching_data.items():
    for algorithm in algorithms:
        method_name = f"{algorithm['method_prefix']}_{test_name}"
        add_method(algorithm["test_class"], method_name, test_data)


if __name__ == "__main__":
    unittest.main()
