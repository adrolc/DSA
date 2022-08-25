import unittest

from algorithms.sorting.bubble_sort.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def _test_sort(self, sorting_func, input):
        expected_output = sorted(input)
        self.assertEqual(sorting_func(input), expected_output)

    def test_bubble_sort_with_positive_numbers(self):
        input = [7, 4, 1, 2, 12, 10, 3, 5]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_with_negative_numbers(self):
        input = [-1, -3, -12, -5, -7, -2]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_with_positive_and_negative_numbers(self):
        input = [-5, 2, -14, 15, 4, 1, -3, 2]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_same_numbers(self):
        input = [5, 5, 5, 5, 5]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_reversed(self):
        input = [5, 4, 3, 2, 1]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_one_element(self):
        input = [1]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_empty_list(self):
        input = []
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_already_sorted(self):
        input = [1, 2, 3, 4, 5]
        self._test_sort(bubble_sort, input)

    def test_bubble_sort_with_repetitions(self):
        input = [5, 2, 6, 2, 5, 1, 2, 8, 6]
        self._test_sort(bubble_sort, input)


if __name__ == "__main__":
    unittest.main()
