import unittest

from data.sorting import sorting_data
from algorithms.sorting.bubble_sort.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    pass


# Dynamically generated test methods.
# Name and data are taken form the sorting_data dictionary as:
# key: str = "name of dataset"
# value: list[list[int]] = [list_to_sorted, sorted_list]
def add_method(cls, name, data):
    def method(self):
        self.assertEqual(bubble_sort(data[0]), data[1])

    method.__name__ = f"test_bubble_sort_{name}"
    setattr(cls, method.__name__, method)


for k, v in sorting_data.items():
    add_method(TestBubbleSort, k, v)


if __name__ == "__main__":
    unittest.main()
