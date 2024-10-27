# Selection Sort in Python
from time import perf_counter


# function
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])


# result
t1_start = perf_counter()
with open('input.txt', 'r') as infile:
    n = int(infile.readline())
    data = str(infile.readline())

data = data.split(' ')
arr = [int(i) for i in data]
size = len(arr)
if n != len(data) or n <= 0 or n > 10 ** 3:
    print('данные не верны')
else:
    selectionSort(arr, size)
    a = ' '.join(str(i) for i in arr)
    with open('output.txt', 'w') as outfile:
        outfile.write(a)
t1_stop = perf_counter()
print('Время работы: %s секунд ' % (t1_stop - t1_start))