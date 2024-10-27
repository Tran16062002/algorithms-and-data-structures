# function
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
with open('input.txt', 'r') as infile:
    n = int(infile.readline())
    data = str(infile.readline())

data = data.split(' ')
arr = [float(i) for i in data]
list = [float(i) for i in data]
if n != len(data) or n <= 0 or n > 10 ** 3 or n % 2 == 0:
    print('данные не верны')
else:
    insertionSort(arr)

    max = arr[-1]
    x = list.index(max) + 1
    min = arr[0]
    y = list.index(min) + 1
    tb = arr[n // 2]
    z = list.index(tb) + 1
    a = str(y) + ' ' + str(z) + ' ' + str(x)

    with open('output.txt', 'w') as outfile:
        outfile.write(a)