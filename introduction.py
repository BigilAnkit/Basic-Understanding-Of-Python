# print("Hello world")
# print("Ankit Gehlot")


# print a number 
print(25)

# Declare a variable
name = "John"
 
# print name
print(name)


# This is an example of multiline comment
# Craeted using multiple single-line comment
# The code prints the text Hello World

print("Hello World")

'''This is an example
of multiline comment'''
print("Multiline Comments code Hello World")

number1 = 10
number2 = 15

sum = number1 + number2

# sum of number1 and number2
print("The sum is : ",sum)
# print("The product is: "product)


# assing value to site_name variable

site_name = "Programiz.pro"

# print the value of site

print(site_name)

# Changing the value of a Variable in python

site_name = 'old value programiz.pro'

#print the old value of site_name
print(site_name)

# changing the value of a variable in python 
site_name = 'Apple user are made'

#print the new value of site_name 
print(site_name)


'''Example: Assiging multiple values to 
multiple variables'''

a,b,c = 5,3.2,'Hello'

# print a value
print(a)

#print b vlaue
print(b)

#print c vlaue
print (c)

'''If we want to assing the same value to 
multiple variable at once, we can do this as'''

site1 = site2 = 'programiz.pro Both are use'

print(site1)
print(site2) 


'''Example 1: Converting integer to float'''

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))


'''Example 2: Addition of String and integer Using Explicit Conversion'''

num_string = '12'
num_integer = 23

print("Data type of num_string before type Casting:",type(num_string))

num_string_to_ineger = int(num_string)

print("Data type of num_string after type Casting:",type(num_string_to_ineger))

# sum of convertion string to integer value

num_Sum1 = num_integer + num_string_to_ineger

print(num_Sum1)

'''Example 2: Python print() with end Parameter'''

#print with end whitspace

print('Good Morning Mumbai!', 2024, end=' ', sep='.')

print('It is rainy today',2025, sep='.')

# Example 3: Python print() with sep parameter

print('New year',2023,'See you soon!',sep ='. ')

#Example: Print python variables and Literals

number_4 = -10.6
name = 'Programiz'

#print literals
print(5)

#print variables
print(number_4)
print(name)


# Example:print Concatenated String
# We can also join two strings together inside the print() statement. for Example.

print('Progrmiz is '+' awesome')

#Output Formatting

'''Sometimes we would like to format our output to make it
look attractive. This can be done by using the 
str.format() method. For Example'''

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))


my_name = 'Ankit Gehlot'
age = 24

print('Hello folks my name is {} and {} years old'.format(my_name,age))

#Example: python user input

# using input() to take user input

# num = input('Enter a number:  ')

# print('You Entered: ',num)

# print('Data type of num: ', type(num))

'''In the above example, we have used the input()
funtion to take input from the user and stored the user
input in the num variable.

It is important to note that the entered value 10 is a string
not a number.So, type(num) return <class <'str'>'''

# num = int(input('Enter a number: '))

# print('you Entered: ',num)
# print(type(num), num)


# 6. Python Special operators

'''python language offers some special types of operators
like the identity operator and the membership operator
They are described below with examples'''

# Identity operators
'''In python, (is) and (is not) are used to check if two
values are located at the same memory location.
It's important to note that having two variables with 
equal values doesn't necessarily mean they are identical'''

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is  y1)
print(x2 is y2)
print(x3 is y3)

# important explaination
'''Here, we see that x1 and y1 are integers of the same
values, so they are equal as well as identical. the same is
the case with x2 and y2(strings).

But x3 and y3 are lists. They are equal but not identical
it is because the interpreter locates them separately in 
memory,although they are equal'''

#Membership Operators
'''In python, (in) and (not in ) are the membership operators,
They are used to test whether a value or variable is found
in a Sequence(String,Tupple,Set and Dictionary)'''

# Example 5: Membership operators in python

message = 'Hello World'
dict1 =  {1:'a',2:'b'}

# check if 'H' is present in message string
print("Membership operators in python\n",'H' in message)

# check if 'hello' is present in message string
print('Hello' not in message)

# check if '1' key is present in dict1
print(1 in dict1) 

#check if 'a' key is present in dict1
print('a' in dict1) 
