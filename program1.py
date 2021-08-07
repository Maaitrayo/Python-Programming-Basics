#            This is a Python Program to Calculate the Average of Numbers in a Given List.

n = int(input("Enter the range: "))
a = []
for i in range(0,n):
    element = int(input("Enter the numbers: "))
    a.append(element)
average = sum(a)/n
print("The average is: ", round(average,2))