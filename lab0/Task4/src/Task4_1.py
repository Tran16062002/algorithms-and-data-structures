from time import perf_counter
with open('input.txt', 'r') as infile:
    n = int(infile.read())
t1_start = perf_counter()
f0, f1 = 0, 1
for i in range (2, n+1):
    f0, f1 = f1, f0+f1
t1_stop = perf_counter()
print('Время работы: %s секунд '% (t1_stop - t1_start))
with open('output.txt', 'w') as outfile:
    outfile.write(str(f1))