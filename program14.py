# This is a Python Program to check whether a given number is a palindrome.

n=int(input('Enter a number: '))
copy=n
n1=0
while(n>0):
    ld=n%10
    n1=n1*10+ld
    n=n//10
if(n1==copy):
    print('Palindrome number')
else:
    print('Not a Palidrome number')