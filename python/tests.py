import unittest
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from strings.pattern_matching import find_match 

class TestSortAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
                ([1,2,3,4,5], [1,2,3,4,5]),
                ([5,4,3,2,1], [1,2,3,4,5]),
                ([3,5,2,4,1], [1,2,3,4,5])
            ]

    def test_selection_sort(self):
        for test, assertion in self.test_cases:
            with self.subTest():
                self.assertEqual(selection_sort(test), assertion)

    def test_insertion_sort(self):
        for test, assertion in self.test_cases:
            with self.subTest():
                self.assertEqual(insertion_sort(test), assertion)

class TestStringAlgorithms(unittest.TestCase):
    def setUp(self):
        self.search_test_cases = [
            ("test", "test string", 0),
            ("string", "test string", 5)
        ]

    def test_string_match_finding(self):
        for sub, search, result in self.search_test_cases:
            with self.subTest():
                self.assertEqual(find_match(sub, search), result)

if __name__ == '__main__':
    unittest.main()

