# Bubble sort in Python
# function
from time import perf_counter


def bubbleSort(array):
    if len(array) <= 1:
        return

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


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
    bubbleSort(arr)
    a = ' '.join(str(i) for i in arr)
    with open('output.txt', 'w') as outfile:
        outfile.write(a)
t1_stop = perf_counter()
print('Время работы: %s секунд ' % (t1_stop - t1_start))