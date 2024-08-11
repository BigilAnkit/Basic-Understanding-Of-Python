# Create a set of integar type

student_id ={112, 114, 116, 118, 115}
print('Student ID:',student_id)

# Create a set of string type
vowel_letters ={'a','e','i','o','u'}
print('Vowel Letters:',vowel_letters)

# Create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:',mixed_set)


'''Create An Empty Set In Python'''

# create a an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:',type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:',type(empty_dictionary))


'''We can see there are no duplicate items in the set as a set cannot contain duplicates'''
numbers = {2,4,6,6,2,8} 
print(numbers)


'''Add and Update Set Item in Python

Sets are mutable. However, since they are unordered, indexing has no meaning.

we cannot access or change an element of a set using indexing
or slicing. The set data type does not support it'''

# Add Items to a set in python

numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)

#using add() Method
numbers.add(32) #add element on front side

print('Updated Set:',numbers)

companies ={'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple','google','apple']

# using update() method
companies.update(tech_companies)

print(companies)

'''Remove an Element from a set

We use the discard() method to remove the specifid 
element from a set. for example'''

language = {'Swift','Java','Python'}
print('Initial Set: ',language)

# remove 'Java' from a set
removedValue = language.discard('Java')

print('Set after remove(): ',language)
