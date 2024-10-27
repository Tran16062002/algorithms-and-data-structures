import unittest

def count_mode(arr, element, left, right):
    count = 0
    for i in range(left, right + 1):
        if arr[i] == element:
            count += 1
    return count

def find_mode(arr, left, right):
    if left > right:
        return None, 0
    if left == right:
        return arr[left], 1

    mid = (left + right) // 2
    left_mode, left_count = find_mode(arr, left, mid)
    right_mode, right_count = find_mode(arr, mid + 1, right)

    total_left = count_mode(arr, left_mode, left, right)
    total_right = count_mode(arr, right_mode, left, right)

    if total_left > total_right:
        return left_mode, total_left
    else:
        return right_mode, total_right

def print_result(array, n):
    if n > len(array) // 2:
        return str(1)
    else:
        return str(0)

class TestFindMode(unittest.TestCase):

    def test_find_mode_single_mode(self):
        arr = [1, 2, 2, 3, 4]
        mode, count = find_mode(arr, 0, len(arr) - 1)
        self.assertEqual(mode, 2)
        self.assertEqual(count, 2)

    def test_find_mode_multiple_modes(self):
        arr = [1, 1, 2, 2, 3]
        mode, count = find_mode(arr, 0, len(arr) - 1)
        # Both modes (1 and 2) appear the same number of times, but find_mode may return the first one found.
        self.assertIn(mode, [1, 2])
        self.assertEqual(count, 2)

    def test_find_mode_empty_array(self):
        arr = []
        mode, count = find_mode(arr, 0, -1)
        self.assertIsNone(mode)
        self.assertEqual(count, 0)

    def test_find_mode_no_elements(self):
        arr = [1, 2, 3, 4, 5]
        mode, count = find_mode(arr, 0, len(arr) - 1)
        self.assertEqual(mode, 5)
        self.assertEqual(count, 1)

    def test_count_mode(self):
        arr = [1, 2, 2, 3, 4]
        count = count_mode(arr, 2, 0, len(arr) - 1)
        self.assertEqual(count, 2)

    def test_print_result_more_than_half(self):
        array = [1, 1, 1, 2, 2]
        result = print_result(array, 3)  # Mode 1 occurs 3 times
        self.assertEqual(result, '1')

    def test_print_result_less_than_half(self):
        array = [1, 1, 2, 2, 3]
        result = print_result(array, 2)  # Mode 1 occurs 2 times
        self.assertEqual(result, '0')

if __name__ == '__main__':
    unittest.main()