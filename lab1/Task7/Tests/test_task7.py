import unittest
import random
# from lab1.Task1.src.Task1 import insertionSort

def insertionSort(arr):
    if len(arr) <= 1:
        return

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

class TestInsertionSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        insertionSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        insertionSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        insertionSort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_array_with_duplicates(self):
        arr = [3, 3, 2, 1, 4, 4]
        insertionSort(arr)
        self.assertEqual(arr, [1, 2, 3, 3, 4, 4])

    def test_empty_array(self):
        arr = []
        insertionSort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [42]
        insertionSort(arr)
        self.assertEqual(arr, [42])

    def test_random_array(self):
        large_array = [random.randint(1, 1000) for _ in range(1000)]
        sorted_array = sorted(large_array)
        insertionSort(large_array)
        self.assertEqual(large_array, sorted_array)


if __name__ == '__main__':
    unittest.main()