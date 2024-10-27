import unittest
import random
from lab2.Task1.src.Task1 import mergeSort

class TestMergeSort(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        mergeSort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_array_with_duplicates(self):
        arr = [3, 3, 2, 1, 4, 4]
        mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 3, 4, 4])

    def test_single_element_array(self):
        arr = [42]
        mergeSort(arr)
        self.assertEqual(arr, [42])
    def test_sort_large_array(self):
        large_array = [random.randint(1,10000) for _ in range(10000)]
        sorted_array = sorted(large_array)
        mergeSort(large_array)
        self.assertEqual(large_array, sorted_array)

if __name__ == '__main__':
    unittest.main()