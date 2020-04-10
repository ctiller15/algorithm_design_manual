import unittest
from sorting.selection_sort import selection_sort

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

if __name__ == '__main__':
    unittest.main()

