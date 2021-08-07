# This is a Python Program to find the sum of digits in a number.

n=int(input('Enter a number: '))
sum=0
while(n>0):
    last_digit=n%10
    sum=sum+last_digit
    n=n//10
print('The sum of the digit is: ',str(sum))