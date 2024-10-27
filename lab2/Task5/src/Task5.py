from time import perf_counter

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

def count_mode(arr, element, left, right):
    count = 0
    for i in range(left, right + 1):
        if arr[i] == element:
            count += 1
    return count


def print_result(array, n):
    if n>len(array)//2:
        return str(1)
    else:
        return str(0)
# result
t1_start = perf_counter()

if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        num = int(infile.readline())
        data = str(infile.readline())
    data = data.split(' ')
    array = [int(i) for i in data]
    result = find_mode(array, 0, len(array)-1)
    n = result[1]
    with open('output.txt', 'w') as outfile:
        outfile.write(print_result(array, n))

t1_stop = perf_counter()
print('Время работы: %s секунд '% (t1_stop - t1_start))