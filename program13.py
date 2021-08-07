# This is a Python Program to count the number of digits in a number.

n=int(input('Enter a number: '))
count=0
while(n>0):
    count+=1
    n=n//10
print('The number of digits are: ',str(count))
