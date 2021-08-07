# This is a Python Program to read a number n and print the natural numbers summation pattern.
# Case 1:
# Enter a number: 4
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10

n=int(input('Enter a number: '))
for i in range(1,n+1):
    sum = 0
    for j in range(1,i+1):
        print(j, sep=' ', end=' ')
        if(j<i):
            print('+', sep=' ', end=' ')
        sum+=j
    print('=', str(sum))

