import unittest

def linearSearch(arr, key):
    list = []
    for i in range(len(arr)):
        if arr[i] == key:
            list.append(i)
    count = len(list)
    if count == 0:
        return str(-1)
    elif count == 1:
        return str(list[0])
    else:
        return str(count) + '  ' + ",".join(map(str, list))

class TestLinearSearch(unittest.TestCase):
    def test_key_found_once(self):
        arr = [1, 2, 3, 4, 5]
        result = linearSearch(arr, 3)
        self.assertEqual(result, '2')  # index of 3 is 2

    def test_key_found_multiple_times(self):
        arr = [1, 2, 3, 2, 5]
        result = linearSearch(arr, 2)
        self.assertEqual(result, '2  1,3')  # 2 is found at indices 1 and 3

    def test_key_not_found(self):
        arr = [1, 2, 3, 4, 5]
        result = linearSearch(arr, 6)
        self.assertEqual(result, '-1')  # 6 is not in the list

    def test_empty_array(self):
        arr = []
        result = linearSearch(arr, 1)
        self.assertEqual(result, '-1')  # Searching in an empty array

    def test_key_found_at_start(self):
        arr = [1, 2, 3, 4, 5]
        result = linearSearch(arr, 1)
        self.assertEqual(result, '0')  # index of 1 is 0

    def test_key_found_at_end(self):
        arr = [1, 2, 3, 4, 5]
        result = linearSearch(arr, 5)
        self.assertEqual(result, '4')  # index of 5 is 4

    def test_multiple_same_elements(self):
        arr = [3, 3, 3, 3]
        result = linearSearch(arr, 3)
        self.assertEqual(result, '4  0,1,2,3')  # 3 is found at all indices


if __name__ == '__main__':
    unittest.main()