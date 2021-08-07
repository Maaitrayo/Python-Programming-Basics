#values that can be changed are kept inside a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#writing over a tuple
values = (200, 50)
print("The original tuple is: ")
for value in values:
    print(value)

values = (400, 450)
print("The changed tuple is:")
for value in values:
    print(value)

