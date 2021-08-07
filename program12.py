# This is a Python Program to find the smallest divisor of an integer.

n=int(input('Enter a number: '))
list=[]
for i in range(2,n+1):
    if(n%i==0):
        list.append(i)
print(min(list))
