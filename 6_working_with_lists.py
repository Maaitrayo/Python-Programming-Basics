#here we will see how to print each item in a list
names = ['maaitrayo', 'rohan', 'rupin', 'bangru']
print("The names are: ")
for name in names:
    print(name)
print("___________________________\n")

#A pizza problem
pizzas = ['plain', 'barbeque', 'pepperoni']
for pizza in pizzas:
    print( "I like " + pizza + " pizza !" )
print("Thank you for visting our store")
print("___________________________\n")


#Using in range() function
for i in range(0,11):
    print(i)
print("___________________________\n")


#Creating a list using range() function
numbers = list(range(1,6))
print(numbers)

#here we create a list to store even numbers. first argument accepts the starting value. second argument accepts the last value.
#Third argument accepts the number to be added at every iteration
numbers = list(range(2,11,2))
print(numbers)


#To store squared values
squared = []
for value in range(1,11):
    square = value**2
    squared.append(square)
print(squared)
print("OR")
squares = [value**2 for value in range(1,11)]
print(squares)
print("___________________________\n")


#min,max,sum functions
digits = [1,2,5,8,9,10,14,52,14,3]
print(min(digits))
print(max(digits))
print(sum(digits))
print("___________________________\n")


#Slicing through list
lists = ["ok", "me", "im", "in", "for", "this"]
print(lists[0:4])
print(lists[:2])
print(lists[-3:])
print("___________________________\n")


#Copying a list
my_foods = ['grape', 'tea', 'cookie', 'orange']
friends_foods = my_foods[:]
print("My foods are: ")
print(my_foods)
print("\nMy friends food are:")
print(friends_foods)
