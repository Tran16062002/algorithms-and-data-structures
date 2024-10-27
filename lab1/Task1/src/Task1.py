# Insertion Sort in Python
# function
from time import perf_counter


def insertionSort(arr):
    if n <= 1:
        return

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# result
t1_start = perf_counter()
with open('input.txt', 'r') as infile:
    n = int(infile.readline())
    data = str(infile.readline())

data = data.split(' ')
arr = [int(i) for i in data]
if n != len(data) or n <= 0 or n > 10 ** 3:
    print('данные не верны')
else:
    insertionSort(arr)
    a = ' '.join(str(i) for i in arr)
    with open('output.txt', 'w') as outfile:
        outfile.write(a)
t1_stop = perf_counter()
print('Время работы: %s секунд ' % (t1_stop - t1_start))