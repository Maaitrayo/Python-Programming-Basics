#Lists in python
bicycle = ['treck', 'redline', 'specialized', 'cross-country']
print(bicycle)

#Accessing elements in a list, index position starts at 0
print(bicycle[0])
print(bicycle[0].title())

#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ["Rick", "Sham", "Radha", "Binod"]
print("The names are:\n\t"+names[0]+"\n\t"+names[1]+"\n\t"+names[2]+"\n\t"+names[3])
print("________________________________\n")

#Modifying a List
print("Modifying a list")
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print("After modifying the list: ")
bikes[0] = 'ducati'
print(bikes)
print("________________________________\n")


#Adding an element at the end of the list by using the command: append('object')
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print("After adding an element at the last position the list: ")
bikes.append('ducati')
print(bikes)
print("________________________________\n")


#inserting an element anywhere in the list by using the command: insert('position','object')
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print("After inserting an element to any desired positon in the list: ")
bikes.insert(1,'ducati')
print(bikes)
print("________________________________\n")

#Removing an element from the list using del list_name[position]
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print("After removing an element the list: ")
del bikes[2]
print(bikes)
print("________________________________\n")


#Removing an element from the list using pop() command, which removes the last element from the list
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print("After removing an element the list: ")
bikes.pop()
print(bikes)
print("And to pop from any position, use pop(index)")
bikes.pop(1)
print(bikes)
print("________________________________\n")

#Removing by value, by using, remove('value')
bikes = ['honda', 'yamaha', 'suzuki']
print(bikes)
print("After removing an element the list: ")
bikes.remove('honda')
print(bikes)
print("________________________________\n")


#Organizing a list
cars = ['bmw', 'audi', 'supra', 'toyota']
print(cars)
print("After sorting the list: ")
cars.sort()
print(cars)
print("________________________________\n")
print("To sort the list in reverse alphabetical order:")
cars = ['bmw', 'audi', 'supra', 'toyota']
cars.sort(reverse=True)
print(cars)
print("________________________________\n")


#To sort the list temporarily use sorted() function
cars = ['bmw', 'audi', 'supra', 'toyota']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#To print the reverse list
cars = ['bmw', 'audi', 'supra', 'toyota']
print("\n")
print(cars)
cars.reverse()
print(cars)
#To print the length of the list
cars = ['bmw', 'audi', 'supra', 'toyota']
print("The length of the list is: "+ str(len(cars)))

