# This is a Python Program to print all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.

for i in range(0,51):
    if(i%2!=0 & i%3!=0):
        print(i)

