# This is a Python Program to read a number n and compute n+nn+nnn.

n = int(input('Enter a number: '))
temp1 = str(n)+str(n)
temp2 = str(n)+str(n)+str(n)
sum = n+int(temp1)+int(temp2)
print(sum)
