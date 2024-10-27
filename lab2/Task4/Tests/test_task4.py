import unittest

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_positions(list_to_search, list_to_find):
    sorted_list = sorted(list_to_search)
    positions = []

    for item in list_to_find:
        pos = binary_search(sorted_list, item)
        positions.append(pos)

    return positions

class TestBinarySearchAndFindPositions(unittest.TestCase):

    def test_binary_search_found(self):
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 3)
        self.assertEqual(result, 2)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 6)
        self.assertEqual(result, -1)

    def test_find_positions_all_found(self):
        list_to_search = [1, 2, 3, 4]
        list_to_find = [1, 2, 3]
        result = find_positions(list_to_search, list_to_find)
        self.assertEqual(result, [0, 1, 2])

    def test_find_positions_some_not_found(self):
        list_to_search = [1, 2, 3, 4]
        list_to_find = [1, 5]
        result = find_positions(list_to_search, list_to_find)
        self.assertEqual(result, [0, -1])

    def test_find_positions_all_not_found(self):
        list_to_search = [1, 2, 3, 4]
        list_to_find = [5, 6]
        result = find_positions(list_to_search, list_to_find)
        self.assertEqual(result, [-1, -1])

    def test_empty_search_list(self):
        list_to_search = []
        list_to_find = [1, 2]
        result = find_positions(list_to_search, list_to_find)
        self.assertEqual(result, [-1, -1])

    def test_empty_find_list(self):
        list_to_search = [1, 2, 3]
        list_to_find = []
        result = find_positions(list_to_search, list_to_find)
        self.assertEqual(result, [])  # No items to find

if __name__ == '__main__':
    unittest.main()