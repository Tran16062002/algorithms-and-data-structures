# Merge Sort in python
from time import perf_counter
def mergeSort(array):
    if len(array) == 1:
        return array
    else:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
        return array

t1_start = perf_counter()
if __name__ == '__main__':

    with open('input.txt', 'r') as infile:
        n = int(infile.readline())
        data = str(infile.readline())
    data = data.split(' ')
    arr = [int(i) for i in data]

    mergeSort(arr)
    result = ' '.join(str(i) for i in arr)
    with open('output.txt', 'w') as outfile:
        outfile.write(result)

t1_stop = perf_counter()
print('Время работы: %s секунд '% (t1_stop - t1_start))