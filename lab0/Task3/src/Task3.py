with open('input.txt', 'r') as infile:
    n = int(infile.read())
f0, f1 = 0, 1
for i in range (2, n+1):
    f0, f1 = f1, f0+f1
with open('output.txt', 'w') as outfile:
    outfile.write(str(f1%10))