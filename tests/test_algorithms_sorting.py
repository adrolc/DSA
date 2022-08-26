import unittest

from data.sorting import sorting_data
from algorithms.sorting.bubble_sort.bubble_sort import bubble_sort
from algorithms.sorting.merge_sort.merge_sort import merge_sort


class TestBubbleSort(unittest.TestCase):
    pass

class TestMergeSort(unittest.TestCase):
    pass

algorithms = [
    {
        "test_class": TestBubbleSort,
        "method_prefix": "test_bubble_sort",
        "function": bubble_sort
    },
    {
        "test_class": TestMergeSort,
        "method_prefix": "test_merge_sort",
        "function": merge_sort
    },
]
# Dynamically generated test methods.
# Name and data are taken from the sorting_data dictionary as:
# key: str = "test name"
# value: list[list[int]] = [list_to_sorted, sorted_list]
def add_method(cls, func, name, data):
    def method(self):
        self.assertEqual(func(data[0]), data[1])

    method.__name__ = name
    setattr(cls, method.__name__, method)


for test_name, test_data in sorting_data.items():
    for algorithm in algorithms:
        method_name = f"{algorithm['method_prefix']}_{test_name}"
        add_method(algorithm["test_class"], algorithm["function"], method_name, test_data)


if __name__ == "__main__":
    unittest.main()
