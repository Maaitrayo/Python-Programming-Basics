# This is a Python Program to exchange the values of two numbers without using a temporary variable.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print('The original value of a is: ', str(a), 'The original value of b is: ', str(b))
a = a+b
b = a-b
a = a-b
print('The swaped value of a is: ', str(a), 'The swaped value of b is: ', str(b))
