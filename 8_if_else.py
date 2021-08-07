cars = ['bmw', 'audi', 'toyota', 'fiat']
for car in cars:
    if(car=='bmw'):
        print(car.upper())
    else:
        print(car.title())
print("__________________________\n")

#if else is case sensetive

#to check inequality
request = 'banana'
if request!= 'potato':
    print("Hold that potato")

print("__________________________\n")


#the keyword in:
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print("___________________________\n")

#The if-elif-else Chain
age = 12
if age<5:
    print("No need to pay")
elif age<18:
    print("Pay 5")
else:
    print("Pay 100")

