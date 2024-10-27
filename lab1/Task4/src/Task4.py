# Linear Search in Python
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


with open('input.txt', 'r') as infile:
    data = str(infile.readline())
    key = int(infile.readline())

data = data.split(' ')
arr = [int(i) for i in data]
if len(data) < 0 or len(data) > 10 ** 3 or -10 ** 3 > key or key > 10 ** 3:
    print('данные не верны')
else:

    with open('output.txt', 'w') as outfile:
        outfile.write(linearSearch(arr, key))