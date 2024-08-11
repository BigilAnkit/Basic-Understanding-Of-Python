# Create a Python list 

# a list of Three elements

ages = [19,26,29]
print(ages)

# a list containing string and numbers
student = ['Jack',32,'Computer Science']
print(student)

# an empty list
empty_list = []
print(empty_list)

# x = "axz"

# #convert to list
result = list(x)

# print(result)

languages = ['Python','Swift','C++']

#access the first element
print(languages[2]) #python


# # access item at index -1
print(languages[-1])

# # accesss item at index 2
print(languages[-3]) #python


My_list = ['p','r','o','g','r','a','m']

print(My_list[2:5])

print(My_list[5:])

print(My_list[:])



fruits = ['apple','banana','orange']
print('Originals List:', fruits)

# using append method
fruits.append('cherry')


print('Updated List: ',fruits)


# Add Elements at the Specified index

# The insert() methhod adds an element at the specified index. For Example,

fruits = ['apple','banana','orange']
print("Original List:",fruits)

# insert 'cherry' at index 2

fruits.insert(2,'cherry')

print("Updated List:", fruits)

'''Add Elements to a list from other iterables'''

'''We use the extend() method to add elementes to a list from other iterables. For example'''

numbers = [1,3,5]
print('Numbers:',numbers)

even_numbers = [2,4,6]

# adding elements of one list to another
numbers.extend(even_numbers)

print('Update Numbers:',numbers)

'''Change List Items

We can change the items of a list by assigning new values using the = operator.'''

color = ['Red','Black','Green']
print('Original List:',color)

# changing the third item to 'Blue'

color[2] = 'Blue'

print('Updated List: ',color)


'''Remove an Item from a List

We can remove an item from a list using the remove() method, For example,'''

numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers)


'''Remove one or more Element of a List

The del statement removes one or more items from a list, For example'''

names = ['John','Eva','Laura','Nick','Jack']

# Deleting the second item
del names[1]
print(names)

# Deleting items from index 1 t index 3

del names[1:4]
print(names) #error ! list doesn't exist.



'''We can also use the del statement to delete the entire list, For Example'''
names = ['John', 'Eva', 'Laura', 'Nick']

# deleting the entire list
del names

print(names)


'''Python List Lenght

We can use the built in len() function to find the number of elelments in 
a list. for example'''

cars = ['BMW','ODDY','Tesla','Mercedes']

print('Total Elements: ',len(cars))


'''Iterating Through a List

We can use a for loop to iterate over the elements of a list. For example'''

fruits = ['apple','banana','orange']

# iterate through the list
for fruit in fruits:
    print(fruit)


'''List Comprehension in  python

List Comprehension is a concise and elegant way to create a list,
For Examaple'''


# create a list with square values

numbers = [n**2 for n in range(1,6)]
print(numbers)


'''check if an item exists in the python list

We use the in Keyword to check if an item exists in the list
for example'''

fruits = ['apple','cherry','banana']

print('orange' in fruits) # false
print('cherry' in fruits) # true