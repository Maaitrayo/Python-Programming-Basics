# This is a Python Program to take in the marks of 5 subjects and display the grade.

# sub1 = int(input('Enter the marks of subject 1: '))
# sub2 = int(input('Enter the marks of subject 2: '))
# sub3 = int(input('Enter the marks of subject 3: '))
# sub4 = int(input('Enter the marks of subject 4: '))
# sub5 = int(input('Enter the marks of subject 5: '))
# average =((sub1+sub2+sub3+sub4+sub5)/5)*100

n = int(input('Enter range: '))
sub = []
for i in range(0,n):
    marks = int(input('Enter marks of subject'))
    sub.append(marks)
average = int((sum(sub)/5))

if(average>=90):
    print('GRADE A')
elif(average>=80 & average<90):
    print('GRADE B')
elif(average>=70 & average<80):
    print('GRADE C')
elif(average>=60 & average<70):
    print('GRADE D')
elif(average>=50 & average<60):
    print('GRADE E')
else:
    print('GRADE F')


# OR
# n = int(input('Enter range: '))
# sub = []
# for i in range(1,n):
#     marks = int(input('Enter marks of subject',i))
#     sub.append(marks)
# average = sum(sub)/5

