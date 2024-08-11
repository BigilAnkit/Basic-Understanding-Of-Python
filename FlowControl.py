#Example: python if statement

number = 10

# check if number is greater than 0

if number > 0:
    print('Number is positive')

print('This statement always executes')


'''Example: python if..else statement'''

number = -10

if number> 0:
    print('Positive number')
else:
    print('Negative number')

print('This statement always executes')

'''Example: python if...elif...else statement'''

number = 0 

if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
else:
    print('zero')

print('This statement is always executed')


'''python nested if statements'''

number = 5

# outer if statment
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')
    
#outer else statement
else:
    print('Number is negative')

    #More on Python if....else statement


'''Python if shorthand'''

number = 10

if number >0:
    print('Positive')

number = 20

if number > 0: print('positive')

'''Ternary Operator in python (if...else)'''

grade = 40

if grade >= 50:
    result = 'Pass'
else: 
    result = 'Fail'

print(result)

# shorthand 

grade = 40

result = 'pass' if grade >= 50 else 'fail'

print(result)


'''Using logical operator'''

age = 35
salary = 6000

# add two conditions using and operator

if age >= 30 and salary >= 5000:
    print("Eligible for the premium membership")
else:
    print("Not eligible for the premium membership")
    