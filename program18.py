# This is a Python Program to read a number n and print an identity matrix of the desired size.

n=int(input('Enter a number: '))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print('1', sep=' ', end=' ')
        else:
            print('0', sep=' ', end=' ')
    print()