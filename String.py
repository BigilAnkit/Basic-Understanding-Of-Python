#python strings

#create a sting using double quotes
string1 = "Python programming"

# Create a string using single quotes
string1 = 'Python programming'

# create string type variables

name = "Python"
print(name)


message = "I Love Deepali"
print(message)

greet = 'hello'

# Access 1st index element
print(greet[:]) #

greet = 'hello'

# access 4th last element
print(greet[-4])

greet = 'Hello'

#access character from 1st index to 3rd index
print(greet[1:4])


message = 'Hola Amigos'

# assign new string to message variable
message = 'Hello Friends'

print(message)

# multiline string

message ="""
Never gonna give you up
Never gonna let you down
"""
print(message)


#iterate through a python string

greet = 'Hello'

#iterating through greet string

for letter in greet:
    print(letter)

'''pyhton string lenght'''

greet = 'Hello'

# count length of greet string
print(len(greet))

#string Membership test

print('a' in 'program')

print('at' not in 'battle')