a = int(input())
b = int(input())
if 10**(-9)<=a and a<= 10**9 and 10**(-9)<=b and b<= 10**9:
    print(a+b*b)
else:
    print('число не верно')