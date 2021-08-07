print("The Original string:")
name = "ada lovelace\n"
print(name)

print("Modified:")
#title() function sets the first letter in uppercase
name = "ada lovelace"
modified_name = name.title()
print(modified_name)

#upper() function sets all the letters into uppercase
print(name.upper())

#lower() function sets all the letters into lowercase
print(name.lower())
print("________________________\n")

#Concatenating strings
first_name = "Maaitrayo"
last_name = "Das"
full_name = first_name + " " + last_name
message = full_name
print("Hello, my name is "+full_name+" !")
print("________________________\n")


#Some use of escape sequence ( \n--> next line & \t-->white spaces)
print("Some languages are:\nPython\nC\nJava\nC++\n")
print("Some languages are:\n\tPython\n\tC\n\tJava\n\tC++\n")

#Removing white spaces operations: rstrip()--> removing white spaces from right side, lstrip() --> from left side, strip()--> entire
print("The Original:")
python = " PYTHON "
print(python)
print("Modified: ")
print(python.rstrip())
print(python.lstrip())
print(python.strip())



