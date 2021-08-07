# This is a Python Program to read a number n and print an inverted star pattern of the desired size.

n=int(input('Enter a number: '))
for i in range(n,0,-1):
    print((n-i)*' '+i*'*')
