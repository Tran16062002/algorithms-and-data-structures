import unittest
import random

def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])


class TestSelectionSort(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        selectionSort(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        selectionSort(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        selectionSort(arr, len(arr))
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_array_with_duplicates(self):
        arr = [3, 3, 2, 1, 4, 4]
        selectionSort(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 3, 4, 4])

    def test_empty_array(self):
        arr = []
        selectionSort(arr, len(arr))
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [42]
        selectionSort(arr, len(arr))
        self.assertEqual(arr, [42])

    def test_random_array(self):
        large_array = [random.randint(1, 1000) for _ in range(1000)]
        sorted_array = sorted(large_array)
        selectionSort(large_array, len(large_array))
        self.assertEqual(large_array, sorted_array)

if __name__ == '__main__':
    unittest.main()