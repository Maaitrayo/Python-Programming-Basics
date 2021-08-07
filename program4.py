# This is a Python Program to reverse a given number.

n = int(input('Enter a number: '))
reverse = 0
while(n>0):
    last_digit = n%10
    reverse = reverse*10 + last_digit
    n = n//10
print('The reversed number is:',reverse)
