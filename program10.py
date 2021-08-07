# This is a Python Program to print odd numbers within a given range.

a = int(input('Enter the lower range: '))
b = int(input('Enter the upper range: '))
for i in range(a,b+1):
    if(i%2 != 0):
        print(i)