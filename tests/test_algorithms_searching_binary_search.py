import unittest

from algorithms.searching.binary_search.binary_search import binary_search
from algorithms.searching.binary_search.binary_search_recursive import (
    binary_search as binary_search_recursive,
)


class TestBinarySearch(unittest.TestCase):
    def _test_search(self, wanted, expected_output=None):
        input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if expected_output == None:
            expected_output = input_arr.index(wanted)
        self.assertEqual(binary_search(input_arr, wanted), expected_output)

    def test_binary_search_exist_value(self):
        self._test_search(3)

    def test_binary_search_nonexist_value(self):
        self._test_search(99, -1)

    def test_binary_search_first_element(self):
        self._test_search(1)

    def test_binary_search_last_element(self):
        self._test_search(10)


class TestBinarySearchResursive(unittest.TestCase):
    def _test_search(self, wanted, expected_output=None):
        input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if expected_output == None:
            expected_output = input_arr.index(wanted)
        self.assertEqual(
            binary_search_recursive(input_arr, wanted, 0, len(input_arr) - 1),
            expected_output,
        )

    def test_binary_search_recursive_exist_value(self):
        self._test_search(3)

    def test_binary_search_recursive_nonexist_value(self):
        self._test_search(99, -1)

    def test_binary_search_recursive_first_element(self):
        self._test_search(1)

    def test_binary_search_recursive_last_element(self):
        self._test_search(10)


if __name__ == "__main__":
    unittest.main()
