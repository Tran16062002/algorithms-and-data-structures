import unittest
import random

def bubbleSort(array):
    if len(array) <= 1:
        return

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        bubbleSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        bubbleSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        bubbleSort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_array_with_duplicates(self):
        arr = [3, 3, 2, 1, 4, 4]
        bubbleSort(arr)
        self.assertEqual(arr, [1, 2, 3, 3, 4, 4])

    def test_empty_array(self):
        arr = []
        bubbleSort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [42]
        bubbleSort(arr)
        self.assertEqual(arr, [42])

    def test_random_array(self):
        large_array = [random.randint(1, 1000) for _ in range(1000)]
        sorted_array = sorted(large_array)
        bubbleSort(large_array)
        self.assertEqual(large_array, sorted_array)


if __name__ == '__main__':
    unittest.main()