# This is a Python Program to read a number n and print and compute the series “1+2+…+n=”.

n=int(input('Enter the limit: '))
sum=0
for i in range(1,n+1):
    sum = sum+i
    if(i<n):
        print(i, end=' + ')
    else:
        print(i, end='')
print(' = ',sum)
