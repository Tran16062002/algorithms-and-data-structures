from time import perf_counter


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


# result

t1_start = perf_counter()
if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        n = int(infile.readline())
        data1 = str(infile.readline()).split(' ')
        k = int(infile.readline())
        data2 = str(infile.readline()).split(' ')
        list_to_search = [int(i) for i in data1]
        list_to_find = [int(i) for i in data2]

        array = find_positions(list_to_search, list_to_find)
        result = ' '.join(str(i) for i in array)

    with open('output.txt', 'w') as outfile:
        outfile.write(result)

t1_stop = perf_counter()
print('Время работы: %s секунд ' % (t1_stop - t1_start))