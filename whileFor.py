num_1 = int(input('Enter your number to be want end :-> '))
num_2 = int(input('Enter your number to be want start :-> '))

while num_2 <= num_1:
    print(num_2)
    num_2 +=1


# Python while loop 

# Calculate the sum of numbers until user enters 0
number = int(input('Enter a number: '))

total = 0

# iterate until the user enters 0
while number != 0:
    total += number
    number = int(input('Enter a number: '))

print('The sum is', total)




num1 = int(2.3)
print(num1) # prints 2

num2 = int(-2.8)
print(num2) #prints -2


num3 = float(5)
print(num3)

num4 = complex('3+5j')
print(num4) # prints(3+5j)

import random

print(random.randrange(10,20))

list = ['a','b','c','d','e']

# get random item from list1
print(random.choice(list))

# shuffle list1
random.shuffle(list)

#print the shuffled list
print(list)

#print random element
print(random.random())


import math

print(math.pi)

print(math.cos(math.pi))

print(math.log())




