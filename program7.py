# This is a Python Program to print all numbers in a range divisible by a given number.

a = int(input("Enter lower limit "))
b = int(input("Enter upper limit "))
n = int(input("Enter number to be divided by: "))
for i in range(a,b+1):
    if(i%n==0):
        print(i)