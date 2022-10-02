import unittest

from algorithms.strings.levenshtein_distance.levenshtein_distance import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):
    def test_same_sequences(self):
        self.assertEqual(levenshtein_distance("table", "table"), 0)

    def test_fully_different_sequences(self):
        self.assertEqual(levenshtein_distance("qwerty", "asdfgh"), 6)

    def test_half_different_sequences(self):
        self.assertEqual(levenshtein_distance("qwerty", "qwefgh"), 3)

    def test_partly_different_sequences(self):
        self.assertEqual(levenshtein_distance("mother", "father"), 2)

    def test_longer_first_sequence(self):
        self.assertEqual(levenshtein_distance("elephant", "cat"), 6)

    def test_longer_second_sequence(self):
        self.assertEqual(levenshtein_distance("cat", "elephant"), 6)


if __name__ == "__main__":
    unittest.main()
