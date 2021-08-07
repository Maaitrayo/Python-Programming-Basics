# This is a Python Program to accept three distinct digits and print all possible combinations from the digits.

a = int(input('Enter first digit: '))
b = int(input('Enter second digit: '))
c = int(input('Enter third digit: '))
d = []
d.append(a)
d.append(b)
d.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])