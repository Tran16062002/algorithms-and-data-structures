# Mở và đọc số nguyên từ file input.txt
with open('input.txt', 'r') as infile:
    a, b = map(int, infile.read().split())

# TÍnh tổng của a và b
result = a + b*b

# Mở file output.txt để ghi kết quả
with open('output.txt', 'w') as outfile:
    outfile.write(str(result))